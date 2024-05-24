import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try :
        driver.find_element(By.NAME,"pramod").send_keys("the testing academy")
    #except Exception as e:
        #print("exception is", e)
    except NoSuchElementException as nse:
        print(f"No Such a element found, check locator:  {nse}")
    time.sleep(5)
    driver.quit()