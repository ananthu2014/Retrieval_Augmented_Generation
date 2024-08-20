import langchain_community
import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
import sys
sys.path.append('/media/user/data/ananthakrishnan/e-commerceSearchAI')

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"] = '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'

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('Langchain Demo With GEMME2 API')
input_text=st.text_input("Search the topic u want")

# ollama GEMMA2 LLM
llm = Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
