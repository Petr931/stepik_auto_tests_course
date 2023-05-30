# инициализируем драйвер браузера. После этой команды вы должны
# увидеть новое открытое окно браузера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    x_page = browser.find_element(By.ID, "input_value").text
    # Выполняем математическую функцию
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = calc(x_page)
    browser.find_element(By.CLASS_NAME, "form-control").send_keys(x)
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