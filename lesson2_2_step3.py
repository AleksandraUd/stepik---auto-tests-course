from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
import time 
import math
from selenium.webdriver.support.ui import Select 

link = " http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(chrome_options=options, executable_path="C:/chromedriver/chromedriver.exe", )
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    select = Select(browser.find_element_by_tag_name("select")) 
    select.select_by_value(str(int(num1.text)+int(num2.text)))

    subnit = browser.find_element_by_css_selector ("button.btn")
    subnit.click()
    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла