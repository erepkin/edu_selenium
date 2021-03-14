from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser, 14)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "100"))

    btn = browser.find_element_by_css_selector("button#book")
    btn.click()

    x = browser.find_element_by_id("input_value")
    x = int(x.text)

    field = browser.find_element_by_css_selector("input#answer")
    field.send_keys(str(calc(x)))

    btn2 = browser.find_element_by_css_selector("button#solve")
    btn2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


