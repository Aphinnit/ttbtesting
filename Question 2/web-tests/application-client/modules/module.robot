*** Settings ***
| Documentation | Modular Keywords For Vnu Web Application.
| Variables | ../pagelibraries/resources/config.py
| Resource  | utils/common.robot
| Library   | utils.generic_keywords
| Library   | ../modules/environmentsetup.py
| Library   | SeleniumLibrary
| Library   | ../pagelibraries/resources/loginPage.py
| Library   | ../pagelibraries/resources/basicPageElement.py


Library    String

*** Variables ***
| @{list}
| ${pathtocsvfile} | ${CONFIG.path_to_csv_file}
| ${protocol}   | ${CONFIG.protocol}
| ${branch}     | ${CONFIG.branch}
| ${cluster_url} | ${CONFIG.cluster_url}



*** Keywords ***

| Launch a Website
| | [Documentation] | _Launch Website and validate user should be on Log in page.
| | Log | \n Loading Website on env ${branch} ... | console=${True}
| | Navigate to application | ${protocol} | ${branch} | ${cluster_url}
| | The Application Should be On logInPage


| User LogIn to The Website
| | [Documentation] | _This Keyword is going to enter the Username and Password in the respected text box
| | ... | of the LogIn Page Using Through CSV.
| | ... | _Sample Test Data:_ \n\n
| | ... | *filename* _datasheet_ \n\n
| | ... | *row_num* _1_\n\n
| | [Arguments] | ${filename} | ${row_num}
| | &{list} | Read from CSV by Row | ${pathtocsvfile} | ${filename} | ${row_num}
| | user enters username  | ${list['username']}
| | user enters password  | ${list['password']}
| | Sleep | 2
| | user clicks on login button