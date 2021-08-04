from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is wrong"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_login = self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REG_PASS_INPUT)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.REG_PASS_INPUT_REPEAT)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        register_login.send_keys(email)
        password_input.send_keys(password)
        repeat_password_input.send_keys(password)
        register_btn.click()




