import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestLesson(unittest.TestCase):
    def test_lesson(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")
            browser.implicitly_wait(2)
            input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CLASS_NAME, "second")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CLASS_NAME, "third")
            input3.send_keys("ivan@mail.ru")
            input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
            input4.send_keys("+79203554894")
            input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
            input4.send_keys("Смоленск")
            button = browser.find_element(By.CLASS_NAME, "btn")
            button.click()
            Congratulations = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(Congratulations, "Congratulations! You have successfully registered!", "Регистрация не успешна")
        finally:
            # успеваем скопировать код за 30 секунд
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_lesson2(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration2.html")
            browser.implicitly_wait(2)
            input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Ivan")
            input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
            input3.send_keys("ivan@mail.ru")
            input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
            input4.send_keys("+79203554894")
            input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
            input4.send_keys("Смоленск")
            button = browser.find_element(By.CLASS_NAME, "bn")
            button.click()
            Congratulations = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(Congratulations, "Congratulations! You have successfully registered!", "Регистрация не успешна")
        finally:
            # успеваем скопировать код за 30 секунд
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()