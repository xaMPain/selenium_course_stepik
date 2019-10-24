from pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

import pytest


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser,link):
        self.product = ProductFactory(title="Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        self.product.delete()

    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart(True)
        page.should_be_present_in_cart()
        page.should_check_overall_cost()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_not_be_present_in_cart()
        page.should_be_message_in_cart_about_no_items()


@pytest.mark.need_review
class TestGuestAddToBasketFromProductPage():
    def test_guest_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart(True)
        page.should_be_present_in_cart()
        page.should_check_overall_cost()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_not_be_present_in_cart()
        page.should_be_message_in_cart_about_no_items()


@pytest.mark.need_review
class TestUserCanGoToLoginPageFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()  # открываем страницу
        page.go_to_login_page()
