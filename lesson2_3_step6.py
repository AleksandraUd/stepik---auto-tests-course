from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(chrome_options=options, executable_path="C:/chromedriver/chromedriver.exe", )
    browser.get(link)

    button = browser.find_element_by_css_selector ("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element_by_id ("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer") 
    input1.send_keys(y)

    subnit = browser.find_element_by_css_selector ("button.btn")
    subnit.click()
    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла