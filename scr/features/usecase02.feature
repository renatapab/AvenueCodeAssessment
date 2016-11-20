# Created by Renata at 20/11/2016
Feature: As a ToDo App user
I should be able to create a subtask
So I can break down my tasks in smaller pieces


  Scenario: Manage Subtasks button is enable
    Given I'm logged in at ave code assessment web site
    When I add a new task
    Then this new task is available at todo list
    And 'Manage Subtask' button is enable to this task

  Scenario: Manage Subtasks button shows the total of subtasks created
    Given I'm logged in at ave code assessment web site
    When I add a new task
    Then I see the number of subtasks created for that tasks

  Scenario: Due date has MM/dd/yyyy format
    Given I'm logged in at ave code assessment web site
    When I click at Manage Subtasks button
    Then I see MM/dd/yyyy format in Due Date field