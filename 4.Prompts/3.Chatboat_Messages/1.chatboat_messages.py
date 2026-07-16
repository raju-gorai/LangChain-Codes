from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model="openai/gpt-oss-20b", temperature=0.9, max_completion_tokens=2000)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?")
]


result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print("AI:", result.content)

print("\nChat History:")
print(messages)
