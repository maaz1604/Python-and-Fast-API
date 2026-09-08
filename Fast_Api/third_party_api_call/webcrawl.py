# Pyhton framework example that how to do web Crawling

# import requests
# from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url=url)

# soup = BeautifulSoup(response.text,"html.parse")

# print(soup.title.text)

#FastApi example of webcrawlong
from fastapi import FastAPI,HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get('/news')
def get_news():
    url='https://indianexpress.com'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text,'html.parser')
    title = []
    for item in soup.find_all("a",class_="article-click topblockNews__sidebarLink"):
        title.append(item.text)
        
    return{
        'news':title[:5]
    }