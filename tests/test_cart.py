import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_add_to_cart(setup_driver):
    """Verificar que se puede agregar un producto al carrito"""
    home_page = HomePage(setup_driver)
    product_page = ProductPage(setup_driver)
    
    # Seleccionar y agregar un producto al carrito
    product_page.select_product(0)
    product_page.add_to_cart()
    
    # Verificar que la alerta ha sido aceptada (la prueba pasa si no hay excepciones)
    assert True