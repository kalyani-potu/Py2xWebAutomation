import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_fileupload():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    #upload_image = driver.find_element(By.ID, "photo")
    upload_image = driver.find_element(By.CSS_SELECTOR, "input[type='file']")#recomended - we need to find element by giving input as file

    upload_image.send_keys(r"C:\Users\Kalyani\Pictures\Screenshots\Image_1.png")#give r - raw path , otherwise it will fail
    time.sleep(3)
    download_file = driver.find_element(By.XPATH, "//a[text() = 'Click here to Download File']")
    download_file.click()
    assert driver.current_url == "https://github.com/stanfy/behave-rest/blob/master/features/conf.yaml"
    time.sleep(3)
    driver.quit()