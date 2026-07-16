from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

maessages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about Lanfchain."),
]

result = model.invoke(maessages)

maessages.append(AIMessage(content=result.content))

print(maessages)