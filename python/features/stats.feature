@stats
Feature: Get account stats

  Background:
    Given I clean params in context


  Scenario: Account_id is obligatory
    Given I want data between "2016-07-01T00:00:00" and "2017-07-01T00:00:00"
      When I call the stats WS
      Then status code should be 400
      And error message should be on "account_id"


  Scenario: Date_to is obligatory
    Given I want to set "1992" in param "account_id"
      And I want data after "2016-07-01T00:00:00"
      When I call the stats WS
      Then status code should be 400
      And error message should be on "date_to"


  Scenario: Date_from is obligatory
    Given I want to call WS with account_id 1992
      And I want data before "2017-07-01T00:00:00"
      When I call the stats WS
      Then status code should be 400
      And error message should be on "date_from"

    #Code error pas bon
  @KO
  Scenario: account without stats for the interval
    Given I want to call WS with account_id 1992
     And  I want data between "2016-07-01T00:00:00" and "2017-07-01T00:00:00"
      When I call the stats WS
      Then status code should be 204


  Scenario: Validate response format
    Given I want to call WS with account_id 221
     And  I want data between "2016-07-01T00:00:00" and "2017-07-01T00:00:00"
      When I call the stats WS
      Then status code should be 200
      And stats result is contains all needed fields