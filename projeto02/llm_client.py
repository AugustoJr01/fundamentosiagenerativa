## é quem conecta com a API.

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

open_api_key = os.getenv("OPENAI_AP_KEY")
groq_api_key = os.getenv("GROQ_AP_KEY")

client = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")

def gerar_resposta(prompt, temperature=0.2):
    resposta = client.responses.create(
        model= "openai/gpt-oss-20b",
        temperature=temperature,
        input=prompt
    )
    return resposta.output_text