from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    PRODUCT_ITEMS = (By.CLASS_NAME, "card-title")
    ADD_TO_CART_BTN = (By.XPATH, "//a[contains(text(), 'Add to cart')]")
    
    def get_products(self):
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return [product.text for product in products]
    
    def select_product(self, index=0):
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        if index < len(products):
            products[index].click()
        else:
            raise IndexError("Índice de producto fuera de rango")
    
    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BTN)
        # Esperar a que aparezca la alerta y aceptarla
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
