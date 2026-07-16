from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India?")

print(result)



# from langchain_nvidia import ChatNVIDIA


# from langchain_nvidia_ai_endpoints import ChatNVIDIA
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatNVIDIA(model="openai/gpt-oss-20b")

# result = llm.invoke("What is the capital of India?")

# print(result)