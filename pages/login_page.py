import pytest
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Не нашли форму входа"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Не нашли форму регистрации"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS_FIELD)
        login.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        pass2.send_keys(password)
        input_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        input_reg.click()




