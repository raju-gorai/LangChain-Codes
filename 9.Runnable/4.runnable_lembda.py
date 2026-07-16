# from langchain_core.runnables import RunnableLambda

# def word_count(text):
#     return len(text.split())

# runnable_word_counter = RunnableLambda(word_count)

# print(runnable_word_counter.invoke("Hello world! This is a test."))


from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model="openai/gpt-oss-20b")

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Tell me a joke about {topic} only joak without any explanation inten words',
    input_variables=['topic']
)

joke_generator_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

result = final_chain.invoke({'topic': 'Elephent'})

final_result = """{} \n The joke has {} words""".format(result['joke'], result['word_count'])
print(final_result)
