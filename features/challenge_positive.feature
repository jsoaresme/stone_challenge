Feature: Scenario Positive

  @positive1
  Scenario: Register only with required fields
    Given load the website for required fields fill
    When fill in the required fields
    Then required fields sent successfully

  @positive2
  Scenario: Fill in successfully
    Given load the website for fill all fields
    When fill all fields
    Then all fields sent successfully

  @positive3
  Scenario: Next questions
    Given load the website for click next questions
    When I go through all the questions
    Then I see the questions available

  @positive4
  Scenario: Access Powered by typeform
    Given load the website for access Powered by typeform
    When I click on Powered by typeform
    Then login page opens

  @positive5
  Scenario: Access Report abuse 
    Given load the website for Access Report abuse 
    When I click on Report abuse
    Then Report abuse page opens