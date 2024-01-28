# Testing

## Table of contents

1. [Introduction](#introduction)
2. [UX](#ux)
    1. [User Stories](#user-stories)
    2. [Design Thinking](#design-thinking)
    3. [Intuitive Design](#intuitive-design)
    4. [Database Design](#database-design)
3. [Features](#features)
    1. [The Landing Page](#the-landing-page)
    2. [Main Page Content](#main-page-content)


## Introduction

In order to ensure that the project is executed according to the plan, a comprehensive set of tests were conducted to achieve the desired objectives. The tests were aimed at assessing the functionality, performance and reliability of the project, and to identify any issues that could potentially impact its success. The results of the tests were carefully analyzed and used to refine the project plan.

## Manual Testing

### 1. Deployed website is working

To ensure the live project works properly, I followed all the steps that were provided by the Code Institute course. These steps are well documented in the latter sections of the [Deployment](deployment.md).

### 2. Site opens on the homepage

To ensure that the deployed site opens on the homepage, it was created a function-based view in the restaurant app and added a path in the URL file of the restaurant app. Then, referenced the restaurant app URL in the it_project URL file.

- **restaurant/views.py:**

![Test 1](static/readme/testing/tt1.jpg)


- **restaurant/urls.py:**

![Test 2](static/readme/testing/tt2.jpg)

- **it_project/urls.py:**

![Test 3](static/readme/testing/tt3.jpg)

- **browser**

![Test 4](static/readme/testing/tt4.jpg)

### 3. CSS file is conected

Ensure that my own css and js files are linked correctly to base.html via head.html and scripts.html. These component files are inserted to base.html using Django Templates.

- **Created my own file CSS**

![Test 5](static/readme/testing/tt5.jpg)

- **Linked on base.html**

![Test 6](static/readme/testing/tt6.jpg)

- **Added on the top of base.html**

![Test 7](static/readme/testing/tt7.jpg)

- **Created static/js**

![Test 8](static/readme/testing/tt8.jpg)

- **Added script.js on base.html**

![Test 9](static/readme/testing/tt9.jpg)

- **Added Bootstrap on base.html**

![Test 11](static/readme/testing/tt11.jpg)

![Test 10](static/readme/testing/tt10.jpg)