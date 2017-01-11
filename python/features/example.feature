@currency
Feature: Get account stats

  Background:
    Given I clean params in context


  Scenario: Account_id is obligatory
    Given I want to set "London" in param "q"
      When I call the example WS
      Then status code should be 401
