from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(url)
    browser.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Evgeni")
    browser.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Bayrambekov")
    browser.find_element(By.XPATH, "//input[contains(@class, 'city')]").send_keys("Moscow")
    browser.find_element(By.XPATH, "//input[@id='country']").send_keys("Russia")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()
