from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.facebook.com')
driver.maximize_window()

login = '+380951555067'
password = 'Zxcvbbh1001'
posttext = 'Детейлинг по ОООООЧЕНЬ заманчивым ценам (полировка от 500 зл), забрать можно будет в тот же день, запись по телефону +48575802988 (вайбер, телеграм)'
links = ['https://www.facebook.com/groups/3128380087479243',
         'https://www.facebook.com/groups/262170162611121/',
         'https://www.facebook.com/groups/2584770008429617/',
         'https://www.facebook.com/groups/2237760959691023/',
         'https://www.facebook.com/groups/1914987112129364/',
         'https://www.facebook.com/groups/1719780204922540/',
         'https://www.facebook.com/groups/283261534590416/',
         'https://www.facebook.com/groups/860799038124297/',
         'https://www.facebook.com/groups/482137544110205/buy_sell_discussion',
         'https://www.facebook.com/groups/347049072421381/',
         'https://www.facebook.com/groups/283261534590416/',
         'https://www.facebook.com/groups/580735663600249/',
         'https://www.facebook.com/groups/636342251753018/',
         'https://www.facebook.com/groups/747804602313295/',
         'https://www.facebook.com/groups/1252032521959617/',
         'https://www.facebook.com/groups/832808721501645/',
         'https://www.facebook.com/groups/534583221794180/',
         'https://www.facebook.com/groups/926326504786312/']

def createpost():
    buttonaddpost = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/span')
    buttonaddpost.click()
    time.sleep(10)
    inputposttext = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
    inputposttext.send_keys(posttext)
    buttonpost = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div')
    buttonpost.click()
    time.sleep(15)

time.sleep(5)

buttonallow = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]')
buttonallow.click()

time.sleep(5)

inputlogin = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
inputlogin.send_keys(login)
inputpassword = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
inputpassword.send_keys(password)
buttonlogin = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
buttonlogin.click()

time.sleep(10)

for i, golink in enumerate(links, start=1): 
    driver.get(golink)
    time.sleep(10)
    createpost()

driver.quit()