from selenium.webdriver.common.by import By


class LoginPageLocators:

    email_input = [By.XPATH, '//label[contains(text(),"Email")]/../input']
    password_input = [By.XPATH, '//label[contains(text(),"Пароль")]/../input']
    login_button = [By.XPATH, '//button[contains(text(),"Войти")]']