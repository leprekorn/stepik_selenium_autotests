from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default:first-child")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_AT_NUMBAR = (By.CSS_SELECTOR, ".breadcrumb > .active")
    PRODUCT_NAME_ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_PRICE_ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color ")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child")


class BasketPageLocators:
    BASKET_PAGE_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
