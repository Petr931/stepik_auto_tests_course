# инициализируем драйвер браузера. После этой команды вы должны
# увидеть новое открытое окно браузера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим сундук
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    num1 = int(num1)
    num2 = int(num2)
    final_num = num1 + num2
    final_num = str(final_num)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(final_num)  # ищем элемент с суммой чисел



    # Отправляем заполненную форму
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)
#
#
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()