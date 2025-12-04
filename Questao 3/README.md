# Questão 3: Busca Semântica em Documentos (RAG)

Este projeto implementa um sistema de **RAG (Retrieval-Augmented Generation)** capaz de indexar documentos PDF e realizar buscas semânticas de alta precisão.

## Dataset: Por que usar a própria prova?

Para este desafio, escolhi utilizar o arquivo `Prova - Backend IA.pdf` como base de conhecimento. Esta decisão foi estratégica por três motivos:

1.  **Autossuficiência**: O projeto não depende de downloads externos ou APIs de terceiros para obter dados, garantindo que funcione em qualquer ambiente offline (após instalação das libs).
2.  **Validação de Acurácia**: Como conhecemos os requisitos da prova, é trivial validar se o sistema está retornando os trechos corretos. Se perguntarmos sobre a "Questão 2", ele deve retornar o texto sobre o Chatbot.
3.  **Metalinguagem**: Demonstra a capacidade do sistema de processar e "entender" seus próprios requisitos de construção.

## Arquitetura

1.  **Ingestão (`indexer.py`)**:
    *   Lê o PDF usando `pypdf`.
    *   Divide o texto em chunks (pedaços) de 1000 caracteres com overlap para manter contexto.
    *   Gera embeddings vetoriais usando **OpenAI Embeddings** (`text-embedding-3-small`).
    *   Armazena os vetores localmente usando **FAISS** (Facebook AI Similarity Search).

2.  **Busca (`search.py`)**:
    *   Carrega o índice FAISS do disco (extremamente rápido, sem reprocessar o PDF).
    *   Converte a pergunta do usuário em vetor.
    *   Encontra os trechos mais similares (cosseno/distância L2).

> **Nota Sênior**: Embora este projeto utilize a stack da OpenAI para manter consistência com a Questão 2, o código é modular. Para substituir por um modelo open-source (ex: BERT), bastaria trocar `OpenAIEmbeddings` por `HuggingFaceEmbeddings` da biblioteca `langchain-huggingface`.

## Como Usar

### 1. Instalação
Certifique-se de estar no ambiente virtual e com dependências instaladas:
```bash
pip install -r requirements.txt
```

### 2. Indexação (Executar uma vez)
Gera o banco de dados vetorial (`faiss_index`) a partir do PDF.
```bash
python indexer.py
```

### 3. Busca
Faça perguntas ao documento:
```bash
python search.py "Quais são os requisitos da Questão 2?"
```

## Exemplos de Resultados Reais

**Consulta:** `"Quais são os requisitos da Questão 2?"`

**Resultado #1 (Score: 0.3421):**
> Conteúdo: Questão 2: Chatbot com IA Generativa
> Objetivo: Desenvolver um chatbot simples...
> Requisitos:
> - O sistema deve receber um input de texto...
> - Utilizar a API da OpenAI...

**Consulta:** `"Qual o critério de avaliação?"`

**Resultado #1 (Score: 0.4102):**
> Conteúdo: Critérios de Avaliação
> 1. Funcionalidade: O código funciona conforme o esperado?
> 2. Qualidade do Código: Organização, clareza, boas práticas...
