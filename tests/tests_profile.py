from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver, options, get_login_driver

class TestProfileArea:

    def test_transition_to_personal_area_from_main_page_success(self, driver, options, get_login_driver):
        # Проверка перехода в личный кабинет с главной страницы по кнопке 'Личный кабинет'
        driver = get_login_driver
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        save_btn_displayed = driver.find_element(*PersonalAreaLocators.save_btn).is_displayed()

        assert driver.current_url == URLS.PROFILE_PAGE_URL and save_btn_displayed
        driver.quit()

    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, driver, options,
                                                                                           get_login_driver):
        # Проверка перехода по клику на 'Конструктор'
        driver = get_login_driver
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        driver.find_element(*PersonalAreaLocators.constructor_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.bun))
        bun_displayed = driver.find_element(*MainPageLocators.bun).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed
        driver.quit()

    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, driver, options,
                                                                                get_login_driver):
        # Проверка перехода по клику на логотип Stellar Burgers в конструктор
        driver = get_login_driver
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        driver.find_element(*PersonalAreaLocators.logo_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.bun))
        bun_displayed = driver.find_element(*MainPageLocators.bun).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed
        driver.quit()

    def test_logout_from_personal_area_success(self, driver, options, get_login_driver):
        # Проверка выхода из личного кабинета
        driver = get_login_driver
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        driver.find_element(*PersonalAreaLocators.exit_btn).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(AuthPageLocators.login_account_btn))
        login_btn_displayed = driver.find_element(*AuthPageLocators.login_account_btn).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed
        driver.quit()


