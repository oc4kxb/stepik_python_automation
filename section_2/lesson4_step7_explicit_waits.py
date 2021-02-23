from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# инициализируем ссылку на драйвер
wd = webdriver.Firefox()

try:
    # добавляем неявные ожидания
    # wd.implicitly_wait(5)
    # передаем драйверу ссылку и переходим по ней
    wd.get("http://suninjuly.github.io/wait2.html")

    # button = wd.find_element(By.ID, value="verify")
    button = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()
    # button = WebDriverWait(wd, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))
    message = wd.find_element(By.ID, value="verify_message")

    assert "successful" in message.text
finally:
    wd.quit()
