from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self, solve_quiz=True):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket_button.click()
        if solve_quiz:
            self.solve_quiz_and_get_code()
        product_name_at_numbar = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_AT_NUMBAR
        ).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        product_name_from_added_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ADDED_MESSAGE
        ).text
        product_price_from_added_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_ADDED_MESSAGE
        ).text
        assert (
            product_name_at_numbar == product_name_from_added_message
        ), f"Product name from message:{product_name_from_added_message} must contain product name:{product_name_at_numbar}"
        assert (
            product_price in product_price_from_added_message
        ), f"Product price from message:{product_name_from_added_message} must contain product name:{product_name_at_numbar}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but it should disappear"
