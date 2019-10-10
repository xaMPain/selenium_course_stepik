from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators ():
    PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, "#Add to basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#col-sm-6 product_main")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#price_color")
