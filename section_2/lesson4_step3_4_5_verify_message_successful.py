import time

from selenium import webdriver
from selenium.webdriver.common.by import By


url = "http://suninjuly.github.io/wait1.html"
wd = webdriver.Firefox()
wd.implicitly_wait(5)

try:
    wd.get(url)
    wd.find_element(By.ID, value="verify").click()
    message = wd.find_element(By.ID, value="verify_message")

    assert "successful" in message.text
finally:
    wd.quit()
