from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import pickle
import time
import bs4
import csv
import datetime


def save_cookie():
    pickle.dump(driver.get_cookies(), open(r"glassdoor_cookies.pkl", "wb"))


def load_cookie():
    cookies = pickle.load(open(r"glassdoor_cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)


# url='https://www.glassdoor.co.in/Job/india-jobs-SRCH_IL.0,5_IN115.htm'
# url='https://www.glassdoor.co.in/Interview/hyderabad-software-engineer-interview-questions-SRCH_IL.0,9_IM1076_KO10,27_IP9.htm'
url = 'https://www.glassdoor.co.in/Interview/hyderabad-software-engineer-interview-questions-SRCH_IL.0,9_IM1076_KO10,27.htm'
driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\Desktop\App nana updated\web driver\chromedriver.exe')
driver.get(url)
load_cookie()
driver.refresh()
# input('Have u finished')
# save_cookie()
# time.sleep(2)
# driver.quit()

urls = ['https://www.glassdoor.co.in/Interview/hyderabad-analyst-interview-questions-SRCH_IL.0,9_IM1076_KO10,17.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-associate-interview-questions-SRCH_IL.0,9_IM1076_KO10,19.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-business-analyst-interview-questions-SRCH_IL.0,9_IM1076_KO10,26.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-data-analyst-interview-questions-SRCH_IL.0,9_IM1076_KO10,22.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-data-scientist-interview-questions-SRCH_IL.0,9_IM1076_KO10,24.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-financial-analyst-interview-questions-SRCH_IL.0,9_IM1076_KO10,27.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-intern-interview-questions-SRCH_IL.0,9_IM1076_KO10,16.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-research-analyst-interview-questions-SRCH_IL.0,9_IM1076_KO10,26.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-senior-analyst-interview-questions-SRCH_IL.0,9_IM1076_KO10,24.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-senior-software-engineer-interview-questions-SRCH_IL.0,9_IM1076_KO10,34.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-software-development-engineer-interview-questions-SRCH_IL.0,9_IM1076_KO10,39.htm',
        'https://www.glassdoor.co.in/Interview/hyderabad-software-engineer-interview-questions-SRCH_IL.0,9_IM1076_KO10,27.htm']

file2 = open('total_pages.txt', 'r')
loo = file2.readlines()
file2.close()
with open('present.txt') as file:
    m, n = [int(i) for i in file.readline().split()]
        

print(f'\n[{m} : {n}]\n')
for i, url in enumerate(loo[m:n],m):  # -12  # 0-index
    this_url = url[:-1]
    if this_url not in urls:
        try:
            print(f'\n{i}th URL\n')
            print(datetime.datetime.now())
            print()
            driver.get(this_url)
            response = bs4.BeautifulSoup(driver.page_source, 'html.parser')
            file_name = response.find('h1', class_='noMarg').text+'.csv'
            print(file_name)
            file = open('./csv/glassdoor/'+file_name, 'w', encoding='utf-8')
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Question', 'Answers-->'])
            number_in_page = int(response.find(
                'div', class_='reviewCount cell span-1-2 drop').text.replace(',', ''))
            if (number_in_page // 10) in [0, 1]:
                no_of_pages = number_in_page // 10 + 1
            else:
                no_of_pages = number_in_page // 10 + 1 + 4
            current_page = 1
            for num in range(no_of_pages):

                response = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                print(f'{current_page}th page')
                a = 0
                for i in response.findAll('div', class_='interviewQuestionWrapper padVertLg'):

                    l, l2 = [], []
                    try:
                        # print('\n Heading : ',i.find('p',class_='questionText h3').text+'\n')
                        l.append(
                            i.find('p', class_='questionText h3').text.strip())
                    except:
                        pass
                    try:
                        # for remaining answers
                        for j in i.findAll('p', class_='cell noMargVert padVert borderBot'):
                            # print(a+1,j.text)
                            l2.append(j.text.strip())
                    except:
                        pass
                    try:
                        # for first answer
                        for j in i.findAll('p', class_='cell noMargVert padTop tightBot'):
                            # print(a+1,j.text)
                            l2.append(j.text.strip())
                            # a+=1
                    except:
                        pass
                    csv_writer.writerow(l+l2)
                current_page += 1

                print('going to next page......')
                # driver.get('http://glassdoor.co.in'+response.find('li',class_='next').a['href'])
                if current_page != no_of_pages+1:
                    try:
                        driver.get(this_url[:-4] + '_IP' +
                                   str(num) + this_url[-4:])
                    except:
                        print(
                            '\n\nStopped------------------------------------------------------------------->')
                else:
                    print('-------------------last page--------------------------')
            file.close()
        except Exception as e:
            print(e)
driver.close()
m, n = m+2, n+2
with open('present.txt', 'w') as file:
    file.write(f'{m} {n}')
