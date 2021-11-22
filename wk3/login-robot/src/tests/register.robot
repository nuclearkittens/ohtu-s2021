*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  ville987
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ab  jeejee42
    Output Should Contain  Username has to contain at least 3 characters

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  akuankka  abc123
    Output Should Contain  Password has to contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  mcgarmiwa  KissatOnBest
    Output Should Contain  Password cannot contain only letters
