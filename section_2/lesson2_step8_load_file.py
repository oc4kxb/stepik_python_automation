import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(url)
    browser.find_element(By.NAME, "firstname").send_keys("My name")
    browser.find_element(By.NAME, "lastname").send_keys("My surname")
    browser.find_element(By.NAME, "email").send_keys("My email")
    file_button = browser.find_element(By.ID, "file")
    file_button.send_keys(os.path.join(os.path.dirname(__file__), "lesson2_step8_load_file.txt"))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()