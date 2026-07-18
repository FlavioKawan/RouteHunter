import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin, urlparse

def queue_control(url):
    queue = deque()
    queue.append(url)
    visited_urls = set()
    domain = urlparse(url).netloc
    while queue:
        current_url = queue.popleft()
        # verifica se a url na fila na foi visitada
        if current_url in visited_urls:
            continue
        visited_urls.add(current_url)
        print(current_url)
        visit_url(current_url)
        extract_links(visited_urls)
    

def domain_filter(url, domain):
    #pega somente a url encontrada
    filter = urlparse(url).netloc
    if filter == domain:
        return True
    else:
        return False


# visita a url
def visit_url(current_url):
    response = requests.get(current_url)
    if response.status_code == 200:
        return response.text
    return None


def extract_links(html, current_url):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a', href=True) 
    for link in links:
        absolute_url = urljoin(current_url, link['href'])
        #verifica se é http ou https
        if urlparse(absolute_url).scheme in ['http' , 'https']:

            
        #
        #    if absolute_url not in visited_urls and absolute_url not in queue:
        #        if domain_filter(absolute_url, domain):
        #           queue.append(absolute_url)
    