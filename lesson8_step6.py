from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "[class = 'form-control']")
    input1.send_keys(y)

    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 150);")



    option1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value = 'robots']")
    option2.click()
    button.click()

    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()