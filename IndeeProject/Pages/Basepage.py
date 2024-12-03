from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, condition=EC.visibility_of_element_located, timeout=10):
    
    
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except Exception as e:
            raise Exception(f"Error waiting for element {locator}: {e}")

    def click_element(self, locator):
        """
        Wait for an element to be clickable and click it.
        """
        element = self.wait_for_element(locator, EC.element_to_be_clickable)
        element.click()

    def send_keys(self, locator, keys):
        """
        Wait for an element to be visible and send keys to it.
        """
        element = self.wait_for_element(locator, EC.visibility_of_element_located)
        element.send_keys(keys)
