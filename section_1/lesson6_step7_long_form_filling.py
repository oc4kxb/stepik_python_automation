from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/huge_form.html"

try:
    browser.get(url)
    fields = browser.find_elements(By.TAG_NAME, "input")
    for field in fields:
        field.send_keys("my answer")
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()