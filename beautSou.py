import requests
from bs4 import BeautifulSoup

# function to extract information from the website
def extract():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://uk.indeed.com/jobs?q=machine+learning+engineer&l=United+Kingdom'
    r = requests.get(url, headers)
    return r.status_code

print(extract())