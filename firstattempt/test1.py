from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (using Chrome in this case)
driver = webdriver.Chrome()

@given('I am on the login page')
def step_impl(context):
    # Open the FYC platform
    driver.get("https://indeedemo-fyc.watch.indee.tv/")  # Directly use the URL here
    # Wait for the page to load and the Access Code field to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Access Code")))

@when('I log in using the PIN "{pin}"')
def step_impl(context, pin):
    # Find the PIN input and submit the login form
    pin_input = driver.find_element(By.NAME, "Access Code")
    pin_input.send_keys(pin)
    pin_input.send_keys(Keys.RETURN)
    # Wait for the page title to change (indicating successful login)
    WebDriverWait(driver, 10).until(EC.title_contains("Brands | Enterprise test FYC"))

@then('I should be on the "All Titles" page')
def step_impl(context):
    # Verify that we are on the correct page
    print('Page title ----> ', driver.title)
    assert "Brands | Enterprise test FYC" in driver.title

@then('I should see the "Test Automation Project"')
def step_impl(context):
    # Wait for the "Test Automation Project" to be visible and click it
    project = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='Test automation project']"))
    )
    project.click()
    assert project.is_displayed()

@when('I play the video')
def step_impl(context):
    # Wait for the menubar to be visible and find the play button
    menubar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='menu-bar']"))
    )
    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "detailsSection"))
    )
    play_button.click()

@then('the video should be playing')
def step_impl(context):
    # Verify that the video is playing
    video = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "video-player"))
    )
    assert "playing" in video.get_attribute("class")

@when('I adjust the volume to {volume}%')
def step_impl(context, volume):
    # Wait for the volume control and adjust it
    volume_control = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "volume-control"))
    )
    volume_control.send_keys(Keys.ARROW_UP * int(volume))  # Adjust volume based on platform

@then('the volume should be {volume}%')
def step_impl(context, volume):
    # Verify the volume level
    volume_level = driver.find_element(By.CLASS_NAME, "volume-level")
    assert volume_level.text == f"{volume}%"

@when('I change the resolution to "{resolution}"')
def step_impl(context, resolution):
    # Wait for the resolution control and change it
    resolution_control = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "resolution-control"))
    )
    resolution_control.click()
    resolution_control.send_keys(resolution)

@then('the resolution should be "{resolution}"')
def step_impl(context, resolution):
    # Verify the selected resolution
    current_resolution = driver.find_element(By.CLASS_NAME, "current-resolution")
    assert current_resolution.text == resolution

@then('I close the browser')
def step_impl(context):
    # Close the browser after all steps
    driver.quit()



'''
        # Switch to the iframe by ID
    iframe = driver.find_element(By.ID, "video_player")
    driver.switch_to.frame(iframe)
    iframe.send_keys(Keys.SPACE)
    print('---------> SPACE')

    time.sleep(8)    

    video_pause = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@aria-label='Pause'])[2]"))
    )
    assert video_pause.is_displayed()
    print('---------> True')

'''


    # action = ActionChains(driver)
    # for i in range(5):
    #      action.send_keys(Keys.ARROW_DOWN).perform()


        # for i in range(7):
    #      action.send_keys(Keys.TAB).perform()
    #      action.send_keys(Keys.RETURN).perform()


    #     iframe = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "video_player"))  # Replace with the actual iframe ID or locator
    # )
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''

'''
Feature: Automating video playback and control

  Scenario: Sign in and navigate to the 'Test Automation Project'
    Given I am on the login page
    When I log in using the PIN "WVMVHWBS"
    Then I should be on the "All Titles" page
    Then I should see the "Test Automation Project"


  Scenario: Play and control the video
    Given I am on the "Test Automation Project" page
    When I play the video
    Then the video should be playing
    When I adjust the volume
    Then the volume should be 50%
    When I change the resolution to "1080p"
    #Then the resolution should be "1080p"
    When Pause and Exit
    Then Logout


'''
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

#from data import loacte, url


#driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome()


@given('I am on the login page')
def step_impl(context):
    # Open the FYC platform
   # driver.get(url['Platform URL'])
   driver.get("https://indeedemo-fyc.watch.indee.tv/")
   time.sleep(3)

@when('I log in using the PIN "{pin}"')
def step_impl(context, pin):
    # Find the PIN input and submit the login form
    pin_input = driver.find_element(By.NAME, "Access Code")
    pin_input.send_keys(pin)
    pin_input.send_keys(Keys.RETURN)
    time.sleep(3)

