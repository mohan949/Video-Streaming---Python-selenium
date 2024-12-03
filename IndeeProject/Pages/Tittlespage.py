# from selenium.webdriver.common.by import By
# from Basepage import BasePage
# from selenium.webdriver.support import expected_conditions as EC


# class AllTitlesPage(BasePage):
#     TEST_AUTOMATION_PROJECT = (By.XPATH, "//div[@title='Test automation project']")

#     def select_project(self):
#         # self.wait_for_element(self.TEST_AUTOMATION_PROJECT)
#         self.wait_for_element(self.TEST_AUTOMATION_PROJECT, EC.element_to_be_clickable)
#         self.click_element(self.TEST_AUTOMATION_PROJECT)



from selenium.webdriver.common.by import By
from .Basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AllTitlesPage(BasePage):
    TEST_AUTOMATION_PROJECT = (By.XPATH, "//div[@title='Test automation project']")
    TEST_AUTOMATION_PROJECT_PAGE_TITTLE = (By.XPATH,"//p[text()='Test automation project']")

    def select_project(self):
        """
        Waits for the 'Test Automation Project' to be clickable and selects it.
        """
        # Wait until the project is clickable
        self.wait_for_element(self.TEST_AUTOMATION_PROJECT, EC.element_to_be_clickable)
        # Click the project
        self.click_element(self.TEST_AUTOMATION_PROJECT)

    def verifytitle(self):
        a = self.wait_for_element(self.TEST_AUTOMATION_PROJECT_PAGE_TITTLE, EC.element_to_be_clickable)
        assert a.is_displayed()  # Verify the element is visible
        print("Successfully navigated to the Test Automation Project page")


