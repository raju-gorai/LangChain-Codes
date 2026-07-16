from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("Test_Doc_Resources\dl-curriculum.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    separator='',
    chunk_size=200,
    chunk_overlap=0
)

chunks = splitter.split_documents(docs)
print(chunks[5].page_content)