from controllers.api_connector import get_emails, update_email
from service.categorizer import EmailClassifier
import time

def main():
    # URL do endpoint Flask
    endpoint_url = "http://172.19.113.12:5000/emails"
    print("Buscando emails do servidor Flask...")
    # Uso do classificador
    classifier = EmailClassifier()

    # Busca e processa os emails
    while True:
        emails = get_emails(endpoint_url)
        if emails:
            for email in emails:
                if email['status'] == "Armazenado":
                    print(f"{len(emails)} emails recebidos. Processando...")
                    subject = email['titulo']
                    category = classifier.classify(subject)
                    if category == "Acesso a Computadores":
                        category = "Acesso"
                    elif category == "Banca de Defesa":
                        category = "Defesa"
                    email['status'] = 'Categorizado'
                    email['tipo'] = category
                    id = email['id']
                    print(category)
                    update_email(email, id)
        else:
            print("Nenhum email foi recebido.")
        time.sleep(60)


if __name__ == "__main__":
    main()