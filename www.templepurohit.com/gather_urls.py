from requests import get
import bs4
file=open('urls.txt','a')
url = 'https://www.templepurohit.com/hindu-temples/deity/page/1'

for now_url in range(1,47):
    
    res = get(f'https://www.templepurohit.com/hindu-temples/deity/page/{now_url}')
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    # print(response.prettify())
    for i in response.findAll('a', class_='btn btn-default more_btn'):
        print(i['href'])
        file.write(i['href']+'\n')

    print()
    url = response.find('a', class_='page-numbers')['href']

