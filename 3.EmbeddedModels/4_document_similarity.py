# from langchain_openai import OpenAIEmbeddings
# from sklearn.metrics.pairwise import cosine_similarity
# # import numpy as np
# from dotenv import load_dotenv

# load_dotenv()

# embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300 )
# documents = [
#     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
#     "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
#     "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
#     "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
#     "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
# ]

# quiry = 'tell me about virat kohli'

# doc_embeddings = embedding.embed_documents(documents)
# query_embedding = embedding.embed_query(quiry)

# similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

# # print(sorted(list(enumerate(similarities)), key=lambda x:x[1])[-1])

# index, score = sorted(list(enumerate(similarities)), key=lambda x:x[1])[-1]
# print(quiry)
# print(documents[index])
# print("similarity score: ", score)



# from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
# from sklearn.metrics.pairwise import cosine_similarity
# from dotenv import load_dotenv

# load_dotenv()

# client = NVIDIAEmbeddings(
#     model="nvidia/llama-nemotron-embed-1b-v2",
#     dimensions=1024
# )

# documents = [
#     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
#     "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",       
#     "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
#     "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",  
#     "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
# ]

# quiry = 'Tell me about virat kohli'

# doc_embeddings = client.embed_documents(documents)
# query_embedding = client.embed_query(quiry)
# similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
# index, score = sorted(list(enumerate(similarities)), key=lambda x:x[1])[-1]
# print(quiry)
# print(documents[index])
# print("similarity score: ", score)






from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv

load_dotenv()

embedding_model = NVIDIAEmbeddings(
    model="nvidia/llama-nemotron-embed-1b-v2",
    dimensions=1024
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me about Virat Kohli"

document_embeddings = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)

# Compares the question embedding with every document embedding. 
# [query_embedding] is used because cosine_similarity expects a list of vectors. [0] gets the first row of results.
similarity_scores = cosine_similarity([query_embedding], document_embeddings)[0]

best_index, best_score = max(enumerate(similarity_scores),  key=lambda item: item[1] )     #key=lambda item: item[1] tells Python to compare using the score, not the index.


print("Question:", query)
print("Best match:", documents[best_index])
print("Similarity score:", best_score)