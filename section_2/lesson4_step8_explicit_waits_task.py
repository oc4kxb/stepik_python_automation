import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


wd = webdriver.Firefox()
wd.implicitly_wait(30)
url = "http://suninjuly.github.io/explicit_wait2.html"

try:
    wd.get(url)
    price = WebDriverWait(wd, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    wd.find_element(By.ID, value="book").click()
    x = wd.find_element(By.ID, value="input_value").text
    answer = calc(x)
    wd.find_element(By.ID, value="answer").send_keys(answer)
    wd.find_element(By.ID, value="solve").click()
finally:
    time.sleep(10)
    wd.quit()
