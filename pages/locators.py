from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form button")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success")
    MESSAGE_SUCCESS__PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
    MESSAGE_CART_COST = (By.CSS_SELECTOR, "#messages .alert-info")
    MESSAGE_CART_COST__COST = (By.CSS_SELECTOR, "#messages .alert-info strong")
