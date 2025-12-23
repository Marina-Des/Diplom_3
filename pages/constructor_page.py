import pytest
import allure
import time

from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from locators.header_locators import HeaderLocators
from urls import Urls


class ConstructorPage (BasePage):

    @allure.step('Добавляем ингредиент в корзину')
    def add_ingredient_to_cart (self, ingredient):
        self.drag_and_drop_2el (ingredient, ConstructorPageLocators.cart_section)


    @allure.step('Нажимаем на Ленту Заказов')
    def click_on_order_feed_link (self):
        self.click_on_element(HeaderLocators.feed_link)


    @allure.step('Нажимаем на картинку с ингредиентом')
    def click_on_ingredient (self, ingredient):
        self.click_on_element(ingredient)    


    @allure.step("Делаем заказ")
    def create_order (self, bun, ingredient):
        self.driver.get(Urls.constructor_page_url)
        self.wait_for_element(ConstructorPageLocators.order_create_button)
        self.add_ingredient_to_cart (bun)
        self.add_ingredient_to_cart (ingredient)
        self.click_on_element(ConstructorPageLocators.order_create_button)
        self.wait_for_element(ConstructorPageLocators.order_id)
        self.wait_for_element_invisible(ConstructorPageLocators.overlay)

        return self.get_text_of_element(ConstructorPageLocators.order_id)
    

    @allure.step('Нажимаем на крестик окна с информацией об ингредиенте')
    def ingredient_details_window_close (self):
        self.click_on_element(ConstructorPageLocators.ingredient_details_close_button)