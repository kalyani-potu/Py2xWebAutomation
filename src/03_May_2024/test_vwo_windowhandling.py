import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
def test_vwo_window02():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1%22)")
    driver.maximize_window()
    time.sleep(5)
    main_window = driver.current_window_handle
    windows = driver.find_elements(By.XPATH, "//img[@data-qa='danawobuqa']")
    variation1 = windows[1]
    variation1.click()
    time.sleep(10)
    for handle in driver.window_handles:
        if handle!=main_window :
            driver.switch_to.window(handle)
            print(driver.title)  # switch to child window
            time.sleep(5)
            driver.switch_to.frame("heatmap-iframe")
            clickmap = driver.find_element(By.XPATH, "//div[@data-qa='liqokuxuba']")
            clickmap.click()
            time.sleep(5)
            break

    driver.quit()
