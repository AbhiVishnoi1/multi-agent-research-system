from langchain.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
from bs4 import BeautifulSoup
from rich import print
load_dotenv()
import requests
import os

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str)->str:
    """Searcch the web for recent and reliable information  on a topic. Return the title , URL and the snippets"""
    result = tavily.search(query=query,max_results=5)

    out=[]
    for r in result['results']:
        out.append(
            f"Title:{r['title']} \nURL:{r['url']}\nSnippet:{r['content'][:300]}\r"
        )
    return "\n----\n".join(out)

def scrape_url(url:str)->str:
    """Scrape and return clean text content form a given URL for deeper reading"""
    try:
        # try and exception is becuase if ai can unable to open url then i donot want to stuck over there 
        resp=requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        soup=BeautifulSoup(resp.text,"html.parser")
        for tag in soup(["scripts","footer","style","nav"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL{str(e)}"

