# инициализируем драйвер браузера. После этой команды вы должны
# увидеть новое открытое окно браузера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим сундук
    x_page = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    print(x_page)
    # Выполняем математическую функцию
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = calc(x_page)
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # Отправляем заполненную форму
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()