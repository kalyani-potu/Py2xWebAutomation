from selenium import webdriver
import time

def test_open_window():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(25) # Python Interpreter waits for the 25 seconds, not the webdriver.
    driver.get("https://google.com") #bing will be closed and google is opened in the same window
    time.sleep(5)
    print(driver.title)