import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

titulos = [
    # Acesso a Computadores
    "Solicitação de acesso às máquinas do laboratório",
    "Preciso de login e senha para o PC da sala de estudos",
    "Problema ao acessar os computadores do laboratório",
    "Erro no login do servidor central",
    "Configuração de dados de entrada para computadores remotos",
    "Como conseguir acesso ao PC do campus?",
    "Informações sobre dados de entrada para os computadores",
    "Problema ao configurar o login no PC remoto",
    "Solicitação de senha para acessar o computador do servidor",
    "Dificuldades para acessar as máquinas do laboratório",
    
    # Banca de Defesa
    "Convite para a banca de defesa do doutorado",
    "Agendamento de banca de mestrado",
    "Informações sobre a defesa de dissertação",
    "Participação na banca de mestrado",
    "Dados necessários para a defesa de tese",
    "Confirmação da banca de defesa do mestrado",
    "Detalhes da defesa de mestrado em engenharia",
    "Solicitação de presença na banca de dissertação",
    "Preparativos para a defesa de tese de doutorado",
    "Datas disponíveis para a banca de defesa",
]

categorias = [
    # Acesso a Computadores
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",
    "Acesso a Computadores",

    # Banca de Defesa
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
    "Banca de Defesa",
]

# Pré-processamento, vetorização e treinamento
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(titulos)

modelo = MultinomialNB()
modelo.fit(X, categorias)

# Salvar o modelo e o vetorizador
joblib.dump(modelo, 'modelo_titulos_email.pkl')
joblib.dump(vectorizer, 'vectorizer_titulos_email.pkl')