from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(chrome_options=options, executable_path="C:/chromedriver/chromedriver.exe", )
    browser.get(link)

    input1 = browser.find_element_by_css_selector ("input:required.form-control.first")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element_by_css_selector ("input:required.form-control.second")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_css_selector ("input:required.form-control.third")
    input3.send_keys("example@mail.ru")
 

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()