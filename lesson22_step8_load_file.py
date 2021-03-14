from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    current_dir = os.path.abspath(os.path.dirname(__file__))

    browser = webdriver.Chrome()
    browser.get(link)

    first_field = browser.find_element_by_name("firstname")
    first_field.send_keys("Evgeny")

    last_field = browser.find_element_by_name("lastname")
    last_field.send_keys("Repkin")

    email_field = browser.find_element_by_name("email")
    email_field.send_keys("erepkin@gmail.com")

    file = browser.find_element_by_id("file")
    file_path = os.path.join(current_dir, '1.txt')
    file.send_keys(file_path)

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
