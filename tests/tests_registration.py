from data import Person, RandomData
from locators import RegistrationPageLocators, AuthPageLocators
from urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, options


class TestRegistrationPage:

    def test_registration_success(self, driver, options):
        # Проверка регистрации пользователя
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomData.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(AuthPageLocators.login_account_btn))
        login_btn_displayed = driver.find_element(*AuthPageLocators.login_account_btn).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed
        driver.quit()

    def test_registration_incorrect_password_check_error(self, driver, options):
        # Проверка регистрации пользователя с некорректным паролем (менее 6 символов)
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(12345)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_any_elements_located(RegistrationPageLocators.error_message_incorrect_password))
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_password).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REG_PAGE_URL)
        driver.quit()

        
