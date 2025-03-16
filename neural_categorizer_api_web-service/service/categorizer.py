import joblib

class EmailClassifier:
    def __init__(self):
        # Carregar o modelo e o vetorizador
        self.modelo = joblib.load('rede/modelo_titulos_email.pkl')
        self.vectorizer = joblib.load('rede/vectorizer_titulos_email.pkl')

    def classify(self, titulo):
        novos_titulos_pre = [titulo.lower()]
        X_novos = self.vectorizer.transform(novos_titulos_pre)
        return self.modelo.predict(X_novos)

