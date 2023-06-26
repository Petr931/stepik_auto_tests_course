import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()
    new_window = browser.window_handles
    new_window = new_window[-1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    num = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(num)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()