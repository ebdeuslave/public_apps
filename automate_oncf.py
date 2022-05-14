from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time

def oncfAuto(processNumber):
    start = time()
    options = webdriver.ChromeOptions()
    # exclude debugging msgs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window() 
    print(f'####################### Process N° {processNumber} - Launching Chrome #######################')
    action = ActionChains(driver)
    driver.get('https://www.oncf-voyages.ma/')
    print(f'Process N° {processNumber} - Waiting for page to load..')
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'origin')))
    sleep(3)
    depart = driver.find_element(By.ID, 'origin')
    sleep(1)
    depart.click()
    sleep(1)
    action.send_keys('Casa Port').key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    print(f'Process N° {processNumber} - Ville Depart')
    sleep(1)
    destination = driver.find_element(By.ID, 'destination')
    sleep(1)
    destination.click()
    sleep(1)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys('Rabat Agdal').key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    print(f'Process N° {processNumber} - Ville Destination')
    sleep(1)
    search = driver.find_element(By.CLASS_NAME, 'searchForm_footer  ').click()
    print(f'Process N° {processNumber} - Loading results..')
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-btn.btn-default.ant-btn-default.ant-btn-round')))
    reserver = driver.find_elements(By.CLASS_NAME,'ant-btn.btn-default.ant-btn-default.ant-btn-round')
    reserver[-1].click()
    print(f'Process N° {processNumber} - Reserve for last trip..')
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-btn.btn-default-ghost.tariffsrecomandation_card_cta.card-button-active.Flex.ant-btn-default.ant-btn-round.ant-btn-background-ghost')))
    sleep(5)
    print(f'Process N° {processNumber} - Select Trip..')
    select = driver.find_element(By.CLASS_NAME, 'ant-btn.btn-default-ghost.tariffsrecomandation_card_cta.card-button-active.Flex.ant-btn-default.ant-btn-round.ant-btn-background-ghost').click()
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-btn.btn-secondary.btn-large.ant-btn-secondary.ant-btn-round')))
    sleep(5)
    print(f'Process N° {processNumber} - Add to Basket..')
    add = driver.find_element(By.CLASS_NAME, 'ant-btn.btn-secondary.btn-large.ant-btn-secondary.ant-btn-round').click()
    sleep(3)
    # Go to AUTH page     
    driver.get('https://www.oncf-voyages.ma/resultats-disponibilites/authentification')
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'SignInFormUsername')))
    sleep(3)
    print(f'Process N° {processNumber} - Logging..')
    email = driver.find_element(By.ID, 'SignInFormUsername').send_keys('ebdeu.slave@gmail.com')
    sleep(1)
    passwd = driver.find_element(By.ID, 'SignInFormPassword').send_keys('maroc.2022')
    sleep(1)
    login = driver.find_element(By.CLASS_NAME, 'ant-btn.btn-secondary.SignInForm_ctaSignIn.ant-btn-secondary.ant-btn-round').click()
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'PassengerComponent_form-label')))
    sleep(2)
    print(f'Process N° {processNumber} - Writing my infos..')
    inputs = driver.find_elements(By.CLASS_NAME, 'ant-input.CustomInput ')
    inputs[0].send_keys('Abderrahim')
    sleep(1)
    inputs[1].send_keys('Essaouaf')
    sleep(1)
    accept = driver.find_elements(By.CLASS_NAME, 'ant-checkbox-input')[1].click()
    sleep(1)
    pay = driver.find_element(By.CLASS_NAME, 'ant-btn.btn-default.FormComponent_confirm.ant-btn-default.ant-btn-round').click()
    print(f'Process N° {processNumber} - Going to Payment Step (CMI Page)')
    end = time()
    duration = end - start
    print(f'Process N° {processNumber} - Automation Finished in {round(duration,2)} seconds | {round(duration/60,2)} minutes')
    sleep(30)
    print(f'Process N° {processNumber} - Window Closed ')
    
    

# run script multiple times at the same time using multiprocessing module
# WARNING : use n times depends on your CPU power, madirsh chi ra9m kbir f processeur na9s radi y tplonta
from multiprocessing import Process
# change n times according to your need
times = 10
# collecting processes in a list
processes = [Process(target=oncfAuto, args=(str(i),)) for i in range(1,times+1)]

if __name__ == '__main__':   
    s = time()
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
    e = time()
    d = e-s
    print(f'processes finished in {round(d,2)} seconds | {round(d/60,2)} minutes')
