from .locators import LoginPageLocators
from .locators import MainPageLocators
from .base_page import BasePage
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login link is not presented"
        assert True

    def register_new_user(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        email = str(time.time()) + "@fakemail.org"
        login = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        login.send_keys(email)
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password.send_keys("123456")
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_CHEK)
        password.send_keys("123456")
        self.browser.find_element(LoginPageLocators.REGISTER_BTN).click()
