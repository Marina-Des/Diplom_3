from selenium.webdriver.common.by import By

class HeaderLocators:

    feed_link = [By.XPATH, '//p[contains(text(),"Лента Заказов")]']
    constructor_link = [By.XPATH, '//p[contains(text(), "Конструктор")]']
    