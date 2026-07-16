from langchain_community.document_loaders import TextLoader


loader = TextLoader('10.Loaders\example.txt', encoding="utf8")
docs = loader.load()

print(docs)
print(type(docs))
print(type(docs[0]))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)