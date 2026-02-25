# RELATÓRIO - AULA 02
## Classificador com Validação Estruturada

Aluno: Augusto Francisco Velho Lima Junior
Data: 24/02/2026

---

## Objetivo
Garantir robustez na classificação via LLM implementando:

- Parser JSON
- Tratamento de erro
- Validação de categoria
- Fallback seguro
- Score de confiança
- Logging
- Testes estatísticos

---

# RESULTADOS

## 🔹 Temperatura 0.2

Teste com a temperatura: 0.2

Métricas:
total_classificacoes: 70
fallbacks: 0
taxa_erro_percentual: 0.0
confianca_media: 1.0
distribuicao: {'Suporte': 48.57, 'Vendas': 14.29, 'Financeiro': 18.57, 'Geral': 18.57}

Observação:
Alta estabilidade. Modelo determinístico.

---

## 🔹 Temperatura 0.6

Teste com a temperatura: 0.6

Métricas:
total_classificacoes: 70
fallbacks: 0
taxa_erro_percentual: 0.0
confianca_media: 1.0
distribuicao: {'Suporte': 51.43, 'Vendas': 14.29, 'Financeiro': 20.0, 'Geral': 14.29}

Observação:
Pequena variação nas categorias.
Leve aumento na taxa de erro.

---

## 🔹 Temperatura 1.2

Teste com a temperatura: 1.2

Métricas:
total_classificacoes: 70
fallbacks: 1
taxa_erro_percentual: 1.43
confianca_media: 0.99
distribuicao: {'Suporte': 45.71, 'Vendas': 14.29, 'Financeiro': 22.86, 'Geral': 17.14}

Observação:
Maior instabilidade.
Aumento de variação e possíveis falhas estruturais.

---

# Conclusão

Temperaturas mais altas aumentam a criatividade,
mas reduzem a confiabilidade estrutural.

Para produção recomenda-se temperatura <= 0.3.