# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

# documents = [
#     "Delhi is the capital of India.",
#     "Mumbai is the financial capital of India.",
#     "Kolkata is the cultural capital of India."
# ]

# result = embedding.embed_documents(documents)
# print(str(result))



from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from dotenv import load_dotenv
load_dotenv()

client = NVIDIAEmbeddings(
    model="nvidia/llama-nemotron-embed-1b-v2",    
    dimensions=1024
)

documents = [
    "Delhi is the capital of India.",   
    "Mumbai is the financial capital of India.",
    "Kolkata is the cultural capital of India."
]

embedding = client.embed_documents(documents)
print(embedding)