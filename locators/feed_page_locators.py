from selenium.webdriver.common.by import By


class FeedPageLocators: 

    counter_orders_for_all_time = [By.XPATH, '//p[contains(text(), "за все время")]/following-sibling::p[1]']

    counter_orders_for_today = [By.XPATH, '//p[contains(text(), "за сегодня")]/following-sibling::p[1]']

    list_orders_ready = [By.XPATH, '']

    list_orders_in_process = [By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]']

    @classmethod
    def order_id_in_preparing_queue (cls, order_number):
        path = f'//ul[contains(@class, "OrderFeed_orderListReady")]/li[text()[2]="{order_number}"]'
        return [By.XPATH, path]

