from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .Basepage import BasePage

class VideoPage(BasePage):
    PLAY_BUTTON = (By.XPATH, "//button[@aria-label='Play Video']")
    PAUSE_BUTTON = (By.XPATH, "//button[@aria-label='Pause Video']")
    CONTINUE_WATCHING = (By.XPATH, "//button[@aria-label='Continue Watching']")
    VOLUME_CONTROL = (By.CLASS_NAME, "volume-control")
    SETTINGS_BUTTON = (By.XPATH, "//button[@aria-label='Settings']")
    RESOLUTION_OPTION = "//span[text()='{}']"  # Use .format() to replace with resolution

    def play_video(self):
        self.click_element(self.PLAY_BUTTON)

    def pause_video(self):
        self.click_element(self.PAUSE_BUTTON)

    def continue_watching(self):
        self.click_element(self.CONTINUE_WATCHING)

    def adjust_volume(self, volume):
        self.driver.execute_script(f"jwplayer().setVolume({volume});")

    def change_resolution(self, resolution):
        self.driver.execute_script(f"jwplayer().setCurrentQuality({resolution});")
