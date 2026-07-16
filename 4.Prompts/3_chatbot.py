from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()  # By default, it uses gpt-3.5-turbo

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print("Chat history: ", chat_history)