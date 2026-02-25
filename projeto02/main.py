from classfier import classificar_mensagem
from validator import gerar_metricas

mensagens_cliente = [
    "Quero contratar o plano premium.",
    "O sistema está com erro.",
    "Quero cancelar minha assinatura.",
    "Quero falar com atendente.",
    "Preciso de ajuda com meu pagamento",
    "Gostaria de atualizar as informações da minha conta.",
    "Vocês trabalham sábado?"
]

temperaturas = [0.2, 0.6, 1.2]

for temp in temperaturas:
    print("\n-------------------------------")
    print(f"Teste com a temperatura: {temp}")

    resultados = []

    for i in range(10):
        for mensagem in mensagens_cliente:
            resposta = classificar_mensagem(mensagem, temperature=temp)
            resultados.append(resposta)

    metricas = gerar_metricas(resultados)

    print("\nMétricas:")
    for k, v in metricas.items():
        print(f"{k}: {v}")