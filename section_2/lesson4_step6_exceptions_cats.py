from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/cats.html"
wd = webdriver.Firefox()

wd.get(url)
wd.find_element(By.ID, value="button")