import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()


try:
    browser.get(url)
    radio_people = browser.find_element(By.ID, "peopleRule")
    radio_people_attribute = radio_people.get_attribute("checked")
    print("Value of people radio button: ", radio_people_attribute)
    assert radio_people_attribute is not None, "People radio is not default."
finally:
    browser.quit()
