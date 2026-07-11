import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin, urlparse

def controle_de_fila(url):
    fila = deque()
    fila.append(url)
    visitadas = set()
    dominio = urlparse(dominio).netloc
    while fila:
        url_atual = fila.popleft()
        # verifica se a url na fila na foi visitada
        if url_atual in visitadas:
            continue
        visitadas.add(url_atual)
        visita(url_atual, fila, visitadas, dominio)
    

def filtro_de_dominio(dominio, url):
    #pega somente a url encontrada
    filtro = urlparse(url).netloc
    if filtro == dominio:
        return True
    else:
        return False


# visita a url
def visita(url_atual, fila, visitadas, dominio):
    response = requests.get(url_atual)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, "html.parser")
        links = bs.find_all('a', href=True) 
        for link in links:
            #Converte links relativos para absolutos
            convert_link = urljoin(url_atual, link['href'])
            #verifica se é http ou https
            if urlparse(convert_link).scheme in ['http' , 'https']:
                if convert_link not in visitadas:
                    #filtro de dominio
                    if filtro_de_dominio(convert_link, dominio):
                        fila.append(convert_link)
    else:
        print(f"erro{response.status_code}")