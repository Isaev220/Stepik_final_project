from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert 'login' in login_url, "Login is not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        a = self.is_element_present(*LoginPageLocators.EMAIL_LOGIN_LINK)
        b = self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN_LINK)
        assert a and b, "Email or password link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        c = self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION_LINK)
        d = self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_LINK)
        e = self.is_element_present(*LoginPageLocators.REPASSWORD_REGISTRATION_LINK)
        assert c and d and e, "Email or password or repassword link is not presented"
