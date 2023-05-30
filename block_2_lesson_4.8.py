import math
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    browser.find_element(By.ID, "price").text
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.ID, "input_value").text
    num = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(num)
    browser.find_element(By.ID, "solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()