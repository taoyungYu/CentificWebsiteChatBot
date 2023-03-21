import os
import requests
from bs4 import BeautifulSoup
import tiktoken

# config
url = 'https://www.centific.com/'

# Create a directory to store the text files
if not os.path.exists("raw/"):
    os.mkdir("raw/")
if not os.path.exists("text/"):
    os.mkdir("text/")

# get text from website
soup = BeautifulSoup(requests.get(url).text, "html.parser")
text = soup.get_text()
with open('raw/' + url[8:-1].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
    f.write(text)

# clean up the text
text = text.replace('\n', ' ')
while '  ' in text:
    text = text.replace('  ', ' ')
with open('text/' + url[8:-1].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
    f.write(text)

# calculate token
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
num_tokens = len(encoding.encode(text))
print(num_tokens)
