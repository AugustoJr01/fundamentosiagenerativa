# Projeto 04 - Assistente com Memória

Este projeto é a evolução do chatbot base, agora implementando injeção de persona, persistência de dados (salvamento em disco), janela de contexto (limite de memória) e execução de funções nativas em Python para tarefas determinísticas.

## Como Executar
1. Certifique-se de ter as bibliotecas instaladas executando: `pip install -r requirements.txt`
2. Crie um arquivo `.env` na raiz do projeto e adicione a sua chave da OpenAI: `OPENAI_API_KEY=sua_chave_aqui`
3. Execute o programa principal: `python main.py`

## Funcionalidades Implementadas
- **Controle de Memória:** O comando `/limpar` apaga imediatamente o histórico da conversa e o arquivo JSON.
- **Persona Sarcástica:** Um *System Prompt* instrui a IA a responder de forma humorada e direta.
- **Limite de Contexto:** A memória é limitada a reter apenas o *System Prompt* e as últimas 10 mensagens, evitando estouro de limite da API.
- **Funções Python (Tools):** A aplicação detecta a intenção do usuário e roda as funções `data_atual()`, `gerar_senha()` e `converter_temperatura()` localmente.
- **Persistência de Dados:** O estado do chatbot é salvo no arquivo `historico.json` e carregado sempre que o script é reiniciado.

## Dificuldades encontradas
- **Filtro de segurança:** Fui testar se o assistente estava realmente salvando as conversas no arquivo JSON e mandei ele guardar a "senha do servidor da faculdade". O histórico funcionou e ele lembrou, mas as travas de segurança do modelo Llama acharam que era um vazamento real de dados e a IA se recusou a me devolver a senha. Tive que refazer o teste com informações inofensivas (como o nome do meu cachorro, o Floquinho, e que minha comida favorita é lasanha) pra provar que a memória estava funcionando.
- **Limpar a memória:** Na hora de limitar o histórico para guardar apenas as últimas 10 mensagens, esbarrei num problema. Se eu simplesmente mandasse o código apagar a mensagem mais velha da lista, a IA acabava esquecendo a própria personalidade (porque o System Prompt era deletado junto). A solução foi ajustar o código para apagar sempre a segunda mensagem mais antiga da lista (usando pop(1)), garantindo que a instrução de "assistente sarcástico" ficasse sempre trancada e protegida no topo da memória.

---

## Reflexão (Questões do Desafio)

**1. Se o histórico crescer muito, quais problemas podem ocorrer no uso de LLMs?**
Se não houver um limite (`pop()` das mensagens mais antigas), o texto enviado para a API crescerá a cada interação. Isso gera três problemas:
* **Estouro de Janela de Contexto:** O modelo rejeitará a requisição assim que o limite de tokens daquele modelo for ultrapassado.
* **Custo Financeiro:** As APIs cobram por token trafegado (entrada + saída). Enviar um histórico gigante a cada pergunta custa muito caro.
* **Perda de Atenção ("Lost in the Middle"):** LLMs tendem a "esquecer" ou dar menos importância a informações que ficam no meio de prompts extremamente longos, focando apenas no início ou no fim do texto.

**2. Por que algumas tarefas são melhores resolvidas por funções Python do que pelo próprio LLM?**
LLMs são modelos probabilísticos baseados em previsão de texto, não são calculadoras. Para tarefas matemáticas complexas, buscas precisas em banco de dados ou acesso a informações em tempo real (como a data de hoje ou a cotação do dólar), o LLM pode "alucinar" respostas. Executar essas tarefas usando código Python nativo garante 100% de precisão e segurança de forma determinística, enquanto o LLM serve apenas como interface de comunicação.

**3. Quais riscos existem ao deixar que o LLM tome decisões sobre quando usar uma função?**
A delegação total (conhecida como *Agentic Workflow* ou *Tool Calling*) traz o risco de **Falsos Positivos** (a IA invocar a execução de um script no momento errado) ou de sofrer **Prompt Injection** (o usuário mal-intencionado convencer a IA a executar uma função destrutiva, como apagar um banco de dados ou realizar transações bancárias). A tomada de decisão do LLM precisa sempre passar por uma camada de validação e permissão restrita.