import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "http://suninjuly.github.io/redirect_accept.html"
wd = webdriver.Firefox()

try:
    wd.get(url)
    wd.find_element(By.TAG_NAME, value="button").click()
    wd.switch_to.window(wd.window_handles[1])
    time.sleep(1)
    x = wd.find_element(By.ID, value="input_value").text
    answer = calc(x)
    wd.find_element(By.ID, value="answer").send_keys(answer)
    wd.find_element(By.TAG_NAME, value="button").click()
finally:
    time.sleep(10)
    wd.quit()
