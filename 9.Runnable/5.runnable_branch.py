from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableSequence, RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model="openai/gpt-oss-20b")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic} \n Detailed report :-',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text in 100 words \n Summary :- \n{text}',
    input_variables=['text']
)

report_generator_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 1000, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generator_chain, branch_chain)

result = final_chain.invoke({'topic': 'AI'})    

print(result)
