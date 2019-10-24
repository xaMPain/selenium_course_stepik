from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_present_in_cart(self) -> None:
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_NAME), "Product name is not present"

    def should_be_message_in_cart_about_no_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MSG), "Message is not presented"