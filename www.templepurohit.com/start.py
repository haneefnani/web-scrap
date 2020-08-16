from requests import get
import bs4
import csv
csv_file=open('abc.csv','a',encoding='utf-8')
csv_writer=csv.writer(csv_file,quoting=csv.QUOTE_ALL)

with open('urls.txt') as file:
    urls = file.readlines()
# print(len(urls))
count=0


def join_the_times():
    for_removal=[]
    for i in word_copy:
        if (i.startswith('Temple Timings')):
            place=word.index(i)
            tttt =' '.join(word[word.index(i) : word.index(word_copy[-1])])
            for u in range(word.index(i),word.index(word_copy[-1])):
                for_removal.append(word[u])                                                                                       
            for i in for_removal:
                word_copy.remove(i)
            word_copy.insert(place,tttt)
#----------------------------------------------------------------------------------------
    
   # for_removal=[]
   # for i in word_copy:
   #     if (i.endswith('Morning')):
   #         # print(i)
   #             # Temple Timings : Morning
   #         place=word.index(i)
   #         tttt =' '.join(word[word.index(i) : word.index(i)+3])
   #         for u in range(word.index(i),word.index(i)+3):
   #             # print(word[u])
   #             for_removal.append(word[u])
   #             for i in for_removal:
   #                 word_copy.remove(i)
   #         word_copy.insert(place,tttt)

for url in urls:
    res = get(url[:-1])
    response = bs4.BeautifulSoup(res.text, 'html.parser')
    # print(response.prettify())
    
    lppp=[]
    heading=response.find('h1', class_='entry-title').text
    # matter=response.find('div',class_='entry-summary')
    # with open('bla.txt','w') as fi:
    # for i in matter.findAll('p'):
    #     print(i.text,'\n')
    #     lppp.append(i.text)
    # joined_word=' '.join(lppp)
    # word=joined_word.replace('\t',' ').split('\n')
    # word_copy=word
    # print(word)
#----------------------------------------------------------------------------------------
    matter=response.find('div',class_='entry-summary')
    for i in matter.findAll('p'):
        # print(i.text)
        # luuu=i.text.replace('\t',' ').split('\n')
        lppp.append(i.text)
    joined_word=' '.join(lppp)
    word=joined_word.replace('\t',' ').split('\n')
    word_copy=word
    # print(word)
    lww=[]
    testing_for_missing=[]
    fixed=['Locality/village','District','State','Country', 'Nearest City/Town',  'Best Season To Visit','Languages','Temple Timings', 'Photography']

#-----------------------------------------------------------------------------------------------------------------------


    # for_removal=[]
    # for i in word_copy:
    #     if (i.endswith('Morning')):
    #         print(i)
    #             # Temple Timings : Morning
    #         place=word.index(i)
    #         tttt =' '.join(word[word.index(i) : word.index(i)+3])
    #         for u in range(word.index(i),word.index(i)+3):
    #             # print(word[u])
    #             for_removal.append(word[u])
    #         for i in for_removal:
    #             word_copy.remove(i)
    #         word_copy.insert(place,tttt)


#-----------------------------------------------------------------------------------------------------------------------
    for i in word_copy:
        # print(i)    
        try:
            lww.append(i.split(' :')[1].strip())
            testing_for_missing.append(i.split(' :')[0].strip())
            join_the_times()
        except IndexError:
            lww.append(i.split(':')[1].strip())
            testing_for_missing.append(i.split(':')[0].strip())
            join_the_times()
        except:
            pass
    got=set(testing_for_missing)
    test_result=list(set(fixed)-got)
    result=[]
    # print(test_result)
    for i in fixed:
        if i in test_result:
            result.append(i)

    # print('result',result)
    # print('fixed',fixed)

    if len(result) > 0:
        for i in list(result):
            lww.insert(fixed.index(i),'')

    # print(lww)
    print(count,'length is',len(lww))
    loo=[]
    for i in response.find('div',class_='panel active'):
    #   print(i.text)
        loo.append(i.text)
    # file.write(i.text)
    for j in i.findAll('p'):
        loo.append(j.text)
    
    count+=1
# print(len(loo))
# 
# 
    csv_writer.writerow([heading]+lww+[' '.join(loo)])
# print((lww))
# print([heading]+lww+[' '.join(loo)])
csv_file.close()
