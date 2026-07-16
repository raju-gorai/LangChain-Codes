from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
load_dotenv()

model =ChatNVIDIA(model="openai/gpt-oss-20b")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Answare the following question \n {question} based on the provided text: \n {text}",
    input_variables=["question","text"]
)

chain = prompt | model | parser

loader = WebBaseLoader("https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/")
docs = loader.load()

question = "What is generative AI?"

print( chain.invoke({'question': question, 'text': docs[0].page_content}) )