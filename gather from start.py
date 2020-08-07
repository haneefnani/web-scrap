import csv
from requests import get
import bs4

with open('./totalurls-Without Q and question.txt') as file:
    urls=file.readlines()

urlss = urls

file = open('abc.csv', 'w', encoding="utf-8")
csv_writer = csv.writer(file)
count=0
for url in urlss:
    print(f'{count+1}th running')
    res = get(url[:-1])
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    lo,images = [],[]
    # with open('telugu.txt', 'a+', encoding="utf-8") as fi:
    heading=(response.find('h3', class_='post-title entry-title').text.replace('\n',''))
        # fi.write(str(titlee))
        # with open('text/'+titlee.strip('\n').replace('|', '').replace('?', '')+'.txt', 'w', encoding="utf-8") as fil:
    z = response.find(
        'div', class_='post-body entry-content float-container')
    # print(z.findAll('sapn'))
    for j in z.findAll('span'):
        if '(adsbygoogle = window.adsbygoogle || []).push({});' not in j.text:
            if '.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }' not in j.text:
                lo.append((j.text))
    for i in response.findAll('img'):
                images.append(i['src'])
                # print(i['src'])
    print('No of images are',len(images))
    to_csv = " ".join(lo).strip()
    # print((to_csv))
    csv_writer.writerow([heading,to_csv]+images)
    count+=1