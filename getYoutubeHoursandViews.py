from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import babel.numbers



def run():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # keep browser open
    video = 'https://www.youtube.com/watch?v=QLOyJViDqHc'
    TOTAL_BROWSERS = 5
    DRIVERS = []

    for n in range(TOTAL_BROWSERS):
        DRIVERS.append(webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options))
        DRIVERS[n].get(video)
        while 1:
            try:
                WebDriverWait(DRIVERS[n], 20).until(EC.presence_of_element_located((By.ID, 'ytd-player')))
                action = ActionChains(DRIVERS[n])
                action.send_keys(Keys.SPACE)
                # action.send_keys('m')
                action.perform()
                print(f'Page N{n} Loaded Completly')
                break
                
            except:
                DRIVERS[n].refresh()
                print(f'Page N{n} Refreshed..')
 

run()
                          



