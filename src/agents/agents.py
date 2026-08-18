from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

from tools import websearch , scrape_url 


load_dotenv()


llm = ChatGroq(model = "openai/gpt-oss-20b", temperature= 0 )


# agent 1

def  build_search_agent():
    return create_agent(model =llm, tools = [websearch])


# agent 2 

def build_reader_agent():
    return create_agent(model = llm, tools = [scrape_url])

