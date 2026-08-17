from langchain.tools import tool
# from requests 
# from langchain_community.tools.tavily_search import TavilySearchResults
from tavily import TavilyClient  
from dotenv import load_dotenv
import os

from rich import print

tavily =  TavilyClient(api_key= os.getenv("TAVILY_API_KEY"))


def websearch(query):
    """ search the web for recent and reliable information on a topic. Returns titles, url and content"""
    results = tavily.search(query=query, max_results=3)
    print(results)

    out = []

    for r in results['results']:
        out.append(

            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    return "\n----\n".join(out)