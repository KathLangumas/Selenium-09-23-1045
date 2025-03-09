from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(), 'Purchase')]")
    SUCCESS_MESSAGE = (By.XPATH, "//h2[contains(text(), 'Thank you')]")
    
    def place_order(self):
        self.click_element(self.PLACE_ORDER_BUTTON)
    
    def fill_order_form(self, name, country, city, card, month, year):
        self.send_keys_to_element(self.NAME_INPUT, name)
        self.send_keys_to_element(self.COUNTRY_INPUT, country)
        self.send_keys_to_element(self.CITY_INPUT, city)
        self.send_keys_to_element(self.CARD_INPUT, card)
        self.send_keys_to_element(self.MONTH_INPUT, month)
        self.send_keys_to_element(self.YEAR_INPUT, year)
    
    def complete_purchase(self):
        self.click_element(self.PURCHASE_BUTTON)
    
    def is_purchase_successful(self):
        return self.is_element_visible(self.SUCCESS_MESSAGE)
