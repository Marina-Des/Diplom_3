import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:


    @allure.step("Инициализация экземпляра класса BasePage")
    def __init__(self, driver):
        self.driver = driver
        

    @allure.step("Подождать видимости элемента с переданным локатором")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    

    @allure.step('Ждем, пока элемент не станет невидимым')
    def wait_for_element_invisible (self, locator, timeout = 15):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))


    @allure.step("Перейти к элементу с переданным локатором")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step("Кликнуть на элемент с переданным локатором")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    
    @allure.step("Кликаем на элемент скриптом, даже если он чем-то перекрыт")
    def click_on_element_anyway (self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step("Вставить переданное значение в элемент с переданным локатором")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)


    @allure.step("Получить текст элемента с переданным локатором")
    def get_text_of_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text
    

    @allure.step("Вернуть текущий url драйвера")
    def get_current_url (self):
        return self.driver.current_url


    @allure.step("Перетащить элемент на элемент")
    def drag_and_drop_2el (self, element_locator, target_locator):
        actions = ActionChains(self.driver)
        element = self.wait_for_element(element_locator)
        target = self.wait_for_element(target_locator)
        self.scroll_to_element(element_locator)
        actions.drag_and_drop(element, target).perform()

