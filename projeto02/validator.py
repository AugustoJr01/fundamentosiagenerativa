import json
import logging
from collections import Counter
from statistics import mean

CATEGORIAS_PERMITIDAS = ["Suporte", "Vendas", "Financeiro", "Geral"]
FALLBACK_CATEGORIA = "Geral"

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_json_resposta(resposta_str):
    try:
        return json.loads(resposta_str)
    except json.JSONDecodeError:
        logging.error(f"JSON inválido: {resposta_str}")
        return None


def validar_categoria(resposta_json):
    if not resposta_json:
        return False
    
    categoria = resposta_json.get("categoria")
    return categoria in CATEGORIAS_PERMITIDAS


def aplicar_fallback(motivo="Erro desconhecido"):
    logging.warning(f"Fallback aplicado. Motivo: {motivo}")
    return {
        "categoria": FALLBACK_CATEGORIA,
        "confianca": 0.0,
        "fallback": True
    }


def calcular_confianca(valido):
    return 1.0 if valido else 0.0


def processar_resposta(resposta_str):
    resposta_json = parse_json_resposta(resposta_str)

    if not resposta_json:
        return aplicar_fallback("JSON inválido")

    if not validar_categoria(resposta_json):
        return aplicar_fallback("Categoria inválida")

    confianca = calcular_confianca(True)

    resposta_final = {
        "categoria": resposta_json["categoria"],
        "confianca": confianca,
        "fallback": False
    }

    logging.info(f"Classificação válida: {resposta_final}")
    return resposta_final


def gerar_metricas(resultados):
    total = len(resultados)
    contador = Counter([r["categoria"] for r in resultados])
    fallbacks = sum([1 for r in resultados if r["fallback"]])
    confiancas = [r["confianca"] for r in resultados]

    distribuicao = {
        categoria: round((contador[categoria] / total) * 100, 2)
        for categoria in CATEGORIAS_PERMITIDAS
    }

    metricas = {
        "total_classificacoes": total,
        "fallbacks": fallbacks,
        "taxa_erro_percentual": round((fallbacks / total) * 100, 2),
        "confianca_media": round(mean(confiancas), 2),
        "distribuicao": distribuicao
    }

    return metricas