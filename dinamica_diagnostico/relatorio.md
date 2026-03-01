# Dinâmica Técnica: Diagnóstico por Imagem

**Aluno:** Augusto Francisco Velho Lima Junior
**Cenário:** Diagnóstico por Imagem

### 1. Variável alvo (y)
É a classe ou o diagnóstico que o modelo deve prever a partir da imagem. Dependendo do problema específico, pode ser uma classificação binária (ex: `0 = Saudável`, `1 = Com Anomalia/Pneumonia`) ou uma classificação multiclasse (ex: `Tumor Benigno`, `Tumor Maligno`, `Sem Tumor`).

### 2. Variáveis de entrada (X)
São os dados visuais fornecidos para a IA. Tratam-se dos pixels da imagem médica (como um Raio-X, Tomografia ou Ressonância Magnética). O modelo processa a imagem como uma matriz numérica, analisando padrões, bordas, texturas e densidades de cores.

### 3. Tipo de aprendizado
**Aprendizado Supervisionado (Classificação).** Para que o sistema consiga diagnosticar corretamente, ele precisa ser treinado com um grande volume de dados históricos contendo imagens médicas que já foram previamente analisadas e rotuladas por médicos especialistas (indicando qual é o diagnóstico correto para cada imagem).

### 4. Métrica
A métrica principal de otimização deve ser o **Recall (Revocação ou Sensibilidade)**.
*Justificativa:* Na área da saúde, o modelo deve ser rigoroso para evitar Falsos Negativos. Dizer a um paciente doente que ele está saudável pode atrasar o tratamento e custar uma vida. É preferível ter uma taxa maior de Falsos Positivos (que serão descartados após exames complementares) do que deixar um caso real escapar.

### 5. Risco ético
* **Vieses de Dados (Bias):** Se o modelo for treinado majoritariamente com imagens de um perfil demográfico específico, sua precisão pode cair drasticamente ao diagnosticar pessoas de outras etnias, idades ou gêneros.
* **Responsabilidade e Automação Excessiva:** A IA não deve substituir o médico. O risco é o profissional de saúde confiar cegamente no diagnóstico da máquina (viés de automação). A responsabilidade final e legal sobre o paciente deve ser sempre do especialista humano.