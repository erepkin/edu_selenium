from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    span1 = browser.find_element_by_css_selector("span#num1")
    num1 = int(span1.text)
    span2 = browser.find_element_by_css_selector("span#num2")
    num2 = int(span2.text)
    sum_spans = num1 + num2

    select = Select(browser.find_element_by_css_selector("select#dropdown"))
    select_sum = select.select_by_visible_text(str(sum_spans))

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
