Feature: showing off behave

  Scenario Outline: Use Calculator with <thing>
    Given I put "<thing>" in a calculate
    When I switch the calculate on
    Then it should transform into "<other thing>"

    Examples: Amphibians
        | thing         | other thing |
        | 1             | 1           |
        | 2             | 4           |

    Examples: Consumer Electronics
        | thing         | other thing |
        | 4             | 16          |
        | 5             | 25          |