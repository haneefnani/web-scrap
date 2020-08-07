from requests import get
import bs4

with open('urls.txt') as file:
    urls = file.readlines()
# print(len(urls))

for url in urls[:1]:
    res = get(url[:-1])
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    # print(response.prettify())
    print(response.find('h1', class_='entry-title'))
