import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_uploads():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload")
    driver.maximize_window()
    # upload_file = os.path.abspath(
    # os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png"))

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(r"C:\Users\Kalyani\Pictures\Screenshots\Image_1.png")
    driver.find_element(By.ID, "file-submit").click()

    file_name_element = driver.find_element(By.ID, "uploaded-files")
    file_name = file_name_element.text

    assert file_name == "Image_1.png"
    driver.quit()
