import pytest
from pages.home_page import HomePage

def test_home_page_load(setup_driver):
    """Verificar que la página principal se carga correctamente"""
    home_page = HomePage(setup_driver)
    assert "STORE" in home_page.get_title()
    assert "PRODUCT STORE" in home_page.get_site_name()
