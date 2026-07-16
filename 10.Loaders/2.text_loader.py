from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate 
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()

model =ChatNVIDIA(model="openai/gpt-oss-20b")
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a summary for the following text? \n {text}",
    input_variables=["text"]
)

chain = prompt | model | parser

loader = TextLoader('10.Loaders\example.txt', encoding="utf8")
docs = loader.load()

# print(docs)

print( chain.invoke({'text': docs[0].page_content}) )