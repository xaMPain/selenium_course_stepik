from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_BUTTON), "No add product to basket button"
        # assert True

    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON)
        add_button.click()

    def should_item_in_basket(self):
        self.should_be_same_product()
        self.should_be_same_price()

    def should_be_same_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_same_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(msg_lst) == 3, "Success message not found"
        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"




