Feature: Login

  @logout
  Scenario: Success login
    Given I am on "login" page
    When I ingress credentials
    Then I can see the user on home page
    And I validate home page elements


  @login
  Scenario: Success logout
    Given I am on "/" page
    When I logout
    Then I should see the landing page
