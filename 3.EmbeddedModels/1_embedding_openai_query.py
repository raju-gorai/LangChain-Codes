# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

# result = embedding.embed_query("What is the capital of India?")

# print(str(result))



from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from dotenv import load_dotenv

load_dotenv()

client = NVIDIAEmbeddings(
  model="nvidia/llama-nemotron-embed-1b-v2",
  dimensions=1024
  )

embedding = client.embed_query("What is the capital of India?")
print(embedding)
