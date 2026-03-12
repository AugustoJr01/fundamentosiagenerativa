import datetime
import random
import string

def data_atual():
    """Retorna a data de hoje."""
    return datetime.date.today()

def gerar_senha(tamanho=12):
    """Gera uma senha segura com letras, números e símbolos."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def converter_temperatura(celsius):
    """Converte Celsius para Fahrenheit."""
    return (float(celsius) * 9/5) + 32