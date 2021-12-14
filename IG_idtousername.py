from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

ids = [id.replace('\n','') for id in open('ids.txt', 'r').readlines()]

### Add your accounts here
### RESPECT ORDERING
usernames = ['user1',  'user2',]
passwords =  ['pass1' , 'pass2',]
   

def igLogin(driver, usr, pwd):
    driver.get('https://instagram.com/')
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.NAME, 'username')))
    print('Login-in..')
    username = driver.find_element(By.NAME,'username').send_keys(usr)
    sleep(1)
    password = driver.find_element(By.NAME,'password').send_keys(pwd)
    sleep(1)
    submit = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
    try:
        WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID, 'slfErrorAlert')))
        print('Incorrect login infos OR instagram blocked the login of this account, please try running script again..')
        driver.quit()
        sleep(.5)
        os._exit(0)
    except:
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[1]/a/div/div/img')))
        print('Logged-In Successful')

def getUserFromId():
    scrapeCounter = 0
    accountsCounter = 0
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=chrome_options)
    igLogin(driver, usernames[accountsCounter], passwords[accountsCounter])
    for id in ids:
        url = 'http://instagram.com/graphql/query/?query_hash=c9100bf9110dd6361671f113dd02e7d6&variables={%22user_id%22:%22' + str(id) + '%22,%22include_chaining%22:false,%22include_reel%22:true,%22include_suggested_users%22:false,%22include_logged_out_extras%22:false,%22include_highlight_reels%22:false,%22include_related_profiles%22:false}'
        driver.get(url)
        data = driver.page_source 
        data = data.replace('\\', '')
        username = data[data.find("username")+11:data.find("owner")-4]
        with open('IGusernames.txt', 'a') as f:
            f .write(f'{username}\n')
        print(username)
        scrapeCounter += 1
        if scrapeCounter == 100:
            if accountsCounter == len(usernames)-1:
                accountsCounter = 0
            else:
                accountsCounter += 1
            scrapeCounter = 0
            driver.get('https://instagram.com/accounts/logout')
            sleep(3)
            igLogin(driver, usernames[accountsCounter], passwords[accountsCounter])
     
          
getUserFromId()
