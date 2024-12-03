from selenium.webdriver.common.by import By
from .Basepage import BasePage
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


# class LoginPage(BasePage):
#     PIN_INPUT = (By.NAME, "Access Code")

#     def login(self, pin):
#         self.send_keys(self.PIN_INPUT, pin)
#         self.find_element(self.PIN_INPUT).send_keys(Keys.RETURN)


class LoginPage(BasePage):
    PIN_INPUT = (By.NAME, "Access Code")

    def login(self, pin):
        pin_input = self.wait_for_element(self.PIN_INPUT, EC.element_to_be_clickable)
        pin_input.send_keys(pin)
        pin_input.send_keys(Keys.RETURN)
        time.sleep(3)
