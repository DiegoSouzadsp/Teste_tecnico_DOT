import os
import argparse
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Carrega variáveis de ambiente
load_dotenv()

def search(query: str, k: int = 3):
    index_path = os.path.join(os.path.dirname(__file__), 'faiss_index')
    
    if not os.path.exists(index_path):
        print(f"[ERRO] Índice não encontrado em {index_path}. Execute 'indexer.py' primeiro.")
        return

    # Inicializa Embeddings (mesmo modelo usado na indexação)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # Carrega o índice do disco (allow_dangerous_deserialization=True pois confiamos no arquivo local)
    vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    
    print(f"\nBusca: '{query}'")
    print("-" * 40)
    
    # Realiza a busca por similaridade com score (distância L2, menor é melhor)
    results = vector_store.similarity_search_with_score(query, k=k)
    
    for i, (doc, score) in enumerate(results, 1):
        print(f"Resultado #{i} (Score: {score:.4f}):")
        print(f"Fonte: {doc.metadata.get('source', 'Desconhecida')}")
        print(f"Conteúdo: {doc.page_content[:300]}...") # Exibe os primeiros 300 caracteres
        print(f"Página: {doc.metadata.get('page', 'N/A')}")
        print("-" * 20)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema de Busca Semântica em Documentos (RAG)")
    parser.add_argument("query", type=str, help="A pergunta ou termo de busca")
    parser.add_argument("--k", type=int, default=3, help="Número de resultados (default: 3)")
    
    args = parser.parse_args()
    search(args.query, args.k)
