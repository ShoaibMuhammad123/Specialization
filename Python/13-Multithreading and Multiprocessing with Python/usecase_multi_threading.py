"""
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O bound because they spend a lot of time waiting for responses from servers. 
Multithreading can significantly time waiting for responses from servers. Multithreading can 
significantly improve the performance by allowing multiple web pages to be fetched concurrently.

"""



import threading
import requests
from bs4 import BeautifulSoup

urls = ['https://docs.langchain.com/oss/python/langchain/overview?_gl=1*1mq9q5*_gcl_au*MzY2NDk5NjczLjE3NjcyMDM1MjI.*_ga*MTUzMzI3MTgxOS4xNzY3MjAzNTIz*_ga_47WX3HKKY2*czE3NjcyMDM1MjMkbzEkZzEkdDE3NjcyMDM1NzUkajgkbDAkaDA.',
       
       'https://docs.langchain.com/oss/python/langgraph/overview']

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched len {(len(soup.text))} characters from this {url}.')
    
    
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()