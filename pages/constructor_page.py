import pytest
import allure

from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from locators.header_locators import HeaderLocators
from urls import Urls



class ConstructorPage (BasePage):


    @allure.step('Открываем страницу Конструктора')
    def open (self):
        self.driver.get(Urls.constructor_page_url)

# Click on links

    @allure.step('Нажимаем на Ленту Заказов')
    def click_on_order_feed_link (self):
        self.click_on_element(HeaderLocators.feed_link)


# Adding to cart

    @allure.step('Добавляем ингредиент в корзину')
    def add_ingredient_to_cart (self, ingredient):
        self.drag_and_drop_2el (ingredient, ConstructorPageLocators.cart_section)


    @allure.step('Добавляем ингредиент в корзину')
    def add_first_sous_to_cart (self):
        self.add_ingredient_to_cart(ConstructorPageLocators.sous_image_first_any)



# Actions with first sous

    @allure.step("Нажимаем на картинку первого соуса на странице")
    def click_on_first_sous_image (self):
        self.click_on_element(ConstructorPageLocators.sous_image_first_any)

    @allure.step("Получаем значение счетчика у первого соуса на странице")
    def get_first_sous_counter (self):
        return self.get_text_of_element(ConstructorPageLocators.sous_counter_first_any)

    @allure.step("Скроллим до счетчика первого соуса на странице")
    def scroll_to_first_sous_counter (self):
        self.scroll_to_element(ConstructorPageLocators.sous_counter_first_any)



# Ingredient details window

    @allure.step("Ждем появления заголовка на окне с информацией об ингредиенте ")
    def wait_for_ingredient_details_window_capture (self):
        self.wait_for_element(ConstructorPageLocators.ingredient_details_capture)


    @allure.step("Ждем исчезания окна с информацией об ингредиенте")
    def wait_for_ingredient_details_window_closed (self):
        self.wait_for_element_invisible(ConstructorPageLocators.ingredient_details_window)


    @allure.step('Нажимаем на крестик окна с информацией об ингредиенте')
    def ingredient_details_window_close (self):
        self.click_on_element(ConstructorPageLocators.ingredient_details_close_button)



# Complex methods

    @allure.step("Делаем заказ")
    def create_order (self, bun, ingredient):
        self.open()
        self.wait_for_element(ConstructorPageLocators.order_create_button)
        self.add_ingredient_to_cart (bun)
        self.add_ingredient_to_cart (ingredient)
        self.click_on_element(ConstructorPageLocators.order_create_button)
        self.wait_for_element(ConstructorPageLocators.order_id)
        self.wait_for_element_invisible(ConstructorPageLocators.overlay)

        return self.get_text_of_element(ConstructorPageLocators.order_id)
    

    @allure.step("Делаем заказ с первой на странице булкой и первым соусом")
    def create_order_with_first_bun_and_first_soun_on_page (self):
        self.create_order(ConstructorPageLocators.bun_image_first_any, ConstructorPageLocators.sous_image_first_any)

