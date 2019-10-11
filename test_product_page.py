from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()  # жмем кнопку добавить в корзину
    page.solve_quiz_and_get_code()  # решаем задание и вносим ответ
    page.should_be_same_product()  # проверяем и запоминаем имя продукта
    page.should_be_same_price()  # проверям и запоминаем цену продукта
    page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
    page.should_item_in_basket()  # проверяем товар в корзине


