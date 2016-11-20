# Created by Renata at 12/11/2016
Feature: US01 - Create Task
  As a ToDo App user
  I should be able to create a task
  So I can manage my tasks

  Scenario: Adding a 2 char task name
    Given I'm logged in at ave code assessment web site
    When I type an invalid task name with 2 chars
    And press add button
    Then this new entrance do not appear at to do list appending

  Scenario: Adding a 251 char task name
    Given I'm logged in at ave code assessment web site
    When I type an invalid task name with 251 chars
    And press add button
    Then this new entrance do not appear at to do list appending


  Scenario: Add a new task by clicking on the add button
    Given I'm logged in at ave code assessment web site
    When I type a new task
    And press add button
    Then this new task entrance is added to the to do list

  Scenario: Add a new task by hitting enter
    Given I'm logged in at ave code assessment web site
    When I type a new task
    And press the enter keyboard button
    Then this new task entrance is added to the to do list

  Scenario: ‘My Tasks’ link is visible through the website
    Given I'm logged in at ave code assessment web site
    When I'm navigatting at the web site
    Then I should be able to see My Task link button

  Scenario: Click on My Task link button
    Given I'm logged in at ave code assessment web site
    When I click at My Task link button
    Then the website sends me to the renata's To Do list

  Scenario: Ownership message is enable
    Given I'm logged in at ave code assessment web site
    When I click at My Task link button
    Then I should see an ownership message saying that this list belongs to the logged user
    And this message is on the top part of the website
