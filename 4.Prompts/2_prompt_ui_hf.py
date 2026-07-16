from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
# from langchain_core.load import loads
# from pathlib import Path
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

llm_obj=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",  
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm_obj)
# result = model.invoke("What is the animal of India?")   
# print(result.content)

st.header("Summarizer Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)


# Template
# template = loads(Path("template.json").read_text(encoding="utf-8"))
template = load_prompt('template.json')


prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})


if st.button("Summarize"):
    st.text("Generating summary...")
    
    result = model.invoke(prompt)
    st.text("Summary:")
    st.write(result.content)
