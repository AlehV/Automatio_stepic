from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)



    input1 = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    input1.send_keys("Atadjhmakhal")

    input2 = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    input2.send_keys("Batinbabat")

    input3 = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
    input3.send_keys("zhena@zhizni.net")

    element = browser.find_element(By.CSS_SELECTOR, "[name = 'file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()