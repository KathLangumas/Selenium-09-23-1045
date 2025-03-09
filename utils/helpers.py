import os
import time
from datetime import datetime

def generate_unique_username(prefix="testuser"):
    timestamp = int(time.time())
    return f"{prefix}_{timestamp}"

def take_screenshot(driver, test_name, result_type="pass"):
    """Toma una captura de pantalla y la guarda en la carpeta correspondiente"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = os.path.join("screenshots", "passes" if result_type == "pass" else "failures")
    os.makedirs(screenshot_dir, exist_ok=True)
    file_name = f"{test_name}_{timestamp}.png"
    file_path = os.path.join(screenshot_dir, file_name)
    driver.save_screenshot(file_path)
    return file_path
