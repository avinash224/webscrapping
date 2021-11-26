# pip install requests
# pip install bs4
# pip install lxml

import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Harry_Potter_and_the_Sorcerers_Stone-241527'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify()) - getting the html code from the page
box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()
print(f'TITLE OF THE WEB SCRAPPED FILM IS:\n {title}')

script = box.find('div', class_='full-script').get_text(separator=' ', strip=True)
print(f'FULL SCRIPT OF THE WEB SCRAPPED FILM IS:\n {script}')

with open('harry_potter.txt', 'w') as file:
    file.write(script)

print(len(script))
