from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/")

# url = 'https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/'
# loader = WebBaseLoader(url)
docs = loader.load()

# print(docs)
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)