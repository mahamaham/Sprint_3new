from locators import MainPageLocators
from urls import URLS
from conftest import driver, options


class TestConstructorPage:
    def test_transition_to_bun_success(self, driver, options):
        # Проверка перехода к разделу 'Булки'
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        driver.find_element(*MainPageLocators.bun_btn).click()

        bun_displayed = driver.find_element(*MainPageLocators.bun_ul).is_displayed()
        bun_btn_class = driver.find_element(*MainPageLocators.bun_btn).get_attribute('class')

        assert bun_displayed and 'active' in bun_btn_class


    def test_transition_to_sauces_success(self, driver, options):
        # Проверка перехода к разделу 'Соусы'
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        sauces = driver.find_element(*MainPageLocators.sauces).text
        sauces_displayed = driver.find_element(*MainPageLocators.sauces_ul).is_displayed()

        assert sauces == 'Соусы' and sauces_displayed


    def test_transition_to_topping_success(self, driver, options):
        # Проверка перехода к разделу 'Начинки'
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()
        topping = driver.find_element(*MainPageLocators.topping).text
        topping_displayed = driver.find_element(*MainPageLocators.topping_ul).is_displayed()

        assert topping == 'Начинки' and topping_displayed
        