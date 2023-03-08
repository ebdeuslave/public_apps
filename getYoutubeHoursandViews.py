from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



def run():
    video = 'https://www.youtube.com/watch?v=5CbgV7h9e8Q'
    TOTAL_BROWSERS = 5
    DRIVERS = []

    for n in range(TOTAL_BROWSERS):
        DRIVERS.append(webdriver.Chrome(ChromeDriverManager().install()))
        DRIVERS[n].get(video)
        # WebDriverWait(DRIVERS[n], 1000).until(EC.presence_of_element_located((By.ID, 'ytd-player')))
        action = ActionChains(DRIVERS[n])
        action.send_keys(Keys.SPACE)
        # action.send_keys('m')
        action.perform()

run()
                          



