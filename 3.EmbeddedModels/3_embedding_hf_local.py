from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "What is the capital of India?"

# documents = [
#     "Delhi is the capital of India.",
#     "Mumbai is the financial capital of India.",
#     "Kolkata is the cultural capital of India."
# ]

vector = embedding.embed_query(text)

# vector = embedding.embed_documents(documents)


print(str(vector))
