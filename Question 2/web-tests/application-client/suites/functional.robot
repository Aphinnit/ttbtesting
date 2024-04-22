*** Settings ***
| Documentation | TestCases For BPS Application

| Resource  | ../modules/module.robot
| Variables | ../pagelibraries/resources/config.py
| Resource  | utils/common.robot

| Library   | datadrivenlibrary.CsvLibrary
| Library   | utils.generic_keywords
| Resource  | utils/generic-keywords.robot
| Library   | utils.pythonproperty_reader
| Library   | utils.clearcache
| Library   | PageObjectLibrary
| Library   | SeleniumLibrary
| Library   | Collections
| Library   | String


| Test Setup | Setup for Test
| Test Teardown | Teardown for Test
| Suite Teardown | Stop webapp and close all browsers

*** Variables ***
| ${root_url} | ${CONFIG.root_url}

*** Keywords ***
| Stop webapp and close all browsers
| | [Documentation] | Stopping the execution and close/terminate all opened browsers
| | Log | \n... Closing Browser ...\n | console=${True}
| | Close all browsers

| Teardown for Test
| | [Documentation] | On test close Capture the screenshot
| | Run Keyword If Test Failed | Capture Page Screenshot
| | Close Browser 

| Setup for Test
| | [Documentation] | Delete all  cookies and session from browser 
| | Open browser and Navigate to Url

| Clear session for edge
| | [Documentation] | clear session/cookies from edge browser
| | run keyword if | "${BROWSER}" == "edge" | clear_edge_cache

| Clear Session For Firefox
| | [Documentation] | clear session/cookies from firefox browser
| | Run Keyword If | "${BROWSER}" == "firefox" | Clear Firefox Cache

| Open browser and Navigate to Url
| | [Documentation] | Initiate the Suite by opening browser about:blank page
| | ... | and validate all the required pages for execution
| | Open Test Browser | URL=${root_url}
| | Maximize Browser Window
| | run keyword if | "${BROWSER}" == "ie" | Set Selenium Speed | 0.2
| | run keyword if | "${BROWSER}" == "edge" | Set Selenium Speed | 0.2
| | run keyword if | "${BROWSER}" == "safari" | Set Selenium Speed | 0.2
| | Go To Page | loginPage


*** Test Cases ***    

Scenario: Login success
   [Documentation]   _As a test, I want to ensure that users can login successfully 
   ...    when input a correct username and password
   [Tags]  
   When Launch a Website
   Then User LogIn to The Website  signInPage_datasheet  1
   And The Application Should be On logInPage
   And Page Should Contain  You logged into a secure area!
   And user clicks on logout button 
   And The Application Should be On logInPage
   And Page Should Contain  You logged out of the secure area!


Scenario: Login failed - Password incorrect
   [Documentation]   _As a test, I want to ensure that users can login unsuccessfully 
   ...    when they input a correct username but wrong password.
   [Tags]  
   When Launch a Website
   Then User LogIn to The Website  signInPage_datasheet  2
   And The Application Should be On logInPage
   And Page Should Contain  Your password is invalid!

Scenario: Login failed - Username not found
   [Documentation]   _As a test, I want to ensure that users can login unsuccessfully 
   ...    when they input a username that did not exist
   [Tags]  
   When Launch a Website
   Then User LogIn to The Website  signInPage_datasheet  3
   And The Application Should be On logInPage
   And Page Should Contain  Your username is invalid