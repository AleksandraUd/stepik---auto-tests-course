from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome(chrome_options=options, executable_path="C:/chromedriver/chromedriver.exe", )
	browser.get("http://suninjuly.github.io/explicit_wait2.html")


	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"),'$100')
	)
	button = browser.find_element(By.ID, "book")
	button.click()

	x_element = browser.find_element_by_id ("input_value")
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_id("answer") 
	input1.send_keys(y)

	subnit = browser.find_element_by_css_selector ("#solve")
	subnit.click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(30)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла

