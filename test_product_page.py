from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])

def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()  # жмем кнопку добавить в корзину
    page.solve_quiz_and_get_code()  # решаем задание и вносим ответ
    page.should_be_same_product()  # проверяем и запоминаем имя продукта
    page.should_be_same_price()  # проверям и запоминаем цену продукта
    page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
    page.should_item_in_basket()  # проверяем товар в корзине


