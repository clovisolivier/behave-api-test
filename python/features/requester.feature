Feature: showing off behave

  Scenario: Weather request status
     Given we call the weather API for London
      then status code should be 401

  @ignore
  Scenario: Weather request status
     Given we call the weather API for Paris
      then status code should be 401
