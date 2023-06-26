import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, url):
    link = url
    browser.get(link)
    answer = math.log(int(time.time()))
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/header/nav/a[2]")))
    browser.find_element(By.XPATH, "/html/body/header/nav/a[2]").click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.NAME, "login")))
    browser.find_element(By.NAME, "login").send_keys("petrlyzhin@gmail.com")
    browser.find_element(By.NAME, "password").send_keys("Qwerty12")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    time.sleep(5)
    WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.CLASS_NAME, "sign-form__btn")))
    time.sleep(2)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area")))
    browser.find_element(By.XPATH, "//textarea").clear()
    browser.find_element(By.XPATH, "//textarea").send_keys(answer)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    time.sleep(2)
    resp = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert resp == "Correct!"
