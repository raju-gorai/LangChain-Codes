from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model="openai/gpt-oss-20b", temperature=0.9, max_completion_tokens=2000)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke \n {joke}',
    input_variables=['joke']
)

joke_generator_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})

print(result)