from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm_obj=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm_obj)

result = model.invoke("What is the animal of India?")

print(result.content)