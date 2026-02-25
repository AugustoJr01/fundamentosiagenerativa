from llm_client import gerar_resposta
from validator import processar_resposta

CATEGORIAS = ["Suporte", "Vendas", "Financeiro", "Geral"]

def classificar_mensagem(mensagem, temperature=0.2):
    prompt = f"""
    Classifique a mensagem abaixo em uma das seguintes categorias: {', '.join(CATEGORIAS)}.
    Retorne apenas um JSON válido no formato:
    {{
        "categoria": "nome_categoria"
    }}

    NÃO retorne texto adicional.
    Mensagem: "{mensagem}"
    """

    resposta_raw = gerar_resposta(prompt, temperature)

    resposta_processada = processar_resposta(resposta_raw)

    return resposta_processada