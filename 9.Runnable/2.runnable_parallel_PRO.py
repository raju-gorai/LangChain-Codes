from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',  
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

model = ChatNVIDIA(model="openai/gpt-oss-20b")

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin_post": RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic': 'AI'})

print(result['tweet'])
print(result['linkedin_post'])