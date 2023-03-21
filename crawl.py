import requests
from bs4 import BeautifulSoup
import os

domain = 'https://www.centific.com'

links_visited = set()
links_html = set()

def crawl(url):
    response = requests.get(url)
    content_type = response.headers.get('Content-Type')

    links_visited.add(url)
    if not content_type.startswith('text/html'):
        return
    links_html.add(url)
    with open(f'link/{domain[8:]}.txt', 'a') as f:
        f.write(url+'\n')
        print(url)


    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        href = a_tag.get('href')

        if href == None:
            continue
        if href.startswith('#') or href.startswith('mailto:'):
            continue

        # case for '/'
        if href.startswith('/'):
            href = domain + href

        if domain not in href:
            continue

        # remove '/' at the end
        if href.endswith('/'):
            href = href[:-1]

        if href in links_visited:
            continue

        crawl(href)



if not os.path.exists("link/"):
    os.mkdir("link/")
with open(f'link/{domain[8:]}.txt', 'w') as f:
        f.write('')
crawl(domain)