import os
import base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    """Converte a imagem para o formato Base64 que a IA entende."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analisar_imagem_com_ia(image_path, prompt_sistema):
    """Envia a imagem e as instruções para o modelo de visão do Groq."""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    base64_image = encode_image(image_path)
    
    # Estrutura específica para modelos multimodais (texto + imagem)
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_sistema},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ]
    
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct", # Modelo de visão do Groq
        messages=messages,
        temperature=0.1 # Temperatura baixa para o diagnóstico ser preciso e não criativo
    )
    return response.choices[0].message.content.strip()