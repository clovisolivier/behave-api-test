@currency
Feature: Get account stats

  Background:
    Given I clean params in context


  Scenario: Account_id is obligatory
    Given I set "EUR" value in POST param "currency"
      When I call the currency WS
      Then status code should be 400
      And error message should be on "account_id"

  Scenario: Currency is obligatory
    Given I set "221" value in POST param "account_id"
      When I call the currency WS
      Then status code should be 400
      And error message should be on "currency"

    @KO
  Scenario Outline: Change currency and check with stats WS
    Given I set "221" value in POST param "account_id"
      And I set "<currency>" value in POST param "currency"
      When I call the currency WS
      Then status code should be 200
    Given I want to call WS with account_id 221
     And  I want data between "2016-07-01T00:00:00" and "2017-07-01T00:00:00"
      When I call the stats WS
      Then status code should be 200
      And stats currency is "<currency>"

    Examples: Currencies
    |currency|
    |EUR     |
    |USR     |
    |GBP     |
    |NOK     |