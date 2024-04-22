*** Settings ***
Library           AppiumLibrary
suite setup    Page Navigation

*** Variables ***
${REMOTE_URL}     http://localhost:4723/wd/hub
${PLATFORM_NAME}  Android
${PLATFORM_VERSION}    11
${DEVICE_NAME}    Google_Pixel_3
${APP_PACKAGE}    com.avjindersinghsekhon.minimaltodo
${APP_ACTIVITY}   .MainActivity

*** Keywords ***
Open Application
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    platformVersion=${PLATFORM_VERSION}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}

Page Navigation
Go To Screen  LoginScreen.py
Go To Screen  registerScreen.py
Go To Screen  settingScreen.py
Go To Screen  taskdetailScreen.py
Go To Screen  taskmangementScreen.py

*** Test Cases ***
Scenario: Automate registration process with valid details.
    When Open Application 
    Then User Register With Email Address And Password  signInscreen  1


Scenario:Automate login process with registered credentials.
    When Open Application
    Then User can Login successfully With Email Address And Password  signInscreen  1


Scenrio: Automate error message validation for invalid login attempts
    Given Open Application
    When User can Login successfully With Email Address And Password  signInscreen  1
    Then Page should contain  Invalid login

Scenario:Add New Task and Delete 
    Given Open Application
    When User can Login successfully With Email Address And Password  signInscreen  1
    Then User Add New Task
    And User Deleted the Task

Scenario: Automate successful logout
    Given Open Application
    When User Enter email adderss and password on login screen  signInscreen  1
    Then User logout

    
