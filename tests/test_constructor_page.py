import pytest
import allure

from urls import Urls
from pages.constructor_page import ConstructorPage
from locators.constructor_page_locators import ConstructorPageLocators
from pages.feed_page import FeedPage


class TestConstructorPage():

    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Переход на страницу очереди заказов, а потом на страницу конструктора')
    def test_transition_to_constructor_page (self, driver_create_quit):
        driver = driver_create_quit
        driver.get(Urls.order_feed_page_url)
        fp = FeedPage(driver)
        fp.click_on_constructor_link()
        new_url = fp.get_current_url()
        assert (new_url == Urls.constructor_page_url) 



    @allure.title('Переход по клику на раздел «Лента заказов»')
    @allure.description('Переход на страницу очереди заказов')
    def test_transition_to_order_feed (self, driver_create_quit):
        driver = driver_create_quit
        driver.get(Urls.constructor_page_url)
        cp = ConstructorPage(driver)
        cp.click_on_order_feed_link()
        new_url = cp.get_current_url()
        assert (new_url == Urls.order_feed_page_url)


    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Нажимаем на картинку ингредиента и ждем, пока и если появится окно с надписью "Детали ингредиента"')
    def test_details_window_appears_by_clicking_on_ingredient (self, driver_create_quit):
        driver = driver_create_quit
        driver.get(Urls.constructor_page_url)
        cp = ConstructorPage(driver)
        cp.click_on_element(ConstructorPageLocators.sous_image_first_any)
        try:
            cp.wait_for_element(ConstructorPageLocators.ingredient_details_capture)
            is_appeared = True
        except Exception:
            is_appeared = False
        
        assert is_appeared




    @allure.title('Всплывающее окно с информацией об ингредиенте закрывается кликом по крестику')
    @allure.description('Жмем на картинку ингредиента, ждем, пок откроется окно "Детали ингредиента", жмем на крестик и ждем, пока и если окно станет невидимым')
    def test_details_window_closed_by_clicking_on_cross (self, driver_create_quit):
        driver = driver_create_quit
        driver.get(Urls.constructor_page_url)
        cp = ConstructorPage(driver)
        cp.click_on_ingredient(ConstructorPageLocators.sous_image_first_any)
        cp.wait_for_element(ConstructorPageLocators.ingredient_details_capture)
        cp.ingredient_details_window_close()
        try:
            cp.wait_for_element_invisible(ConstructorPageLocators.ingredient_details_window)
            is_disappeared = True
        except Exception:
            is_disappeared = False
        
        assert is_disappeared



    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('Запоминаем значение счетчика ингредиента, перетаскиваем его в корзину, снова смотрим значение счетчика и проверяем, что второй на единицу больше первого')
    def test_ingredient_counter_increases_after_adding_it_into_burger (self, driver_create_quit):
        driver = driver_create_quit
        driver.get(Urls.constructor_page_url)
        cp = ConstructorPage(driver)
        cp.scroll_to_element(ConstructorPageLocators.sous_counter_first_any)
        counter_before = cp.get_text_of_element(ConstructorPageLocators.sous_counter_first_any)
        cp.add_ingredient_to_cart(ConstructorPageLocators.sous_image_first_any)
        counter_after = cp.get_text_of_element(ConstructorPageLocators.sous_counter_first_any)
        assert ((int(counter_after)-1) == int(counter_before))



        



"""
ПРОВЕРКА ОСНОВНОЙ ФУНКЦИОНАЛЬНОСТИ

Проверь:
переход по клику на «Конструктор»; 
переход по клику на раздел «Лента заказов»;
если кликнуть на ингредиент, появится всплывающее окно с деталями;
всплывающее окно закрывается кликом по крестику;
при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.
"""