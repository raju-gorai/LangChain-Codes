from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv  
load_dotenv()

llm_obj=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm_obj)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input=='exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print("Chat history: ", chat_history)