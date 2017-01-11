@currency
Feature: Get account stats

  Background:
    Given I clean params in context


  Scenario: Account_id is obligatory
    Given I set "EUR" value in POST param "currency"
      When I call the currency WS
      Then status code should be 400
      And error message should be on "account_id"
