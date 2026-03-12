import os
import json
import re
from groq import Groq
from dotenv import load_dotenv
from tools import data_atual, gerar_senha, converter_temperatura

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

ARQUIVO_HISTORICO = "historico.json"
LIMITE_MEMORIA = 10
PERSONA = "Você é um assistente virtual sarcástico, nerd e super inteligente. Você responde de forma direta, resolve os problemas do usuário, mas sempre com um toque de humor irônico de quem sabe mais que os humanos."

historico_mensagens = []

def carregar_historico():
    global historico_mensagens
    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
                historico_mensagens = json.load(f)
        except:
            historico_mensagens = [{"role": "system", "content": PERSONA}]
    else:
        historico_mensagens = [{"role": "system", "content": PERSONA}]

def salvar_historico_json():
    with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
        json.dump(historico_mensagens, f, ensure_ascii=False, indent=4)

def adicionar_mensagem(role, content):
    global historico_mensagens
    historico_mensagens.append({"role": role, "content": content})
    if len(historico_mensagens) > LIMITE_MEMORIA + 1:
        historico_mensagens.pop(1)
    salvar_historico_json()

def chat(pergunta):
    adicionar_mensagem("user", pergunta)
    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=historico_mensagens
    )
    resposta_conteudo = resposta.choices[0].message.content
    adicionar_mensagem("assistant", resposta_conteudo)
    return resposta_conteudo

carregar_historico()
print("*"*50)
print(" Assistente Sarcástico Iniciado!")
print(" Comandos: 'sair' para encerrar | '/limpar' para resetar a memória")
print("*"*50)

while True:
    pergunta = input("\nVocê: ").strip()

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Assistente: Finalmente paz. Encerrando o chat!")
        break

    if pergunta.lower() == "/limpar":
        historico_mensagens = [{"role": "system", "content": PERSONA}]
        salvar_historico_json()
        print("Assistente: Memória da conversa apagada. Quem é você mesmo?")
        continue

    texto_min = pergunta.lower()
    
    if "data" in texto_min or "dia é hoje" in texto_min:
        adicionar_mensagem("user", pergunta)
        resposta = f"Segundo meus relógios internos de altíssima precisão, hoje é {data_atual()}."
        adicionar_mensagem("assistant", resposta)
        print("Assistente: " + resposta)
        continue
        
    if "gerar senha" in texto_min or "criar senha" in texto_min:
        adicionar_mensagem("user", pergunta)
        senha = gerar_senha()
        resposta = f"Aqui está uma senha inquebrável gerada pela minha rotina local: '{senha}'. Tente não esquecer."
        adicionar_mensagem("assistant", resposta)
        print("Assistente: " + resposta)
        continue
        
    if "converter" in texto_min and "celsius" in texto_min:
        try:
            numeros = re.findall(r'-?\d+\.?\d*', texto_min)
            if numeros:
                celsius = float(numeros[0])
                fahrenheit = converter_temperatura(celsius)
                adicionar_mensagem("user", pergunta)
                resposta = f"Cálculo executado localmente: {celsius}°C equivale a {fahrenheit}°F. Viu? Nem precisei usar a rede neural pra isso."
                adicionar_mensagem("assistant", resposta)
                print("Assistente: " + resposta)
                continue
        except Exception:
            pass 

    resposta = chat(pergunta)
    print("Assistente:", resposta)