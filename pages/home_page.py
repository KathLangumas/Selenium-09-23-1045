from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SITE_NAME = (By.ID, "nava")
    CATEGORIES = {
        "phones": (By.XPATH, "//a[contains(text(), 'Phones')]"),
        "laptops": (By.XPATH, "//a[contains(text(), 'Laptops')]"),
        "monitors": (By.XPATH, "//a[contains(text(), 'Monitors')]")
    }
    LOGIN_LINK = (By.ID, "login2")
    SIGNUP_LINK = (By.ID, "signin2")
    CART_LINK = (By.ID, "cartur")
    
    def get_title(self):
        return self.driver.title
    
    def get_site_name(self):
        return self.get_element_text(self.SITE_NAME)
    
    def click_category(self, category):
        if category in self.CATEGORIES:
            self.click_element(self.CATEGORIES[category])
        else:
            raise ValueError(f"Categoría '{category}' no encontrada")
    
    def go_to_login(self):
        self.click_element(self.LOGIN_LINK)
    
    def go_to_register(self):
        self.click_element(self.SIGNUP_LINK)
    
    def go_to_cart(self):
        self.click_element(self.CART_LINK)
