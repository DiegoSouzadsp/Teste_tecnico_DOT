import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Carrega variáveis de ambiente do arquivo .env na pasta atual
load_dotenv()

def main():
    # Define a pasta onde estão os PDFs (pasta atual 'Questao 3')
    docs_folder = os.path.dirname(__file__)
    index_path = os.path.join(docs_folder, 'faiss_index')
    
    print(f"--- Iniciando Indexação Multi-Documento ---")
    print(f"Pasta alvo: {docs_folder}")

    all_documents = []
    
    # Itera sobre todos os arquivos na pasta
    for filename in os.listdir(docs_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(docs_folder, filename)
            print(f"1. Processando: {filename}")
            try:
                loader = PyPDFLoader(pdf_path)
                docs = loader.load()
                # Adiciona metadados da fonte para saber de qual arquivo veio
                for doc in docs:
                    doc.metadata['source'] = filename
                all_documents.extend(docs)
                print(f"   -> {len(docs)} páginas carregadas.")
            except Exception as e:
                print(f"   [ERRO] Falha ao ler {filename}: {e}")

    if not all_documents:
        print("[AVISO] Nenhum PDF encontrado para indexar.")
        return

    print(f"2. Dividindo {len(all_documents)} páginas em chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(all_documents)
    print(f"   -> {len(chunks)} chunks gerados no total.")

    print("3. Gerando Embeddings e criando Índice FAISS...")
    # Usa o modelo definido no .env ou o default text-embedding-3-small
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    vector_store = FAISS.from_documents(chunks, embeddings)

    print(f"4. Salvando índice unificado em disco: {index_path}")
    vector_store.save_local(index_path)
    print("--- Indexação Concluída com Sucesso! ---")

if __name__ == "__main__":
    main()
