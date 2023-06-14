from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    try:
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    except:
        assert False, 'Элемент не найден'