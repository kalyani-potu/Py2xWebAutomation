import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys


def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    driver.maximize_window()
    time.sleep(10)
    search = driver.find_element(By.ID, "search_city")
    search.send_keys("India")
    time.sleep(5)
    states_list = driver.find_elements(By.XPATH, "//table[@id = 'example']/tbody/tr/td[2]")
    for state in states_list:
        AQI = driver.find_element(locate_with(By.TAG_NAME, 'p').to_right_of(state)).text
        Rank = driver.find_element(locate_with(By.TAG_NAME, 'p').to_left_of(state)).text
        print(state.text + "--" + AQI + "--" + Rank)
        b_s =driver.find_element(locate_with(By.TAG_NAME, 'p').below(state)).text
        a_s = driver.find_element(locate_with(By.TAG_NAME, 'p').above(state)).text
        print(state.text + " | " + a_s + " | " + b_s)
    time.sleep(5)
    driver.quit()