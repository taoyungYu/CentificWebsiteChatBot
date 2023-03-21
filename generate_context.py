import os

import requests
import tiktoken
from bs4 import BeautifulSoup

# Create a directory to store the text files
if not os.path.exists("raw/"):
    os.mkdir("raw/")
if not os.path.exists("text/"):
    os.mkdir("text/")

for filename in os.listdir('link'):
    domain = filename[:-4]
    with open('link/' + filename, 'r') as f:
        if not os.path.exists(f'raw/{domain}'):
            os.mkdir(f'raw/{domain}')
        if not os.path.exists(f'text/{domain}'):
            os.mkdir(f'text/{domain}')
        
        for line in f:
            url = line[:-1]
            # get text from website
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            text = soup.get_text()
            with open(f'raw/{domain}/' + url[8:].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
                f.write(text)

            # clean up the text
            text = text.replace('\n', ' ')
            while '  ' in text:
                text = text.replace('  ', ' ')
            with open(f'text/{domain}/' + url[8:].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
                f.write(text)



