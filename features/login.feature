Feature: Login

  Scenario: Success login
    Given I am on login page
    When I ingress credentials
    Then I can see the user on home page
    And I validate home page elements
