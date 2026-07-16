from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model =ChatNVIDIA(model="openai/gpt-oss-20b")
parser = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field( description="Classify the sentiment of the review as either positive or negative")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='classify the sentiment of the following review as either positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = 'Write an appropriate response to the following review in 30 words: \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to the following review in 30 words and ask to contact us at support@aitool.com \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Invalid sentiment")
)

chain = classifier_chain | branch_chain

# result = chain.invoke({'feedback': 'The movie was fantastic!'})
result = chain.invoke({'feedback': 'The movie was very bad. I hated it.'})

print(result)