from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("test_first_name")
        last_name = browser.find_element_by_css_selector(".first_block .second")
        last_name.send_keys("test_last_name")
        email = browser.find_element_by_css_selector(".first_block .third")
        email.send_keys("test@test.test")

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
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Not Equal")

        # self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("test_first_name")
        last_name = browser.find_element_by_css_selector(".first_block .second")
        last_name.send_keys("test_last_name")
        email = browser.find_element_by_css_selector(".first_block .third")
        email.send_keys("test@test.test")

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
        #assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"Not Equal")

        #self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()

