
import pytest
import allure
import random
from selenium import webdriver
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage





@pytest.fixture(params=['Chrome', 'FireFox'])
def driver_create_quit (request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    if request.param == 'FireFox':
        driver = webdriver.Firefox()
    driver.set_window_size(1920,1080)
    yield driver
    driver.quit()



@pytest.fixture(params = ['Chrome', 'FireFox'])
def driver_create_register_login_quit (request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    if request.param == 'FireFox':
        driver = webdriver.Firefox()
    rp = RegistrationPage(driver)
    lp = LoginPage(driver)
    email = 'usver'+ str(int(random.random()*10000))+'@abvgd.edu'
    rp.register('Имечко', email, '1234567890')
    lp.login(email, '1234567890')
    yield driver
    driver.quit()
