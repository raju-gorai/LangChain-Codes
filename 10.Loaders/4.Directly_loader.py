from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books', 
    glob="*.pdf", 
    show_progress=True, 
    loader_cls=PyPDFLoader
)
docs = loader.load()
# docs = loader.lazy_load()

# for doc in docs:
#     # print(doc.page_content)
#     print(doc.metadata)

# print(len(docs))
# print(docs)

print(docs[66].page_content)
print(docs[66].metadata)