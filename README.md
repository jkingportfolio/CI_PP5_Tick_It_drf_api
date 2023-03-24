# Tick It API in DRF

**Developer: Jamie King**

💻 [Live link](https://tick-it-pp5.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the Tick It front-end application ([repository here](https://github.com/jkingportfolio/ci_pp5_tick_it_react) and [live website here](https://tick-it-app-pp5.herokuapp.com/)

## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Credits](#credits)

## User Stories

The back-end section of the project focuses on its administration side and covers one user story:
- As an admin, I want to be able to create, edit and delete users, tasks, packs, comments and watches, so that I can have control over the content of the application and also remove any potential inappropriate content.


## Database

The following models were created to represent the database model structure of the application:
<img src="docs/readme/database-diagram.png">

#### User Model

- The User model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with 
- ForeignKey relation with 


#### Profile Model

- The Profile model contains the following fields: owner, xx, xx and xxx
- One-to-one relation between the xx and xx

#### Task Model

- The Task model contains the following fields: owner, xx, xx and xx
- ForeignKey relation with the xx
- ForeignKey relation with the xx

#### Watch Model

- The Watch model contains the following fields: owner, xx and xx
- ForeignKey relation between the xx and xx
- ForeignKey relation between the xx and xx

#### Comment Model

- The Comment model contains the following fields: xx, xx and xx
- ForeignKey relation between the xx and xx
- ForeignKey relation between the xx and xx

#### Pack Model

- The Pack model contains the following fields: xx, xx and xx
- ForeignKey relation between to the xx and xx
- ForeignKey relation between the xx and xx
- ForeignKey relation between the xx and xx

##### Back to [top](#table-of-contents)


## Technologies Used

### Languages & Frameworks

- Python
- Django

### Libraries & Tools

- [TOOL NAME](LINK) - DESCRIPTION

##### Back to [top](#table-of-contents)


## Validation

### Python Validation

PEP8 was unavailable so used pycodestyle etc

[Pycodestyle](LINK) - Description


## Testing

The following tests were carried out on the app:
1. Manual testing of user stories
2. Automated testing

### Manual testing of user stories

- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Task | Create, update & delete | A Task can be created, edited or deleted | Works as expected
Comment | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Watch | Create & delete | xxxxxxxxxxxxxxxxx | Works as expected
Pack | Create & delete | xxxxxxxxxxxr | Works as expected

In addition, tasks, comments, packs and watches can be created by logged-in users only. Users can only update or delete the content which was created by themselves.

<details><summary>Screenshots - USER</summary>
    <details><summary>Create user</summary>
    <img src="docs/testing/user-create-test.png">
    </details>
    <details><summary>Change user permissions</summary>
    <img src="docs/testing/user-change-permissions-test.png">
    </details>
</details>

<details><summary>Screenshots - PROFILE</summary>
    <details><summary>Update profile</summary>
    <img src="docs/testing/profile-update-test.png">
    </details>
        <details><summary>Delete profile</summary>
    <img src="docs/testing/profile-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - TASK</summary>
    <details><summary>Create task</summary>
    <img src="docs/testing/task-create-test.png">
    </details>
    <details><summary>Update task</summary>
    <img src="docs/testing/task-update-test.png">
    </details>
    <details><summary>Delete task</summary>
    <img src="docs/testing/task-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - COMMENT</summary>
    <details><summary>Create comment</summary>
    <img src="docs/testing/comment-create-test.png">
    </details>
    <details><summary>Update comment</summary>
    <img src="docs/testing/comment-update-test.png">
    </details>
    <details><summary>Delete comment</summary>
    <img src="docs/testing/comment-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - PACK</summary>
    <details><summary>Create pack</summary>
    <img src="docs/testing/pack-create-test.png">
    </details>
    <details><summary>Delete pack</summary>
    <img src="docs/testing/pack-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - WATCH</summary>
    <details><summary>Create - Watch Task</summary>
    <img src="docs/testing/watch-create-test.png">
    </details>
    <details><summary>Delete - UnWatch Task</summary>
    <img src="docs/testing/watch-delete-test.png">
    </details>
</details>


### Automated testing

Automated testing was done using the Django Rest Framework APITestCase. The report of overall testing was produced using the coverage tool (```$ coverage report``` & ```$ coverage html``` commands)

- Tests summary

<img src="docs/testing/apitestcase-tickit.png">

<details><summary>Detailed coverage report</summary>
<img src="docs/testing/coverage-report-tickit.jpg">
</details>

##### Back to [top](#table-of-contents)


## Credits


### Code

This project was created based on the Code Institute's Django REST API walkthrough project ['Moments'](https://github.com/Code-Institute-Solutions/drf-api).

##### Back to [top](#table-of-contents)