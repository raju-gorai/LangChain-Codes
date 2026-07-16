from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model="openai/gpt-oss-20b", temperature=0.9, max_completion_tokens=2000)

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        print("Exiting chat...")
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)


print("\nChat History:")
print(chat_history)