# Testing

## Table of contents

1. [Introduction](#introduction)
2. [Manual Testing](#manual-testing)
    1. [Deployed website is working](#deployed-website-is-working)
    2. [Site opens on the homepage](#site-opens-on-the-homepage)
    3. [CSS file is conected](#css-file-is-conected)
    4. [base.html is linked](#base.html-is-linked)
    5. [Load index.html and base.html](#load-index.html-and-base.html)
    6. [Check allauth working](#check-allauth-working)
    7. [Create and Migrate a Module](#create-and-migrate-a-module)
    8. [Buttons and Links](#buttons-and-links)
    9. [Sign In, Edit, Cancel and Sign Out](#sign-In,-edit,-cancel-and-sign-out)
3. [Validation](#validation)
4. [Lighthouse](#lighthouse)
5. [Browsers](#browsers)


## Introduction

In order to ensure that the project is executed according to the plan, a comprehensive set of tests were conducted to achieve the desired objectives. The tests were aimed at assessing the functionality, performance and reliability of the project, and to identify any issues that could potentially impact its success. The results of the tests were carefully analyzed and used to refine the project plan.

## Manual Testing

### 1. Deployed website is working

To ensure the live project works properly, I followed all the steps that were provided by the Code Institute course. These steps are well documented in the latter sections of the [Deployment](deployment.md).

[Back to top](#testing)

### 2. Site opens on the homepage

To ensure that the deployed site opens on the homepage, it was created a function-based view in the restaurant app and added a path in the URL file of the restaurant app. Then, referenced the restaurant app URL in the it_project URL file.

- **restaurant/views.py:**

![Test 1](static/readme/testing/tt1.jpg)


- **restaurant/urls.py:**

![Test 2](static/readme/testing/tt2.jpg)

- **it_project/urls.py:**

![Test 3](static/readme/testing/tt3.jpg)

- **browser**

![Test 4](static/readme/testing/tt4-1.jpg)

[Back to top](#testing)

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

[Back to top](#testing)

- **Collectstatic**

I included django.contrib.staticfiles in my INSTALLED_APPS in Setting. And Added:

![Test 13](static/readme/testing/tt13.jpg)

On the Terminal I imput the command **python3 manage.py collectstatic**


- **Deleted DISABLE_COLLECTSTATIC**

I excluded DISABLE_COLLECTSTATIC on Heroku's Config Vars. I used the command to push to GitHub and everything was working. 

![Test 12](static/readme/testing/tt12.jpg)

[Back to top](#testing)

### 4. base.html is linked

The main content is in *restaurant/template/restaurant/index.html*, and to ensure that base.html is included on index.html and in all the others html files, it is added on the top of the html files:

![Test 14](static/readme/testing/tt14.jpg)

Following the *{% endblock %}* in the end of the page content.

### 5. Load index.html and base.html

After everything is connected the page loads normally:

![GIF 1](static/readme/testing/gifs/gif1.gif)

### 6. Check allauth working

Allauth handled signup/login/logout. If User is not authenticated the Sign In and Sign up button will apper.

![GIF 2](static/readme/testing/gifs/gif2.gif)

If the user is authenticated, their personal pages will be displayed instead of Sign In/Sign Up page.

If User is not authenticated, They can Sign Up or Sign In:

![GIF 3](static/readme/testing/gifs/gif3.gif).

The authentication can be cheked on *reservatios/template/reservations/view_reservations.html:

![Test 15](static/readme/testing/tt15.jpg)

It is possible to check the resistration on *admin/* as well.

[Back to top](#testing)

### 7. Create and Migrate a Module

- Type *python3 manage.py makemigrations --dry-run* to view unexecuted effect. These are the instructions to build a table.
- Remove the  *--dry-run* flag to perform the action.
- Use the *python3 manage.py showmigrations* command to see a list of existing migrations.
- To build the table in the backend type *python3 manage.py migrate* into the terminal.

The model must be registered within the apps admin file:

![Test 17](static/readme/testing/tt17.jpg)

![Test 16](static/readme/testing/tt16.png)

How Profile is a different table to User, it was added to the top of the models file *import post_save and reciever*:

![Test 18](static/readme/testing/tt18.png)

[Back to top](#testing)

### 8. Buttons and Links

All buttons and links are working:

- Reservations buttons:

![GIF Reservations](static/readme/testing/gifs/reservation-button.gif)

- Reservations buttons:

![Menu](static/readme/testing/gifs/menu.gif)

### 9. Sign In, Edit, Cancel and Sign Out

- Once a user is signed in, they are authorized to access the booking system. As a result, they can see **only** their own name, but they also have the ability to view other bookings date and time of the reservation, as well as the number of people who will be attending.

![GIF Sign In](static/readme/testing/gifs/signin.gif)

- The Edit button and cancel Model is working as well:

![GIF Edit/Cancel](static/readme/testing/gifs/edit-cancel.gif)

- The Sign Out Button tested too:

![GIF Sign Out](static/readme/testing/gifs/signout.gif)

[Back to top](#testing)

## Validation

Passed in all validators below:

### HTML Validation

[W3C Markup Validator](https://validator.w3.org/)

![W3C Markup Validator](static/readme/testing/html-validator.jpg "W3C Markup Validator")


### CSS Validation

[Jigsaw](https://jigsaw.w3.org/css-validator/)  

![Jigsaw](static/readme/testing/css-valid.jpg "Jigsaw Validator")


### JS Validation

[JSHint](https://jshint.com/) 

![Jshint](static/readme/testing/jshint.jpg "Jshint Validator")

### Python Validation

[PEP8](https://extendsclass.com/python-tester.html/ "Python Validator")

Tested all Python codes and all of them passed:

![PEP8](static/readme/testing/python-validator.jpg "Python Validator")

[Back to top](#testing)

## Lighthouse

![Lighthouse](static/readme/testing/lighthouse.png)

## Browsers

- Chrome:

![Chrome](static/readme/testing/chrome.jpg)

- Edge:

![Edge](static/readme/testing/edge.jpg)

- Firefox:

![Firefox](static/readme/testing/firefox.jpg)

- Opera:

![Opera](static/readme/testing/opera.jpg)

[Back to top](#testing)

Back to Readme file [README.md](README.md)

