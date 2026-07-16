# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PrompteTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# prompt1 = PrompteTemplate(
#     template = 'Generate a detailed report on {topic}',
#     input_variables=['topic']
# )

# prompt2 = PrompteTemplate(
#     template = 'Generate a 5 pointers summary from the following text \n {text}',
#     input_variables=['text']
# )

# model = ChatOpenAI()

# parser = StrOutputParser()

# chain = prompt1 | model | parser | prompt2 | model | parser

# result = chain.invoke({'topic': 'space exploration'})   

# print(result)

# chain.get_graph().print_ascii()



























from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on {topic}', 
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a 5 pointers summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatNVIDIA(model="openai/gpt-oss-20b", temperature=0.9, max_completion_tokens=2000)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Gen AI'})

print(result)