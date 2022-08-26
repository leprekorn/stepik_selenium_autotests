from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_AT_NUMBAR = (By.CSS_SELECTOR, ".breadcrumb > .active")
    PRODUCT_NAME_ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")
    PRODUCT_PRICE_ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color ")
