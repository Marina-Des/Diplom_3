from selenium.webdriver.common.by import By

class RegistrationPageLocators:

    login_link = [By.XPATH, './/a[contains(text(),"Войти")]']
    name_input = [By.XPATH, '//label[contains(text(),"Имя")]/../input']
    email_input = [By.XPATH, '//label[contains(text(),"Email")]/../input']
    password_input = [By.XPATH, '//label[contains(text(),"Пароль")]/../input']
    register_button = [By.XPATH, '//button[contains(text(),"Зарегистрироваться")]']
    incorrect_password_message = [By.XPATH, '//*[contains(text(),"Некорректный пароль")]']