@then('I should be on the "All Titles" page')
def step_impl(context):
    # Verify that we are on the correct page
    print('Page title ----> ',driver.title)
    assert "Brands | Enterprise test FYC" in driver.title
    time.sleep(3)

@then('I should see the "Test Automation Project"')
def step_impl(context):
    project = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@title='Test automation project']"))
    )
    project.click()
    assert project.is_displayed()

@given(u'I am on the "Test Automation Project" page')
def step_impl(context):
    # Wait for an element on the "Test Automation Project" page to become visible
    project_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Test automation project']"))
    )
    assert project_element.is_displayed()  # Verify the element is visible
    print("Successfully navigated to the Test Automation Project page")



@when('I play the video')
def step_impl(context):

    menubar_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='menubar']"))
    )
    assert menubar_ele.is_displayed()  # Verify the element is visible
    print("Successfully navigated to the menubar element")
   # print(menubar_ele.get_attribute)('outerHTML')

    detailsLabel_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='menubar']"))
    )
    detailsLabel_ele.click()

    videosLabel_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='menubar']"))
    )
    videosLabel_ele.click()

@then('the video should be playing')
def step_impl(context):

    videoPlayButton_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Play Video']"))
    )
    assert videoPlayButton_ele.is_displayed() 
    videoPlayButton_ele.click()

 
    time.sleep(10)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  # Replace with the actual iframe ID or locator
    )
    driver.switch_to.frame(iframe)
    duration = 600 # 600 = 10 sec
    # Now execute the JW Player script
    driver.execute_script(f"jwplayer().seek({duration})"); time.sleep(2)
    print("Video Played at 10 sec")
    driver.switch_to.default_content()

    action = ActionChains(driver)
    action.send_keys(Keys.SPACE).perform(); time.sleep(2)
    print('Video Paused')

    videoContinueButton_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Continue Watching']"))
    )
    assert videoContinueButton_ele.is_displayed(), "Error: 'Continue Watching' button is not visible."
    videoContinueButton_ele.click()
    print('---------> Video continue button is clicked'); time.sleep(2)


@when('I adjust the volume')
def step_impl(context):


    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  # Replace with the actual iframe ID or locator
    )
    driver.switch_to.frame(iframe)

    # Now execute the JW Player script
    driver.execute_script("jwplayer().setMute(true);"); time.sleep(2)
    print("Muted JW Player successfully.")
    driver.switch_to.default_content()


@then('the volume should be {volume}%')
def step_impl(context, volume):
    
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  # Replace with the actual iframe ID or locator
    )
    driver.switch_to.frame(iframe)

    #set volue to 50 percent
    driver.execute_script(f"jwplayer().setVolume({volume});");  time.sleep(2)
    print("Volume set to 50%")
    driver.switch_to.default_content()


@when('I change the resolution to "{resolution}"')
def step_impl(context, resolution):
    action = ActionChains(driver)
    print('resoluton from feature file ---> ',resolution)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  # Replace with the actual iframe ID or locator
    )
    driver.switch_to.frame(iframe)

    #set volue to 50 percent
    driver.execute_script(f"jwplayer().setCurrentQuality({2})");  time.sleep(2)
    print("set resolution to 480p")
    driver.switch_to.default_content()

    

@when('Pause and Exit')
def step_impl(context):
    time.sleep(5)    
    print('---------> Pause and Exit')
    #driver.back()
    action = ActionChains(driver)
    action.send_keys(Keys.SPACE).perform()
    print('---------> Video paused')
    time.sleep(3)    

    backButton_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Go Back and continue playing video']"))
    )
    assert backButton_ele.is_displayed(), "Error: 'Back button is not visible."
    backButton_ele.click()
    
    project_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Test automation project']"))
    )
    assert project_element.is_displayed()  # Verify the element is visible
    print("Successfully navigated to the Test Automation Project page")

@then('Logout')
def step_impl(context):
         
    SideBar_ele = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "SideBar"))
    )
    assert SideBar_ele.is_displayed()  # Verify the element is visible
    print("Side bar is Displayed")

    signOutButton_ele = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "signOutSideBar"))
    )
    assert signOutButton_ele.is_displayed()  # Verify the element is visible
    signOutButton_ele.click()
    print("SignOut")

    SignInForm_ele = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "form-section"))
    )
    assert SignInForm_ele.is_displayed, 'Error: Access Code is not visible.'
    print('Sign Out Done')
