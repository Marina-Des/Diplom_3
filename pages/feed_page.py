import pytest
import allure

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from locators.header_locators import HeaderLocators



class FeedPage (BasePage):

    @allure.step('Берем значение счетчика заказов за все время')
    def get_orders_for_all_time_counter_value (self):
        return self.get_text_of_element(FeedPageLocators.counter_orders_for_all_time)


    @allure.step('Берем значение счетчика заказов за сегодня')
    def get_orders_for_today_counter_value (self):
        return self.get_text_of_element(FeedPageLocators.counter_orders_for_today)


    @allure.step('Нажимаем на Конструктор')
    def click_on_constructor_link (self):
        self.click_on_element(HeaderLocators.constructor_link)


    @allure.step('Ждем появления номера заказа в очереди заказов "В работе"')
    def wait_for_order_number_in_process_queue (self, order_id):
        self.wait_for_element(FeedPageLocators.order_id_in_preparing_queue(order_id), 15)






