import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class PythonChatbot:
    """
    Chatbot especializado em programação Python usando Langchain e OpenAI.
    """
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.2):
        """
        Inicializa o chatbot.
        
        Args:
            model_name (str): Nome do modelo da OpenAI a ser usado.
            temperature (float): Temperatura para controle de criatividade (0.0 a 1.0).
        
        Raises:
            ValueError: Se a chave de API da OpenAI não estiver configurada.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("A variável de ambiente OPENAI_API_KEY não está configurada. Verifique seu arquivo .env.")

        self.model_name = model_name
        self.temperature = temperature
        
        # Configuração do Modelo
        self.llm = ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            api_key=self.api_key
        )
        
        # Configuração do Prompt
        self.prompt = PromptTemplate(
            input_variables=["question"],
            template="""
            Você é um assistente especialista em programação Python sênior.
            Sua tarefa é responder a perguntas sobre Python de forma clara, técnica e didática.
            Forneça exemplos de código sempre que possível.
            
            Pergunta: {question}
            
            Resposta:
            """
        )
        
        # Configuração da Chain (Cadeia)
        self.chain = self.prompt | self.llm | StrOutputParser()

    def ask(self, question: str) -> str:
        """
        Envia uma pergunta ao chatbot e retorna a resposta.
        
        Args:
            question (str): A pergunta do usuário.
            
        Returns:
            str: A resposta do chatbot.
        """
        try:
            response = self.chain.invoke({"question": question})
            return response
        except Exception as e:
            return f"Erro ao processar sua pergunta: {str(e)}. Verifique sua conexão ou chave de API."
