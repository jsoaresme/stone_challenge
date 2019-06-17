Feature: Scenario Negative

  @negative1
  Scenario: Register without filling in required fields
    Given load the website for register without filling in required fields
    When I click Register without filling fields
    Then I see the error message

  @negative2
  Scenario: Fill in wrong email
    Given load the website for fill in wrong email
    When fill in wrong email
    Then I see the error message about in wrong email

  @negative3
  Scenario: Fill in wrong filds born
    Given load the website for fill in wrong filds born
    When fill in wrong filds born
    Then I see the error message about in wrong filds born