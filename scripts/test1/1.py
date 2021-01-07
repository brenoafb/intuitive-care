# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     comment_magics: true
#     split_at_heading: true
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3.8.2 64-bit
#     metadata:
#       interpreter:
#         hash: 20bf69066c0dd38d51965b69d5e1b6e387082e3198ba56e97997ac55f4e50ad0
#     name: python3
# ---

import re
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.ans.gov.br'
page_url = base_url + '/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

header = next(x for x in soup.find_all('h2') if x.string.startswith('Padrão TISS – Versão'))

print('Found: {}'.format(header.string))

a_tag = header.findNext('a')

suffix = a_tag.get('href')
suffix

link = '{}{}'.format(base_url, suffix)
link

page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

class_name = 'table-responsive'
divs = soup.findAll("div", {"class": class_name})
divs

a_tag = divs[0].findNext('a')
suffix = a_tag.get('href')
suffix

link = base_url + '/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padrao_TISS_Componente_Organizacional__202012.pdf'
link


# +
# https://stackoverflow.com/a/16696317

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

download_file(link)
