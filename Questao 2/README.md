# Questão 2: Chatbot com IA Generativa (Langchain + OpenAI)

Este projeto implementa um chatbot especialista em programação Python utilizando **Langchain** e a API da **OpenAI (GPT-4)**.

## Funcionalidades

*   **Especialista em Python**: Prompt otimizado para responder dúvidas técnicas de programação.
*   **Interface CLI**: Interação simples e direta via terminal.
*   **Configurável**: Permite ajuste de modelo e temperatura (criatividade) via código.
*   **Tratamento de Erros**: Lida graciosamente com falhas de API e falta de configuração.

## Pré-requisitos

*   Python 3.9+
*   Uma chave de API da OpenAI válida.

## Instalação

1.  Navegue até a pasta do projeto:
    ```bash
    cd "Questao 2"
    ```

2.  Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1.  Crie um arquivo `.env` na raiz da pasta `Questao 2`.
2.  Adicione sua chave da OpenAI:
    ```env
    OPENAI_API_KEY=sua-chave-aqui-sk-...
    OPENAI_MODEL=gpt-4o-mini  # Opcional: gpt-4, gpt-3.5-turbo, etc.
    ```

### Observabilidade (LangSmith)

Este projeto é compatível nativamente com o **LangSmith** para tracing e monitoramento. Para ativar, basta adicionar as seguintes variáveis ao seu `.env`:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=sua-chave-langchain
LANGCHAIN_PROJECT=prova-backend-ia
```

Não é necessário alterar o código, pois a biblioteca `langchain` detecta essas variáveis automaticamente.

> **Nota**: O arquivo `.env` já está no `.gitignore` para segurança.

## Como Executar

Execute o arquivo principal:

```bash
python main.py
```

## Exemplos de Uso

O chatbot aceita perguntas em linguagem natural. Abaixo, alguns exemplos reais de interação:

### Exemplo 1: Conceitos Básicos
**Você:** "Qual a diferença entre tupla e lista?"
**Bot:**
> Em Python, a principal diferença é a **mutabilidade**:
> *   **Listas (`[]`)**: São mutáveis, ou seja, você pode adicionar, remover ou alterar itens após a criação.
> *   **Tuplas (`()`)**: São imutáveis. Uma vez criadas, não podem ser alteradas.
>
> Use tuplas para dados constantes e listas para coleções dinâmicas.

### Exemplo 2: Código Prático
**Você:** "Como criar uma lista em Python?"
**Bot:**
> Para criar uma lista, use colchetes `[]` separando os itens por vírgula:
> ```python
> frutas = ["maçã", "banana", "laranja"]
> print(frutas[0])  # Saída: maçã
> ```

### Exemplo 3: Explicação Técnica
**Você:** "Explique o que é list comprehension."
**Bot:**
> List comprehension é uma forma concisa de criar listas. Em vez de usar um loop `for` tradicional, você pode fazer em uma linha:
>
> ```python
> # Tradicional
> quadrados = []
> for x in range(5):
>     quadrados.append(x**2)
>
> # List Comprehension
> quadrados = [x**2 for x in range(5)]
> ```
> É mais "pythônico" e geralmente mais rápido.

## Estrutura do Código

*   **`main.py`**: Ponto de entrada. Gerencia o loop de interação com o usuário (CLI).
*   **`chatbot.py`**: Contém a classe `PythonChatbot`, responsável pela lógica do Langchain, configuração do modelo e prompt.
*   **`requirements.txt`**: Lista de bibliotecas necessárias.

## Tecnologias Utilizadas

*   **Langchain**: Framework para orquestração de LLMs.
*   **OpenAI API**: Motor de inteligência (GPT-4o-mini).
*   **Python-dotenv**: Gerenciamento de variáveis de ambiente.
