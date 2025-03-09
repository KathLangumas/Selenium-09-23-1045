import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_category_navigation(setup_driver):
    """Verificar la navegación por categorías"""
    home_page = HomePage(setup_driver)
    product_page = ProductPage(setup_driver)
    
    # Navegar a la categoría de teléfonos
    home_page.click_category("phones")
    products = product_page.get_products()
    assert len(products) > 0