import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_fileupload():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    upload_image = driver.find_element(By.ID, "photo")
    #action = ActionChains(driver)
    #action.send_keys_to_element()
    #print(os.getcwd())
    upload_image.send_keys(os.getcwd()+"\Image.png")
    time.sleep(3)
    download_file = driver.find_element(By.XPATH, "//a[text() = 'Click here to Download File']")
    download_file.click()
    assert driver.current_url == "https://github.com/stanfy/behave-rest/blob/master/features/conf.yaml"
    time.sleep(3)
    driver.quit()