Feature: Word to Pdf conversion
  Scenario: To Convert word file to pdf
    Given The User is already on the pdf conversion page
    When User successfully lands on the page
    Then User uploads the word document to be converted
    And User clicks on the upload button
    And User recieves the link to the converted pdf file
    Then User clicks on the link and downloads the converted file

  Scenario Outline: To login to outlook and send the converted file across
    Given User is already on the outlook website
    Then User clicks on the login from navigation links
    And User lands on a page to enter email
    Then User enters the email address into the email field <email>
    And User clicks on the Next Button
    Then User lands on the page to enter password
    And User enters the password <password>
    And Clicks on the next button
    Then User gets a popup to stay signed in and user sets value to Yes by clicking it
    And User lands on the home page of oulook
    Then User clicks on New email button
    And User clicks on attach browsers a file and attaches the file
    And User enters the value in to field <to>
    And User clicks on cc button
    And User enters value in cc field <cc>
    And User clicks on Bcc field
    And User sends value into Bcc field <bcc>
    And User enters the subject
    And User enters the message into textbox
    Then User clicks on send to send an email




    Examples:
    | email | password | to | cc | bcc |
    | darshanmesta47@hotmail.com | DbossKA47@ | darshanmesta33@gmail.com | surajmesta47@gmail.com | darshanmesta47@hotmail.com|
