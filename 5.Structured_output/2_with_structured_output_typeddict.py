# from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv  
from typing import TypedDict

load_dotenv()

llm_obj=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm_obj)

# model =  ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

#schema for the output
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

# print(result)
print(result['summary'])
print(result['sentiment'])