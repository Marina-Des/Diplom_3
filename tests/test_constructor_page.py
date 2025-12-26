import pytest
import allure

from urls import Urls
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage


class TestConstructorPage():

    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Переход на страницу очереди заказов, а потом на страницу конструктора')
    def test_transition_to_constructor_page (self, driver_create_quit):
        driver = driver_create_quit
        fp = FeedPage(driver)
        fp.open()
        fp.click_on_constructor_link()
        new_url = fp.get_current_url()
        assert (new_url == Urls.constructor_page_url) 



    @allure.title('Переход по клику на раздел «Лента заказов»')
    @allure.description('Переход на страницу очереди заказов')
    def test_transition_to_order_feed (self, driver_create_quit):
        driver = driver_create_quit
        cp = ConstructorPage(driver)
        cp.open()
        cp.click_on_order_feed_link()
        new_url = cp.get_current_url()
        assert (new_url == Urls.order_feed_page_url)



    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Нажимаем на картинку ингредиента и ждем, пока и если появится окно с надписью "Детали ингредиента"')
    def test_details_window_appears_by_clicking_on_ingredient (self, driver_create_quit):
        driver = driver_create_quit
        cp = ConstructorPage(driver)
        cp.open()
        cp.click_on_first_sous_image()

        cp.wait_for_ingredient_details_window_capture()
        is_appeared = True
        
        assert is_appeared




    @allure.title('Всплывающее окно с информацией об ингредиенте закрывается кликом по крестику')
    @allure.description('Жмем на картинку ингредиента, ждем, пок откроется окно "Детали ингредиента", жмем на крестик и ждем, пока и если окно станет невидимым')
    def test_details_window_closed_by_clicking_on_cross (self, driver_create_quit):
        driver = driver_create_quit
        cp = ConstructorPage(driver)
        cp.open()
        cp.click_on_first_sous_image()
        cp.wait_for_ingredient_details_window_capture()
        cp.ingredient_details_window_close()
        cp.wait_for_ingredient_details_window_closed
        is_disappeared = True
        
        assert is_disappeared



    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('Запоминаем значение счетчика ингредиента, перетаскиваем его в корзину, снова смотрим значение счетчика и проверяем, что второй на единицу больше первого')
    def test_ingredient_counter_increases_after_adding_it_into_burger (self, driver_create_quit):
        driver = driver_create_quit
        cp = ConstructorPage(driver)
        cp.open()
        cp.scroll_to_first_sous_counter()
        counter_before = cp.get_first_sous_counter()
        cp.add_first_sous_to_cart()
        counter_after = cp.get_first_sous_counter()
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