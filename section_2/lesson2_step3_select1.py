import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(url)
    sum_str = str(int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum_str)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()
