from selenium.webdriver.common.by import By


class ConstructorPageLocators:

    bun_image_first_any = [By.XPATH, '//img[contains(@alt, "булка")]']
    sous_image_first_any = [By.XPATH, '//img[contains(@alt, "Соус")]']
    sous_counter_first_any = [By.XPATH, '//img[contains(@alt, "Соус")]/preceding-sibling::div[contains(@class, "counter_counter")]']
    
    #'/p[contains(@class, "counter_counter__num")]']


    cart_section = [By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket")]']
    order_create_button = [By.XPATH, '//button[contains(text(), "Оформить заказ")]']

    order_id = [By.XPATH, '//h2[contains(@class, "text_type_digits-large")]']

    overlay = [By.XPATH, '//div[contains(@class, "Modal_modal_opened")]']

    tick_animation = [By.XPATH, '//img[contains(@alt, "tick animation")]']
    loading_animation = [By.XPATH, '//img[contains(@alt, "loading animation")]']

    ingredient_details_window = [By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]']

    ingredient_details_capture = [By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]//*[contains(text(), "Детали ингредиента")]']

    ingredient_details_close_button = [By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]']

