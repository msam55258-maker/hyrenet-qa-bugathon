from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # Locators (kept flexible due to dynamic UI)
    EMAIL_INPUT = (By.XPATH, "//input[contains(@type,'email') or contains(@placeholder,'Email')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@type,'password')]")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(.,'Sign') or contains(.,'Login')]")

    def open(self):
        self.driver.get("https://app.hyrenet.in/")

    def login(self, email, password):
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)

        sign_in_btn = self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON))
        sign_in_btn.click()
