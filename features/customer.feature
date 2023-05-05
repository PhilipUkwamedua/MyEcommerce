Feature: Customer management

  Scenario: Create a new customer
    Given a new user with the username "testuser" and password "testpass"
    When I create a new customer with the name "Dave Joe" and email "dave.joe@example.com"
    Then the customer should have a user with the username "testuser" and password "testpass"
    And the customer should have the name "Dave Joe"
    And the customer should have the email "dave.joe@example.com"
