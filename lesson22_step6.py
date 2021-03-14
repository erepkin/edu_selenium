from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x = int(x.text)

    btn = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

    field = browser.find_element_by_css_selector("input#answer")
    field.send_keys(str(calc(x)))

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    btn = browser.find_element_by_class_name("btn")
    btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
