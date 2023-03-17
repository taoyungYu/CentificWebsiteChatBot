import openai
import os
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

# next step:
# add some print for important action

# config
openai.api_key_path = 'apikey.txt'
url = 'https://www.centific.com/'

# Create a directory to store the text files
if not os.path.exists("text/"):
    os.mkdir("text/")

soup = BeautifulSoup(requests.get(url).text, "html.parser")
text = soup.get_text()
with open('text/' + url[8:-1].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
    f.write(text)
