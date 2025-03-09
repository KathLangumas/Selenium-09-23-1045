import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.helpers import take_screenshot
from utils.constants import BASE_URL

@pytest.fixture(scope="function")
def setup_driver():
    # Configuración del driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(BASE_URL)
    
    # Devuelve el driver para la prueba
    yield driver
    
    # Teardown - cierra el navegador después de cada prueba
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        driver = item.funcargs.get("setup_driver")
        if driver:
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            result_type = "pass" if report.passed else "fail"
            take_screenshot(driver, test_name, result_type)