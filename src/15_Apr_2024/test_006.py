from selenium import webdriver
import time

def test_open_window():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    print(driver.title)
    time.sleep(10)

    driver.get("https://www.google.com") #bing will be closed and google is opened in the same window
    print(driver.title)
    time.sleep(10)

    driver.back()
    print(driver.title)
    time.sleep(10)

    driver.forward()
    print(driver.title)
    time.sleep(10)

    driver.refresh()
    time.sleep(5)

    driver.quit()

