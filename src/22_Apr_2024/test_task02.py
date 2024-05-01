import time
import pytest
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Print all the top 60 results of 16gb laptops")
@allure.description("TC#01 - Print all the top 60 results of 16gb laptops and print the cheapest one")
def test_ebay_laptop():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    search_box = driver.find_element(By.XPATH, value="//input[@id = 'gh-ac']")
    search_box.send_keys("16gb")
    search_button = driver.find_element(By.XPATH, value="//input[@id = 'gh-btn']")
    search_button.click()
    title_list = driver.find_elements(By.XPATH, value="//span[@role = 'heading']")
    for i in title_list:
        print(i.text)
    price_list = driver.find_elements(By.XPATH, value="//span[@class = 's-item__price']")
    for i in price_list:
        print(i.text)
    time.sleep(5)
    driver.quit()
