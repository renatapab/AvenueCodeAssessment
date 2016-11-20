# Created by Renata at 12/11/2016
Feature: US01 - Create Task
  As a ToDo App user
  I should be able to create a task
  So I can manage my tasks

  Scenario: Add a new task by clicking on the add task button
    Given I'm logged in
    When I type a new task
    And press the task button
    Then this new task is added to the to do list

  Scenario: Add a new task by hitting enter
    Given I'm logged in
    When I type a new task
    And press the enter keyboard button
    Then this new task is added to the to do list

  Scenario: Check ‘My Tasks’ link visibility through the hole website
    Given I'm logged in
    When I'm navigatting through the web site
    Then I should be able to see My Task link

  Scenario: Go to to do list clicking on My Task link
    Given I'm logged in
    When I click at My Task link
    Then the web site sends me to the user's To Do list

  Scenario: Check ownership message
    Given I'm logged in
    When I'm at My Task page
    Then I should see a ownership message saying that this list belongs to the logged user

  Scenario: Check ownership message at the top part of the web site
    Given I'm logged in
    When I'm at My Task page
    Then I should see a ownership on the top part saying that list belongs to the logged user

  Scenario: Enter a 2 char task name
    Given I'm logged in
    And I enter a 2 char task name
    When hit enter
    Then the app do not allow this new entrance

  Scenario: Enter a 251 char task name
    Given I'm logged in
    And I enter a 251 char task name
    When I hit enter
    Then the app do not allow this new entrance

  Scenario: The new task added appear at appended list
    Given I'm logged in
    And Add a new task
    When I hit add button
    Then the new task appear at the appended list