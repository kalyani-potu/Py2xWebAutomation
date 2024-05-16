import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_make_my_trip():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")

    driver.maximize_window()

    time.sleep(10)
    from_city = driver.find_element(By.ID, "fromCity")
    #from_city.send_keys("delhi")
    #time.sleep(3)
    #ActionChains(driver).move_to_element(from_city).send_keys("New Delhi").perform()
    ActionChains(driver).send_keys_to_element(from_city, 'New Delhi').perform()
    time.sleep(3)
    driver.quit()