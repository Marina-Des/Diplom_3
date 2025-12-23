import pytest
import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.constructor_page_locators import ConstructorPageLocators
from urls import Urls

class LoginPage (BasePage):

    @allure.step('Заполняем поле "Электронная почта')
    def fill_email_input (self, email):
        self.send_keys_to_input(LoginPageLocators.email_input, email)


    @allure.step('Заполняем поле "Пароль"')
    def fill_password_input (self, password):
        self.send_keys_to_input (LoginPageLocators.password_input, password)


    @allure.step('Жмем на кнопку "Войти')
    def click_login_button (self):
        self.click_on_element_anyway(LoginPageLocators.login_button)


    @allure.step('Весь процесс авторизации: заполняем поля, нажимаем кнопку "Войти" и ждем перехода на страницу Конструктора и появления кнопки "Оформить заказ" вместо "Войти в аккаунт"')
    def login (self, email, password):
        self.driver.get(Urls.login_page_url)
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_login_button()
        self.wait_for_element(ConstructorPageLocators.order_create_button, 20)