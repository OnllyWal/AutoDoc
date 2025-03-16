import requests

def get_emails(endpoint_url):
    try:
        # Faz a requisição GET para o endpoint Flask
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Verifica se houve erro HTTP
        emails = response.json()  # Converte a resposta JSON para um objeto Python (lista de dicionários)
        return emails
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do endpoint: {e}")
        return []
    

def update_email(email,id):
    response = requests.put(f"http://172.19.113.12:5000/emails/{id}", json=email)
    print(response.json)