from requests import get
import bs4
import csv
csv_file=open('abc.csv','a')
csv_writer=csv.writer(csv_file,quoting=csv.QUOTE_ALL)

with open('urls.txt') as file:
    urls = file.readlines()
# print(len(urls))

for url in urls:
    res = get(url[:-1])
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    # print(response.prettify())
    
    lppp=[]
    heading=response.find('h1', class_='entry-title').text
    matter=response.find('div',class_='entry-summary')
    # with open('bla.txt','w') as fi:
    for i in matter.findAll('p'):
        # print(i.text,'\n')
        lppp.append(i.text)
    joined_word=' '.join(lppp)
    word=joined_word.replace('\t',' ').split('\n')
    word_copy=word
    # print(word_copy)
    for_removal=[]
    for i in word:
        if (i.endswith('Morning')):
            place=word.index('Temple Timings : Morning')
            tttt =' '.join(word[word.index('Temple Timings : Morning') : word.index('Temple Timings : Morning')+3])
            for u in range(word.index('Temple Timings : Morning'),word.index('Temple Timings : Morning')+3):
                # print(word[u])
                for_removal.append(word[u])
            for i in for_removal:
                word_copy.remove(i)
            word_copy.insert(place,tttt)


    lww=[]
    for i in word_copy:
        lww.append(i.split(':')[1].strip())
    print(lww)
    loo=[]
    for i in response.find('div',class_='panel active'):
    #   print(i.text)
        loo.append(i.text)
    # file.write(i.text)
    for j in i.findAll('p'):
        loo.append(j.text)
# print(len(loo))
# 
# 
    csv_writer.writerow([heading]+lww+[' '.join(loo)])
# print((lww))
# print([heading]+lww+[' '.join(loo)])
csv_file.close()
