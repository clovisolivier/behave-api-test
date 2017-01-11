@has_stats
Feature: show if an account has stats

  Background:
    Given I clean params in context

  Scenario: Account ID is obligatory
    Given I want data between "2016-07-01T00:00:00" and "2017-07-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 400
      And error message should be on "account_id"

  Scenario: Date_from is optional
    Given  I want to call WS with account_id 1984
      And I want data after "2016-07-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200

  Scenario: Date_to is optional
    Given  I want to call WS with account_id 1984
      And I want data before "2016-07-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200

  Scenario: Get indication on an account without stat
    Given  I want to call WS with account_id 1984
      And I want data between "2016-07-01T00:00:00" and "2016-12-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200
      And this account has no stat

  Scenario: Get indication on an account with stat
    Given  I want to call WS with account_id 221
      When I call the stats API has_stat
      Then status code should be 200
      And this account has stat

    @KO
  Scenario: Get indication on an account without stat between dates
     Given  I want to call WS with account_id 221
      And I want data between "2016-12-01T00:00:00" and "2016-12-30T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200
      And this account has no stat

  Scenario: Get indication on an account with stat before
     Given  I want to call WS with account_id 221
      And I want data before "2016-09-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200
      And this account has stat

   @KO
  Scenario: Get indication on an account without stat before
     Given  I want to call WS with account_id 221
      And I want data before "2016-06-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200
      And this account has no stat


  Scenario: Get indication on an account with stat after
     Given  I want to call WS with account_id 221
      And I want data before "2016-06-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200
      And this account has stat

   @KO
  Scenario: Get indication on an account without stat after
     Given  I want to call WS with account_id 221
      And I want data before "2016-09-01T00:00:00"
      When I call the stats API has_stat
      Then status code should be 200
      And this account has no stat