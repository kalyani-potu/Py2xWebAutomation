import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl
import pytest
import allure

def read_test_data():
    credentials = []
    workbook = openpyxl.load_workbook(r"C:\Users\Kalyani\Desktop\Testdata_ddt.xlsx")
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        firstname = row
        credentials.append(firstname)
    return credentials

@pytest.mark.parametrize("user_details", read_test_data())
def test_ddt(user_details):
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    firstname = driver.find_element(By.NAME, "firstname")
    firstname.send_keys(user_details)
    time.sleep(3)
    driver.quit()

