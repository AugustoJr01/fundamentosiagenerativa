import os
from classifier import classificar_raio_x

def main():
    print("="*50)
    print(" 🩺 SISTEMA DE VALIDAÇÃO: DIAGNÓSTICO POR IMAGEM ")
    print("="*50)
    
    while True:
        print("\n(Dica: coloque uma imagem .jpg ou .png nesta mesma pasta)")
        caminho = input("Digite o nome da imagem (ou 'sair' para encerrar): ").strip()
        
        if caminho.lower() == 'sair':
            break
            
        if not os.path.exists(caminho):
            print(f"❌ Erro: O arquivo '{caminho}' não foi encontrado.")
            continue
            
        print("\n⏳ Enviando imagem para o modelo de Visão Computacional...")
        resposta_json = classificar_raio_x(caminho)
        
        print("\n✅ Diagnóstico Concluído:")
        print(resposta_json)
        print("-" * 50)

if __name__ == "__main__":
    main()