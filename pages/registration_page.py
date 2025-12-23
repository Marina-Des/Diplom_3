import pytest
import allure

from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from urls import Urls



class RegistrationPage (BasePage):


    @allure.step('Заполняем поле "Имя"')
    def fill_name_input (self, name):
        self.send_keys_to_input(RegistrationPageLocators.name_input, name)


    @allure.step('Заполняем поле "Электронная почта"')
    def fill_email_input (self, email):
        self.send_keys_to_input(RegistrationPageLocators.email_input, email)


    @allure.step('Заполняем поле "Пароль"')
    def fill_password_input (self, password):
        self.send_keys_to_input(RegistrationPageLocators.password_input, password)


    @allure.step('Жмем на кнопку "Зарегистрироваться"')
    def click_on_register_button (self):
        self.click_on_element_anyway(RegistrationPageLocators.register_button)


    @allure.step('Весь процесс регистрации: заполняем имя, эл.почту, пароль и жмем "Зарегистрироваться"')
    def register(self, name, email, password):
        self.driver.get(Urls.registration_page_url)
        self.fill_name_input (name)
        self.fill_email_input (email)
        self.fill_password_input (password)
        self.click_on_register_button()

