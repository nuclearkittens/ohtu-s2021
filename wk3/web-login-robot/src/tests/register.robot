*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App and Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Choose Username  kalle
    Choose Password  kalle123
    Confirm Password  kalle123
    Register New User
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Choose Username  my
    Choose Password  muumitbest621
    Confirm Password  muumitbest621
    Register New User
    Registering Should Fail With Message  Username has to contain at least 3 characters

Register With Valid Username And Too Short Password
    Choose Username  nuuskis
    Choose Password  teltta1
    Confirm Password  teltta1
    Register New User
    Registering Should Fail With Message  Password has to contain at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Choose Username  nipsu
    Choose Password  muumitbest666
    Confirm Password  muumitbest621
    Register New User
    Registering Should Fail With Message  Password confirmation does not match password

*** Keywords ***
Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register New User
    Click Button  Register

Choose Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Choose Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset App and Go To Register Page
    Reset Application
    Go To Register Page
