import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_page = browser.find_element(By.ID, "input_value").text
    x_page = int(x_page)
    num = str(math.log(abs(12 * math.sin(int(x_page)))))
    button = browser.find_element(By.TAG_NAME, "button")
    browser.find_element(By.ID, "answer").send_keys(num)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "robotsRule").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()