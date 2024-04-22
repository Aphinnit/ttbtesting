*** Settings ***
| Documentation | Modular Keywords For Minimal todo application

| Variables | ../pagelibraries/config/config.py
| Resource  | utils/common-mobile.robot
| Library   | AppiumLibrary
| Library   | String
| Library   | OperatingSystem
| Library   | Process
| Library   | ../pagelibraries/resources/registerScreen.py
| Library   | ../pagelibraries/resources/loginScreen.py
| Library   | ../pagelibraries/resources/taskmanagementScreen.py
| Library   | ../pagelibraries/resources/taskdetailScreen.py
| Library   | ../pagelibraries/resources/settingScreen.py


*** Variables ***
| ${pathtocsvfile} | ${CONFIG.path_to_csv_file}


*** Keywords ***
| User Register With Email Address And Password
| | [Documentation] | _This Keyword is going to enter the email_address and password in the respected text box
| | ... | of the SignIn Page Using Through CSV.
| | ... | _Sample Test Data:_ \n\n
| | ... | *filename* _datasheet_ \n\n
| | ... | *row_num* _1_\n\n
| | [Arguments] | ${filename} | ${row_num}
| | &{list} | Read from CSV by Row | ${pathtocsvfile} | ${filename} | ${row_num}
| | User Enters Email Address  | ${list['email_address']}
| | User Enters Password  | ${list['password']}
| | User Clicks On Register Button


 User can Login successfully With Email Address And Password
| | [Documentation] | _This Keyword is going to enter the email_address and password in the respected text box
| | ... | of the SignIn Page Using Through CSV.
| | ... | _Sample Test Data:_ \n\n
| | ... | *filename* _datasheet_ \n\n
| | ... | *row_num* _1_\n\n
| | [Arguments] | ${filename} | ${row_num}
| | &{list} | Read from CSV by Row | ${pathtocsvfile} | ${filename} | ${row_num}
| | User Enters Email Address  | ${list['email_address']}
| | User Enters Password  | ${list['password']}
| | User Clicks On Login Button












