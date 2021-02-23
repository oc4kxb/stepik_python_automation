import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(url)
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()

