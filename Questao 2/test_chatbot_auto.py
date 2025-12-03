from chatbot import PythonChatbot
import sys

def test_bot():
    print("Iniciando teste automatizado do Chatbot...")
    try:
        bot = PythonChatbot()
        question = "Quanto é 2 + 2 em Python?"
        print(f"Pergunta: {question}")
        response = bot.ask(question)
        print(f"Resposta: {response}")
        
        if "4" in response:
            print("Teste SUCESSO: Resposta contém o resultado esperado.")
        else:
            print("Teste ALERTA: Resposta pode não estar correta, verifique a saída.")
            
    except Exception as e:
        print(f"Teste FALHOU: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_bot()
