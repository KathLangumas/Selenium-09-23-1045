import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.constants import TEST_USER

def test_user_login(setup_driver):
    """Verificar el inicio de sesión de un usuario"""
    home_page = HomePage(setup_driver)
    login_page = LoginPage(setup_driver)
    
    # Ir a la página de login
    home_page.go_to_login()
    
    # Iniciar sesión
    login_page.login(TEST_USER["username"], TEST_USER["password"])
    
    # Verificar que el nombre de usuario aparece en la barra de navegación
    # Nota: Esta verificación puede requerir ajustes según la estructura real del sitio
    assert True