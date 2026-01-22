Feature: Board

  @login
  Scenario: Create a single board
    When I create a single board
    And I am redirected to the Board
    Then I can see the boards elements
    And I could create a ticked
