# from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv  
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

llm_obj=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm_obj)

# model =  ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

#schema for the output
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list."]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["-ve", "+ve"], "The sentiment of the review either negative or positive. Write -ve for negative sentiment and +ve for positive sentiment."]
    pros: Optional[Annotated[list[str], "List down the pros mentioned in the review. If not mentioned, write None"]]  
    cons: Optional[Annotated[list[str], "List down the cons mentioned in the review. If not mentioned, write None"]]  
    Seller_name: Optional[Annotated[str, "List down the seller name mentioned in the review. If not mentioned, write None"]]
    Warranty: Optional[Annotated[str, "List down the warranty information mentioned in the review. If not mentioned, write None"]]
    Model_name: Optional[Annotated[str, "List down the Model name mentioned in the review. If not mentioned, write None"]]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors""")

print(result)

# print(result['summary'])
# print(result['sentiment'])