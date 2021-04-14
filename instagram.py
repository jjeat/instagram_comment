from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import sys

tryagain = 1
num = 0
comment_list = []
id_list = []
end_list = []

user = ""
pw = ""

pwd='/Users/doker/instagram/chromedriver'

webdriver = webdriver.Chrome(pwd)
time.sleep(3)
log = 'https://www.instagram.com/'

url = ''

webdriver.get(log)

id_input = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
id_input.send_keys(user)
time.sleep(60)

pw_input = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
pw_input.send_keys(pw)
time.sleep(3)

webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

webdriver.get(url)

time.sleep(90)

#while tryagain < 6:
#     time.sleep(15)
#     webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span').click()
#     time.sleep(30)
#     tryagain = tryagain + 1

soup = BeautifulSoup(webdriver.page_source, "html.parser")

for comment in soup.select("ul > ul"):
    for c in comment.select('div > li > div > div > div > span'):
      comment_list.append(c.text)

for id in soup.select("ul > ul"):
    for i in id.select('div > li > div > div > div > a'):
       id_lists = i.attrs['href']
       id_list.append(id_lists)

listcount = len(id_list)

sys.stdout = open('ID_List >> Comment_List And Random Result.txt', 'a')

while num < listcount:
    print(id_list[num], ">>" , comment_list[num],"\n")
    num = num + 1

print(listcount)

end_list = random.sample(id_list, 3)

print(end_list)
