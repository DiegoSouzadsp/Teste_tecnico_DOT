import sys
from chatbot import PythonChatbot

def main():
    print("=== Chatbot de Python (Langchain + OpenAI) ===")
    print("Digite 'sair', 'exit' ou 'quit' para encerrar.\n")

    try:
        # Inicializa o chatbot (pode levantar erro se sem API Key)
        bot = PythonChatbot(model_name="gpt-4o-mini", temperature=0.3)
        print(f"Modelo carregado: {bot.model_name}")
        print("-" * 40)
    except ValueError as e:
        print(f"Erro de Configuração: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado ao iniciar o chatbot: {e}")
        sys.exit(1)

    while True:
        try:
            user_input = input("Você: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["sair", "exit", "quit"]:
                print("Encerrando o chatbot. Até logo!")
                break
            
            print("Bot: Pensando...", end="\r")
            response = bot.ask(user_input)
            
            # Limpa a linha de "Pensando..." e mostra a resposta
            print(" " * 20, end="\r") 
            print(f"Bot: {response}\n")
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\nEncerrando o chatbot. Até logo!")
            break
        except Exception as e:
            print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main()
