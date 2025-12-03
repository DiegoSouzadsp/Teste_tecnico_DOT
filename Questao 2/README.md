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
    ```

> **Nota**: O arquivo `.env` já está no `.gitignore` para segurança.

## Como Executar

Execute o arquivo principal:

```bash
python main.py
```

## Exemplos de Uso

O chatbot aceita perguntas em linguagem natural. Exemplos:

*   *"Como criar uma lista em Python?"*
*   *"Explique o conceito de decorators com um exemplo."*
*   *"Qual a diferença entre tupla e lista?"*

## Estrutura do Código

*   **`main.py`**: Ponto de entrada. Gerencia o loop de interação com o usuário (CLI).
*   **`chatbot.py`**: Contém a classe `PythonChatbot`, responsável pela lógica do Langchain, configuração do modelo e prompt.
*   **`requirements.txt`**: Lista de bibliotecas necessárias.

## Tecnologias Utilizadas

*   **Langchain**: Framework para orquestração de LLMs.
*   **OpenAI API**: Motor de inteligência (GPT-4o-mini).
*   **Python-dotenv**: Gerenciamento de variáveis de ambiente.
