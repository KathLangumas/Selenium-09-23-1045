import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.constants import TEST_USER, TEST_ORDER

def test_complete_purchase(setup_driver):
    """Verificar el proceso completo de compra"""
    home_page = HomePage(setup_driver)
    login_page = LoginPage(setup_driver)
    product_page = ProductPage(setup_driver)
    cart_page = CartPage(setup_driver)
    
    # Iniciar sesión
    home_page.go_to_login()
    login_page.login(TEST_USER["username"], TEST_USER["password"])
    
    # Agregar un producto al carrito
    product_page.select_product(0)
    product_page.add_to_cart()
    
    # Ir al carrito y realizar la compra
    home_page.go_to_cart()
    cart_page.place_order()
    cart_page.fill_order_form(
        TEST_ORDER["name"],
        TEST_ORDER["country"],
        TEST_ORDER["city"],
        TEST_ORDER["card"],
        TEST_ORDER["month"],
        TEST_ORDER["year"]
    )
    cart_page.complete_purchase()
    
    # Verificar que la compra fue exitosa
    assert cart_page.is_purchase_successful()
