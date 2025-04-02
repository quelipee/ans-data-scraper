import os

import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url: str):
        self.url = url

    def run(self):
        # é uma biblioteca que analisa e munipulacao de html e xml
        # transforma elementos html em um objeto manipulavel

        response = requests.get(self.url)
        # pegando o texto da request, e assim utilizando o beautifulsoup para manipular os elementos
        soup = BeautifulSoup(response.text, 'html.parser')

        # correndo a lista para encontrar uma tag em html<a> e vendo se ela possui um href
        for link in soup.find_all('a', href=True):
            # verificando dentro dessa lista se existe um nome do arquivo com ('anexo I e anexo II')
            # assim pegando pegando a url e fazendo uma chamada http do item,
            # o with open, cria um arquivo com o nome do link que no caso é anexo I, e ja coloca todos
            # os dados que foi pego pela request dentro desse arquivo
            if "Anexo I." in link.text or "Anexo II." in link.text:
                pdf_url = link['href']
                pdf_response = requests.get(pdf_url)
                if os.path.exists('./code/web_scraping/' + link.text + 'pdf'):
                    print('PDF ' + link.text + ' already exists')
                else:
                    with open('./code/web_scraping/' + link.text + 'pdf', 'wb') as f:
                        f.write(pdf_response.content)
        return None
