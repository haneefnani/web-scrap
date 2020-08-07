from requests import get
import bs4
import csv    

with open('urls.txt') as file:
    urls = file.readlines()

csv_file = open('abc.csv', 'a')
csv_writer = csv.writer(csv_file)


for url in urls[:1]:
    res = get(url[:-1])
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    heading = response.find('h1', class_='entry-title').text
    matter = response.find('div', class_='entry-summary')
    # with open('bla.txt','w') as fi:
    for i in matter.findAll('p'):
        print(i.text)
        luuu = i.text.replace('\t', ' ').split('\n')
        lww = []
        for i in luuu:
            # print(i)
            lww.append(i.split(':')[1].strip())

    loo = []
    for i in response.find('div', class_='panel active'):
        print(i.text)
        loo.append(i.text)
        # file.write(i.text)
        # for j in i.findAll('p'):
        # print(j.text)
    # print(len(loo))


    csv_writer.writerow([heading]+lww+[' '.join(loo)])
    # print((lww))
    
csv_file.close()
