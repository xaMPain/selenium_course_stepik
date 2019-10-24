from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CHEK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


class BasketPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items > div > div> a")
    BASKET_MSG = (By.CSS_SELECTOR, "#content_inner > p")
