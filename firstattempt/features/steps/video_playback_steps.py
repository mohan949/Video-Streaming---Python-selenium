import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

@given('I am on the login page')
def step_impl(context):
   driver.get("https://indeedemo-fyc.watch.indee.tv/")  # Navigate to the FYC platform login page

@when('I log in using the PIN "{pin}"')
def step_impl(context, pin):       # Find the PIN input and submit the login form
    pin_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "Access Code"))
    )
    pin_input = driver.find_element(By.NAME, "Access Code")
    pin_input.send_keys(pin)
    pin_input.send_keys(Keys.RETURN)

@then('I should be on the "All Titles" page')
def step_impl(context):
     # Wait until the page title includes the expected text
    WebDriverWait(driver, 10).until(
        lambda driver: "Brands | Enterprise test FYC" in driver.title
    )
    # Print and assert the page title to confirm successful navigation
    print('Page title ----> ', driver.title)
    assert "Brands | Enterprise test FYC" in driver.title
    

@then('I should see the "Test Automation Project"')
def step_impl(context):
    # Wait for the "Test Automation Project" element to be visible
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
    # Wait for the menubar element to be visible
    menubar_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='menubar']"))
    )
    assert menubar_ele.is_displayed()  
    print("Successfully navigated to the menubar element")
    # Click on the 'details' section label
    detailsLabel_ele =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='detailsSection']"))
    )
    detailsLabel_ele.click()
    # Click on the 'video' section label
    videosLabel_ele =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='videosSection']"))
    )
    videosLabel_ele.click()
    time.sleep(2) # Wait for 2 seconds for the video to load

@then('the video should be playing')
def step_impl(context):
     # Wait for the 'Play Video' button to be clickable
    videoPlayButton_ele =  WebDriverWait(driver, 30 ).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play Video']"))
    )
    assert videoPlayButton_ele.is_displayed() 
    videoPlayButton_ele.click()

    iframe = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "video_player"))  
    )
    driver.switch_to.frame(iframe)
    duration = 600 # 600 = 10 sec
    # Now execute the JW Player script
    driver.execute_script(f"jwplayer().seek({duration})"); time.sleep(2)  # Wait for the video to seek
   
    print("Video Played at 10 sec")
    driver.switch_to.default_content()

    action = ActionChains(driver)
    action.send_keys(Keys.SPACE).perform(); 
    print('Video Paused')

    videoContinueButton_ele =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue Watching']"))
    )
    assert videoContinueButton_ele.is_displayed(), "Error: 'Continue Watching' button is not visible."
    videoContinueButton_ele.click() # Click the 'Continue Watching' button
    print('---------> Video continue button is clicked'); time.sleep(2)

@when('I adjust the volume')
def step_impl(context):
    # Switch to the iframe where the video player is located
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  
    )
    driver.switch_to.frame(iframe)

    # Now execute the JW Player script
    driver.execute_script("jwplayer().setMute(true);"); time.sleep(2)
    print("Muted JW Player successfully.")
    driver.switch_to.default_content()

@then('the volume should be {volume}%')
def step_impl(context, volume):
    
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  
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
        EC.presence_of_element_located((By.ID, "video_player"))  
    )
    driver.switch_to.frame(iframe)

     # Change the video resolution to the specified quality (e.g., 480p)
    driver.execute_script(f"jwplayer().setCurrentQuality({2})");  time.sleep(2)
    print("set resolution to 480p")
    driver.switch_to.default_content()
 
@when('Pause and Exit')
def step_impl(context):
    
    iframe = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "video_player"))  
    )
    driver.switch_to.frame(iframe)
    # Now execute the JW Player script
    driver.execute_script(f"jwplayer().pause()"); time.sleep(2)
    print("video pause")
    driver.switch_to.default_content()
 
    backButton_ele =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go Back and continue playing video']"))
    )
    assert backButton_ele.is_displayed(), "Error: 'Back button is not visible."
    backButton_ele.click()

    # Verify that the "Test Automation Project" page is displayed after going back
    project_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Test automation project']"))
    )
    assert project_element.is_displayed()  # Verify the element is visible
    print("Successfully navigated to the Test Automation Project page")

@then('Logout')
def step_impl(context):
    # Wait for the sidebar to be visible
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
    # Wait for the 'Sign Out' button to be visible
    SignInForm_ele = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "form-section"))
    )
    assert SignInForm_ele.is_displayed, 'Error: Access Code is not visible.'
    print('Sign Out Done')
