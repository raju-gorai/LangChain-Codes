# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableConditional, RunnableBranch, RunnableLambda
# from langchain_core.output_parsers import PydanticOutputParser
# from pydantic import BaseModel, Field
# from typing import Literal

# load_dotenv()

# model = ChatOpenAI()

# parser = StrOutputParser()

# class Sentiment(BaseModel):
#     sentiment: Literal['positive', 'negative'] = Field(..., description="Classify the sentiment of the review as either positive or negative")

# parser2 = PydanticOutputParser(pydantic_object=Sentiment)

# prompt1 = PromptTemplate(
#     template = 'Classify the sentiment of the following review as either positive or negative \n {review} \n {format_instructions}',
#     input_variables=['review'],
#     partial_variables={'format_instructions': parser2.get_format_instructions()}
# )

# classifier_chain = prompt1 | model | parser2

# # result = classifier_chain.invoke({'review': 'The movie was fantastic!'}).sentiment

# # print(result)


# prompt2 = PromptTemplate(
#     template = 'Write an appropriate response to the following review \n {review}',
#     input_variables=['review']
# )

# prompt3 = PromptTemplate(
#     template = 'Write an appropriate response to the following review \n {review}',
#     input_variables=['review']
# )

# branch_chain = RunnableBranch(
#     (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
#     (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
#     RunnableLambda(lambda x: "Invalid sentiment")
# )

# chain = classifier_chain | branch_chain

# print(chain.invoke({'review': 'The movie was fantastic!'}))

# # chain.get_graph().print_ascii()


























