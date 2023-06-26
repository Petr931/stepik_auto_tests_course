import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_trash_button(browser, url):
    link = url
    browser.get(link)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "btn-add-to-basket")))
    button_name = browser.find_element(By.CLASS_NAME, "btn-add-to-basket").text
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket").click()
    assert button_name == "Добавить в корзину"
