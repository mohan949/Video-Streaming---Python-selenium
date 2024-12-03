from selenium.webdriver.common.by import By
from .Basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProjectPage(BasePage):
    DETAILS_TAB = (By.ID, "detailsSection")  
    VIDEOS_TAB = (By.ID, "detailsSection")  

    def switch_to_details_tab(self):
        self.wait_for_element(self.DETAILS_TAB, EC.element_to_be_clickable)
        self.click_element(self.DETAILS_TAB)



    def switch_to_videos_tab(self):
        self.wait_for_element(self.VIDEOS_TAB, EC.element_to_be_clickable)
        self.click_element(self.VIDEOS_TAB)
