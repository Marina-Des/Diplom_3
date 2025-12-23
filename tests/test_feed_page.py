import pytest
import allure

from urls import Urls
from pages.feed_page import FeedPage
from pages.constructor_page import ConstructorPage
from locators.feed_page_locators import FeedPageLocators
from locators.constructor_page_locators import ConstructorPageLocators



class TestFeedPage:

    @allure.title('Тест: при создании нового заказа счётчик «Выполнено за всё время» в Ленте заказов увеличивается')
    @allure.description('Сравниваем значение счетчика "Выполнено за все время" до и после создания заказа. Хотя никто не гарантирует, что в это время не прилетит еще какой-нибудь другой заказ')
    def test_counter_orders_for_all_time_increases (self, driver_create_register_login_quit):
        driver = driver_create_register_login_quit
        fp=FeedPage(driver)
        cp=ConstructorPage(driver)
        
        driver.get(Urls.order_feed_page_url)
        counter_before=fp.get_orders_for_all_time_counter_value()

        cp.create_order(ConstructorPageLocators.bun_image_first_any, ConstructorPageLocators.sous_image_first_any)

        driver.get(Urls.order_feed_page_url)
        counter_after=fp.get_orders_for_all_time_counter_value()
 
        assert ((int(counter_before) + 1) == int(counter_after))



    @allure.title('Тест: при создании нового заказа счётчик «Выполнено за сегодня» в Ленте заказов увеличивается')
    @allure.description('Сравниваем значение счетчика "Выполнено за сегодня" до и после создания заказа. Хотя никто не гарантирует, что в это время не прилетит еще какой-нибудь другой заказ')
    def test_counter_orders_for_today_increases (self, driver_create_register_login_quit):
        driver = driver_create_register_login_quit
        fp=FeedPage(driver)
        cp=ConstructorPage(driver)
        
        driver.get(Urls.order_feed_page_url)
        counter_before=fp.get_orders_for_today_counter_value()

        cp.create_order(ConstructorPageLocators.bun_image_first_any, ConstructorPageLocators.sous_image_first_any)

        driver.get(Urls.order_feed_page_url)
        counter_after=fp.get_orders_for_today_counter_value()
 
        assert ((int(counter_before) + 1) == int(counter_after))




    @allure.title('Тест: после оформления заказа его номер появляется в разделе «В работе»')
    @allure.description('Оформляем заказ, запоминаем его номер, переходим на Ленту заказов и ждем, пока и если этот номер появится в списке заказов "В работе"')
    def test_order_number_appears_in_list_in_process (self, driver_create_register_login_quit):
        driver = driver_create_register_login_quit
        fp=FeedPage(driver)
        cp=ConstructorPage(driver)

        order_id = cp.create_order(ConstructorPageLocators.bun_image_first_any, ConstructorPageLocators.sous_image_first_any)

        driver.get(Urls.order_feed_page_url)
        try:
            fp.wait_for_order_number_in_process_queue(order_id)
            is_appeared=True
        except Exception:
            is_appeared = False

        assert is_appeared






"""
РАЗДЕЛ "ЛЕНТА ЗАКАЗОВ"

Проверь:
при создании нового заказа счётчик «Выполнено за всё время» увеличивается;
при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;
после оформления заказа его номер появляется в разделе «В работе».

"""