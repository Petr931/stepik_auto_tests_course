import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)


    browser.find_element(By.NAME, "firstname").send_keys("Petr")
    browser.find_element(By.NAME, "lastname").send_keys("Petr")
    browser.find_element(By.NAME, "email").send_keys("petr@mail.ru")
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'file.txt')
    print(file_path)
    browser.find_element(By.ID, "file").send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()