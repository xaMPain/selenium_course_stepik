from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    # page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()  # жмем кнопку добавить в корзину
    # page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом

# def test_add_product(browser):
