# # from langchain_openai import ChatOpenAI
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import promtTemplate
# from langchain_core.output_parsers import strOutputParser

# load_dotenv()

# prompt = PrompteTemplate(
#     template='Generate 5 interesting facts about {topic}',
#     input_variables=['topic']
# )

# # model = ChatOpenAI()
# llm_obj=HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct", 
#     task="text-generation"
#     )

# model = ChatHuggingFace(llm=llm_obj)

# parser = StrOutputParser()

# chain = prompt | model | parser

# result = chain.invoke({'topic': 'space exploration'})

# print(result)

# chain.get_graph().print_ascii()



























from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model =ChatNVIDIA(model="openai/gpt-oss-20b")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'space exploration'})
print(result)

# print(chain.get_graph().print_ascii())