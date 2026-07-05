import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin, urlparse

fila = deque()
def requisitar_url(url):
    fila.append(url)
    visitadas = set()
    while fila:
        url_atual = fila.popleft()
        #verifica se a url na fila na foi visitada
        if url_atual in visitadas:
            continue
        visitadas.add(url_atual)
        #visita a url
        response = requests.get(url_atual)
        if response.status_code == 200:
            bs = BeautifulSoup(response.text, "html.parser")
            links = bs.find_all('a', href=True) 
            for link in links:
                #Converte links relativos para absolutos
                convert_link = urljoin(url_atual, link['href'])
                if urlparse(convert_link).scheme in ['http' , 'https']:
                    if convert_link not in visitadas:
                        fila.append(convert_link)
                        print(fila)
          