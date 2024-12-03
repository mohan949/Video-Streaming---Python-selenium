from behave import *
from selenium import webdriver
#from ..Pages.Loginpage import LoginPage
from Pages.Loginpage import LoginPage
from Pages.Tittlespage import AllTitlesPage
from Pages.Projectpage import ProjectPage
from Pages.Videopage import VideoPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys





driver = webdriver.Chrome()


import time

@given('I am on the login page')
def step_impl(context):
    context.driver = driver
    context.driver.get("https://indeedemo-fyc.watch.indee.tv/")
    context.login_page = LoginPage(context.driver)

@when('I log in using the PIN "{pin}"')
def step_impl(context, pin):
    context.login_page.login(pin)

@then('I should be on the "All Titles" page')
def step_impl(context):
    #assert "Brands | Enterprise test FYC" in context.driver.title
    print(driver.title)
    assert "Brands | Enterprise test FYC" in driver.title
    context.all_titles_page = AllTitlesPage(context.driver)
    context.all_titles_page.select_project()


@then('I should see the "Test Automation Project"')
def step_impl(context):

    
    menubar_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='menubar']"))
    )
    assert menubar_ele.is_displayed()  # Verify the element is visible
    print("Successfully navigated to the menubar element")
   # print(menubar_ele.get_attribute)('outerHTML')
    context.all_titles_page = AllTitlesPage(context.driver)
    context.all_titles_page.verifytitle()

@given(u'I am on the "Test Automation Project" page')
def step_impl(context):
    # context.project_page = ProjectPage(context.driver)
    # context.project_page.switch_to_details_tab()
    # context.project_page.switch_to_videos_tab()

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



@when('I play the video')
def step_impl(context):
    # context.video_page = VideoPage(context.driver)
    # context.video_page.play_video()


    videoPlayButton_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Play Video']"))
    )
    assert videoPlayButton_ele.is_displayed() 
    videoPlayButton_ele.click()

 
#    time.sleep(10)
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



@then('the video should be playing')
def step_impl(context):
    
    # time.sleep(10)
    # context.video_page.pause_video()


    videoPlayButton_ele =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Play Video']"))
    )
    assert videoPlayButton_ele.is_displayed() 
    videoPlayButton_ele.click()

 
    time.sleep(10)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  #  iframe ID or locator
    )
    driver.switch_to.frame(iframe)
    duration = 600 # 600 = 10 sec
    #  JW Player script
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


@then('I adjust the volume to {volume}%')
def step_impl(context, volume):
    # context.video_page.adjust_volume(volume)


    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  #iframe ID or locator
    )
    driver.switch_to.frame(iframe)

    # Now execute the JW Player script
    driver.execute_script("jwplayer().setMute(true);"); time.sleep(2)
    print("Muted JW Player successfully.")
    driver.switch_to.default_content()



@when('I change the video resolution to "{resolution}"')
def step_impl(context, resolution):
    # context.video_page.change_resolution(resolution)
    action = ActionChains(driver)
    print('resoluton from feature file ---> ',resolution)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video_player"))  #iframe ID or locator
    )
    driver.switch_to.frame(iframe)

    #set volue to 50 percent
    driver.execute_script(f"jwplayer().setCurrentQuality({2})");  time.sleep(2)
    print("set resolution to 480p")
    driver.switch_to.default_content()


@when('Pause and Exit')
def step_impl(context):
    # context.video_page.pause_video()
    # context.driver.back()

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
    # logout_button = context.driver.find_element(By.ID, "signOutSideBar")
    # logout_button.click()
    # assert "Access Code" in context.driver.page_source

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

