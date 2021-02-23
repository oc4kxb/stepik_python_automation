import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(url)
    x = browser.find_element(By.ID, "input_value").text
    func = calc(x)
    field = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView();", field)
    field.send_keys(func)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView();", robot_checkbox)
    robot_checkbox.click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()
