from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # запомнить первое окно
    first_window = browser.window_handles[0]

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

    # перейдем в новое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("span#input_value")
    x = int(x.text)

    field = browser.find_element_by_css_selector("input#answer")
    field.send_keys(str(calc(x)))

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
