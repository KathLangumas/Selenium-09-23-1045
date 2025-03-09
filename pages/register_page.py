from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    USERNAME_INPUT = (By.ID, "sign-username")
    PASSWORD_INPUT = (By.ID, "sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign up')]")
    
    def register(self, username, password):
        self.send_keys_to_element(self.USERNAME_INPUT, username)
        self.send_keys_to_element(self.PASSWORD_INPUT, password)
        self.click_element(self.SIGNUP_BUTTON)
        # Esperar a que aparezca la alerta y aceptarla
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()