from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options
import pickle
import time
import bs4
import csv

file = open('bla.csv', 'a', encoding='utf-8')
csv_writer = csv.writer(file)


def save_cookie():
    pickle.dump(driver.get_cookies(), open(r"glassdoor_cookies.pkl", "wb"))


def load_cookie():
    cookies = pickle.load(open(r"glassdoor_cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)


# url='https://www.glassdoor.co.in/Job/india-jobs-SRCH_IL.0,5_IN115.htm'
# url='https://www.glassdoor.co.in/Interview/hyderabad-software-engineer-interview-questions-SRCH_IL.0,9_IM1076_KO10,27_IP9.htm'
url = 'https://www.glassdoor.co.in/Interview/hyderabad-software-engineer-interview-questions-SRCH_IL.0,9_IM1076_KO10,27.htm'
driver = webdriver.Chrome(
    executable_path=r'C:\Users\haneef\PycharmProjects\nani\venv\code\chromedriver_win32\browers\chromedriver.exe')
driver.get(url)
load_cookie()
driver.refresh()
# input('Have u finished')
# save_cookie()
# time.sleep(2)
# driver.quit()
to_next_page = 0
for _ in range(750):
    response = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    print(f'{to_next_page+1}th page')

    a = 0
    for i in response.findAll('div', class_='interviewQuestionWrapper padVertLg'):

        l, l2 = [], []
        try:
            # print('\n Heading : ',i.find('p',class_='questionText h3').text+'\n')
            l.append(i.find('p', class_='questionText h3').text.strip())
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
            #for first answer
            for j in i.findAll('p', class_='cell noMargVert padTop tightBot'):
                # print(a+1,j.text)
                l2.append(j.text.strip())
                # a+=1
        except:
            pass
        csv_writer.writerow(l+l2)
    to_next_page += 1
    time.sleep(2)
    print('going to next page......')
    # driver.get('http://glassdoor.co.in'+response.find('li',class_='next').a['href'])
    try:
        driver.find_element_by_xpath(
            '//*[@id="FooterPageNav"]/div/ul/li[7]/a').click()
    except:
        print('\n\nStopped------------------------------------------------------------------->')
    time.sleep(2)
file.close()
