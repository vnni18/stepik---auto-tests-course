# в одном файле делал все уроки, для меня это удобнее

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    #return str(math.log(abs(12*math.sin(int(x)))))
    return str(math.log(abs(12*math.sin(x))))

try:
    #print (y)
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    a = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    browser.find_element_by_css_selector("button#book.btn").click()
    #browser.switch_to.alert.accept()

    #new_wind=browser.window_handles[1]
   # browser.switch_to.window(new_wind)

    #browser.implicitly_wait(5)

    text_x = browser.find_element_by_css_selector("span#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_x)

    x=browser.find_element_by_css_selector('span#input_value').text
    y=calc(int(x))
    browser.find_element_by_css_selector('input#answer').send_keys(y)

    #browser.find_element_by_css_selector('input[name="firstname"]').send_keys("Sergey")
    #browser.find_element_by_css_selector('input[name="lastname"]').send_keys("Lebedev")
    #browser.find_element_by_css_selector('input[name="email"]').send_keys("test@test.test")

    #path_name = os.path.abspath(os.path.dirname(__file__))
    #full_link_upload_file = os.path.join(path_name,'test.txt')

    #browser.find_element_by_css_selector('input#file').send_keys(full_link_upload_file)

    #robotsRule = browser.find_element_by_css_selector("input#robotsRule")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    #robotsRule.click()


    button = browser.find_element_by_css_selector("button#solve.btn").click()
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    text=browser.switch_to.alert.text

    print (text)

    #button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()
    #assert True

    #browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #x = browser.find_element_by_css_selector("span#num1").text
    #y = browser.find_element_by_css_selector("span#num2").text

    #select = Select(browser.find_element_by_css_selector("select#dropdown"))
    #select.select_by_value(str(int(x) + int(y)))

    #browser.find_element_by_css_selector("input#answer").send_keys(y)

    #browser.find_element_by_css_selector("input#robotCheckbox").click()

    #browser.find_element_by_css_selector("input#robotsRule").click()

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()