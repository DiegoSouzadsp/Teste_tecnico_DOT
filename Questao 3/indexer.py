import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Carrega variáveis de ambiente (.env da raiz ou da pasta atual)
# Tenta carregar da pasta Questao 2 onde já criamos, ou da raiz se existisse
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'Questao 2', '.env'))

def main():
    pdf_path = os.path.join(os.path.dirname(__file__), '..', 'Prova - Backend IA.pdf')
    index_path = os.path.join(os.path.dirname(__file__), 'faiss_index')

    if not os.path.exists(pdf_path):
        print(f"[ERRO] Arquivo PDF não encontrado em: {pdf_path}")
        return

    print(f"--- Iniciando Indexação ---")
    print(f"1. Carregando PDF: {pdf_path}")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(f"   -> {len(documents)} páginas carregadas.")

    print("2. Dividindo texto em chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"   -> {len(chunks)} chunks gerados.")

    print("3. Gerando Embeddings e criando Índice FAISS...")
    # Usa o modelo definido no .env ou o default text-embedding-3-small (mais barato e eficiente)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    vector_store = FAISS.from_documents(chunks, embeddings)

    print(f"4. Salvando índice em disco: {index_path}")
    vector_store.save_local(index_path)
    print("--- Indexação Concluída com Sucesso! ---")

if __name__ == "__main__":
    main()
