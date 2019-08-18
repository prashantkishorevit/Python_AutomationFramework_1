from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):

        driver = self.driver

        url = utils.URL
        driver.get(url)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):

        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_on_welcome()
            homepage.click_on_logout()
            x = driver.title
            assert x == 'OrangeHRMa'

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("There is an exception")
            raise