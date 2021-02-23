import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/registration1.html")

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста

try:
    input1 = driver.find_element_by_css_selector(".first_block .first_class input")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_css_selector(".first_block .second_class input")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_css_selector(".first_block .third_class input")
    input3.send_keys("Smolensk")
    # input4 = driver.find_element_by_id("country")
    # input4.send_keys("Russia")
    button = driver.find_element_by_xpath("//button[text()='Submit']")
    button.click()
    time.sleep(1)
    welcome = driver.find_element_by_tag_name("h1")
    welcome_text = welcome.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    driver.quit()

# После выполнения всех действий мы не должны забыть закрыть окно браузера
