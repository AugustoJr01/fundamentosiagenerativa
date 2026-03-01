from llm_client import LLMClient
from retriever import load_conhecimento, simple_retriever
from validator import validate_json
from prompt import build_system_prompt

def main():
    provider = input("Escolha o provedor (openai/groq): ").strip().lower()
    client = LLMClient(provider=provider)
    
    # Carrega a memória apenas uma vez no início
    load_conhecimento()

    while True:
        query = input("\nDigite sua pergunta (ou 'sair' para encerrar): ").strip()
        if query.lower() == "sair":
            break
        
        # O retriever agora só precisa da query, pois a memória é global no arquivo
        contexto = simple_retriever(query)
        system_prompt = build_system_prompt()

        # CONSERTO AQUI: Juntamos a pergunta do usuário com o contexto recuperado
        user_prompt = f"Contexto recuperado da base:\n{contexto}\n\nPergunta do usuário:\n{query}"

        response_text = client.generate_text(system_prompt, user_prompt)

        try:
            is_valid, data = validate_json(response_text)
            if is_valid:
                print(f"[{data.get('status', 'sem status').upper()}] {data.get('resposta', '')}")
        except ValueError as e:
            print(f"Erro de validação: {e}")
            print(f"Texto bruto recebido: {response_text}")

if __name__ == "__main__":
    main()