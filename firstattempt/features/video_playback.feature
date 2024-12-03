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
    When Pause and Exit
    Then Logout

