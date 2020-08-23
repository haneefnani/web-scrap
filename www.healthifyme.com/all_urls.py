from requests import get
import bs4
import csv
with open('./urls.txt', 'r') as file:
    l = file.readlines()

csv_file = open('abc.csv', 'a', encoding='utf-8')
csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

# url = 'https://www.healthifyme.com/blog/post-sitemap.xml'

for url in l[0:1]:
    l=[]
    res = get(url[:-1])
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    # print(response.prettify())
    heading = response.find('h1', class_='jeg_post_title').text
    inner_page = response.find('div', class_='content-inner')
    #removing unwanted tag
    try:
        for figure in inner_page('figure'):
            inner_page.figure.decompose()
        inner_page.find('p', style='text-align: center;').decompose()
        inner_page.find('div', class_='jeg_post_tags').decompose()
    except:
        pass
    for i in inner_page.contents:
        try:
            l.append(i.text+'\n')
        except:
            pass
    csv_writer.writerow([heading] + [' '.join(l)])
csv_file.close()