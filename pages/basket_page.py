from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PAGE_ITEMS
        ), "Basket contains items, but it should not"

    def basket_is_not_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_PAGE_ITEMS
        ), "Basket should contain items, but it is empty"

    def basket_empty_message_exists(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_MESSAGE
        ), "Message that Basket is empty does not exist"

    def basket_empty_message_not_exists(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_MESSAGE
        ), "Message that Basket is empty exist, but it should not"
