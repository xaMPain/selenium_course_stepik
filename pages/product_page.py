from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    # def should_be_add_to_cart_button(self):
    #
    # def add_product_to_cart(self):
    #
    # def should_be_success_message(self):
    #
    # def should_be_same_product(self):
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product is same"
    #     assert True
    #
    # def should_be_same_price(self):
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price is same"
    #     assert True

    # page = ProductPage(url="", browser)  # инициализируем объект Page Object
    # page.open()  # открываем страницу в браузере
    # page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
    # page.add_product_to_cart()  # жмем кнопку добавить в корзину
    # page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
