from requests import get
import bs4
import csv    

with open('urls.txt') as file:
    urls = file.readlines()

csv_file = open('abc.csv', 'a')
csv_writer = csv.writer(csv_file)

count=0
for url in urls[223:226]:
    print(f'{count} running')
    res = get(url[:-1])
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    heading = response.find('h1', class_='entry-title').text
    matter = response.find('div', class_='entry-summary')
    for i in matter.findAll('p'):
        # print(i.text)
        luuu = i.text.replace('\t', ' ').split('\n')
        lww = []
        testing_for_missing = []
        fixed = ['Locality/village', 'State', 'Country', 'Nearest City/Town',
                'Best Season To Visit', 'Languages', 'Temple Timings', 'Photography']

        for i in luuu:
            # print(i)
            lww.append(i.split(':')[1].strip())
            testing_for_missing.append(i.split(':')[0].strip())
        got = set(testing_for_missing)
        result = set(fixed) - got
        if len(list(result)) > 0:
            lww.insert(fixed.index(list(result)[0]), '')
        # print(lww)
    
    images = []
    images.append(response.find('div', class_='page-inner').img['src'])
    try:
        image=response.find('div', class_='panel active').figure.a.img['src']
        images.append(image)
    except:
        pass

    loo = []
    for i in response.find('div', class_='panel active'):
        print(i.text)
        loo.append(i.text)
        # file.write(i.text)
        # for j in i.findAll('p'):
        # print(j.text)
    # print(len(loo))

    count+=1
    csv_writer.writerow([heading]+lww+[' '.join(loo)]+images)
    # print((lww))

csv_file.close()
