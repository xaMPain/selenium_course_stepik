from .pages.product_page import ProductPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart(True)  # жмем кнопку добавить в корзину
    page.should_not_be_success_message()  # смотрим есть сообщение или нет

def test_guest_cant_see_alert(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_not_be_success_message()  #смотрим есть сообщение или нет

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart(True)  # жмем кнопку добавить в корзину
    page.should_disappear_success_message()    # смотрим исчезло сообщение или нет