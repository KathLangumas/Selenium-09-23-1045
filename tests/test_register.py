import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.helpers import generate_unique_username

def test_user_registration(setup_driver):
    """Verificar el registro de un nuevo usuario"""
    home_page = HomePage(setup_driver)
    register_page = RegisterPage(setup_driver)
    
    # Generar un nombre de usuario único
    username = generate_unique_username()
    password = "password321"
    
    # Ir a la página de registro
    home_page.go_to_register()
    
    # Registrar un nuevo usuario
    register_page.register(username, password)
    
    # La prueba pasa si no hay excepciones al aceptar la alerta
    assert True
