from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_BUTTON), "No add product to basket button"
        assert True

    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON)
        add_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product is same"
        assert True

    # def should_be_same_product(self):
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product is same"
    #     assert True
    #
    # def should_be_same_price(self):
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price is same"
    #     assert True


