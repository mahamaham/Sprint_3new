from data import Person
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, RecoverPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver, options


class TestLogin:
    def test_login_in_login_btn_success(self, driver, options):
        # Вход по кнопке 'Войти в аккаунт' на главной
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')


    def test_login_in_personal_account_btn_success(self, driver, options):
        # Вход через кнопку 'Личный кабинет'
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')


    def test_login_in_registration_form_success(self, driver, options):
        # Вход через кнопку в форме регистрации
        driver.get(URLS.REG_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')


    def test_login_in_recover_form_success(self, driver, options):
        # Вход в личный кабинет через форму восстановления пароля
        driver.get(URLS.RECOVER_PAGE_URL)
        driver.find_element(*RecoverPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')



