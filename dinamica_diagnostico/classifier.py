from llm_client import analisar_imagem_com_ia

def classificar_raio_x(caminho_imagem):
    prompt = """
    Você é um assistente de IA atuando como um modelo de Aprendizado Supervisionado para Diagnóstico por Imagem (Radiologia).
    Sua tarefa é analisar os pixels da imagem fornecida e classificá-la.
    
    DIRETRIZES DO MODELO (Conforme Relatório Técnico):
    1. Variável Alvo (y): Classifique como 'Saudável' ou 'Com Anomalia/Pneumonia'.
    2. Variáveis de Entrada (X): Baseie-se exclusivamente nos padrões e densidade de pixels da imagem médica.
    3. Métrica (Recall): Seja extremamente conservador para evitar Falsos Negativos. Na dúvida mínima, aponte anomalia.
    4. Risco Ético: Você NÃO substitui um médico e está sujeito a vieses.
    
    Responda EXCLUSIVAMENTE em formato JSON, sem nenhum outro texto (nem mesmo marcações markdown como ```json), usando esta estrutura:
    {
        "status": "sucesso",
        "diagnostico_y": "Saudável ou Com Anomalia/Pneumonia",
        "variaveis_entrada_X": "Descrição do que os pixels mostram...",
        "tipo_aprendizado": "Classificação via Aprendizado Supervisionado simulado",
        "foco_metrica": "Otimizado para alto Recall (minimizando falsos negativos)",
        "aviso_etico": "Risco de automação. O diagnóstico deve ser validado por um médico."
    }
    """
    try:
        resultado = analisar_imagem_com_ia(caminho_imagem, prompt)
        return resultado
    except Exception as e:
        return f'{{"status": "erro", "mensagem": "{str(e)}"}}'