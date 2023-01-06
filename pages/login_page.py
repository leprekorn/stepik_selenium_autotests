from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        currentUrl = self.browser.current_url
        assert (
            "login" in currentUrl
        ), f"Current url is not a login page, it is {currentUrl}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):
        register_email_field = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL
        )
        register_email_field.click()
        register_email_field.send_keys(email)
        register_password_field = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD
        )
        register_password_field.click()
        register_password_field.send_keys(password)
        register_password_confirm_field = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM
        )
        register_password_confirm_field.click()
        register_password_confirm_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        assert self.is_element_present(
            *LoginPageLocators.ALERT_SUCCESS
        ), "Alert Thanks for registering does not exist, but it should be"
