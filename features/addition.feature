Feature: Addition API

  Scenario: Add two numbers
    Given the application is running
    When I send a request to add 1 and 2
    Then I receive a response with the result 3

  Scenario: Missing parameters
    Given the application is running
    When I send a request to add 1 and no second number
    Then I receive a 400 error
