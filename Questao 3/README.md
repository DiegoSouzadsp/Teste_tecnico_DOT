# Questão 3: Busca Semântica em Documentos (RAG)

Este projeto implementa um sistema de **RAG (Retrieval-Augmented Generation)** capaz de indexar documentos PDF e realizar buscas semânticas de alta precisão.

## Dataset e Flexibilidade

O sistema foi projetado para ser **agnóstico ao conteúdo**. Embora utilizemos a prova como exemplo inicial, você pode indexar qualquer conjunto de documentos (artigos, posts de blog, contratos, etc.).

Para adicionar novos documentos:
1.  Coloque os arquivos `.pdf` na pasta `Questao 3`.
2.  Execute `python indexer.py` novamente.
3.  O sistema irá gerar embeddings para todos os arquivos e atualizar o índice.

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

## Suporte a Múltiplos Documentos (Feature Sênior)

O sistema foi projetado para indexar **todos os PDFs** presentes na pasta `Questao 3`. Isso demonstra escalabilidade e flexibilidade.

Para fins de teste, o projeto inclui:
1.  `Prova_Backend_IA.pdf`: O enunciado original.
2.  `Politica_Privacidade_Dummy.pdf`: Um documento fictício gerado automaticamente para validar a busca em múltiplos contextos.

O script `indexer.py` varre a pasta, processa todos os arquivos `.pdf` e cria um índice unificado. O `search.py` retorna, além do conteúdo, a **fonte** (nome do arquivo) de onde a informação foi extraída.

## Exemplos de Resultados Reais

**Consulta:** `"Quais são os requisitos da Questão 2?"`
**Resultado #1:**
> Fonte: Prova_Backend_IA.pdf
> Conteúdo: Questão 2: Chatbot com IA Generativa...

**Consulta:** `"Qual o contato do DPO?"`
**Resultado #1:**
> Fonte: Politica_Privacidade_Dummy.pdf
> Conteúdo: 4. Contato do DPO: Para assuntos de LGPD, entre em contato com dpo@exemplo.com.

## Como Usar

### 1. Instalação
```bash
pip install -r requirements.txt
```

### 2. Geração de Dados (Opcional)
Se quiser recriar o PDF dummy:
```bash
python generate_dummy_pdf.py
```

### 3. Indexação
Processa todos os PDFs da pasta:
```bash
python indexer.py
```

### 4. Busca
```bash
python search.py "Sua pergunta aqui"
```
