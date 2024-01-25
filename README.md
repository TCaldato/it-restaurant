- **Readme still in development**

# IT Restaurant

Step into the heart of Italy with our Italian restaurant website, a digital showcase of culinary excellence crafted using HTML, CSS, JS, and Python with the power of Django and Bootstrap frameworks. Immerse yourself in the flavors of Italy as you navigate through a visually stunning and user-friendly interface, mirroring the warmth of Italian hospitality. Explore our menu and experience the fusion of technology and tradition, all at your fingertips. Buon appetito!

![mock-up images](---- "Website preview at different resolutions")

[View the live project here](https://it-restaurant-42ee32c14928.herokuapp.com/)

## Table of contents

1. [Introduction](#introduction)
    1. [About the Project IT Restaurant](#about-the-project-it-restaurant)
2. [UX](#ux)
    1. [User Stories](#user-stories)
    2. [Design Thinking](#design-thinking)
    3. [Intuitive Design](#intuitive-design)
    4. [Database Design](#database-design)
3. [Features](#features)
    1. [Data Model](#data-model)
    2. [Existing Features](#existing-features)
    3. [Input validation and error-checking](#input-validation-and-error-checking)
    4. [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
5. [Testing](#testing)
    1. [Validator Testing](#validator-testing)
    2. [Bugs](#bugs)
        - [Solved Bugs](#solved-bugs)
        - [Remaining Bugs](#remaining-bugs)
6. [Deployment](#deployment)
    1. [Deploying on GitHub Pages](#deploying-on-github-pages)
    2. [GitHub Forking and Cloning](#github-forking-and-cloning)
    3. [Deploying on Heroku](#deploying-on-heroku)
7. [Credits](#credits)
    1. [Code](#code)
8. [Acknowledgements](#acknowledgements)

# Introduction

## About the Project IT Restaurant

A Full-Stack website was developed for this project, which utilizes business logic to manage a centralized dataset. A role-based access authentication mechanism was implemented to ensure secure access to the website's data. The website was built using a combination of HTML, CSS, JavaScript, Python, and the Django and Bootstrap frameworks, with Postgres serving as the relational database. An Agile approach was employed throughout the project. The project also involved the implementation of authorization, authentication, and permission features in a Full-Stack web application solution. Furthermore, the project utilized object-based software concepts to achieve its goals.

## UX

### User-Stories

In the Agile approach, a "user story" is a technique that assists in capturing the user's perspective and needs. It is a simple, yet powerful tool that shifts the focus from documenting requirements to discussing them. A user story is a brief, informal description from a user's point of view that explains what they want to achieve with the product. It encourages collaboration between the development team and the user, as it sparks meaningful conversations about the features and functionality that the user story represents. This approach promotes a better understanding of the user's needs, resulting in a product that meets their requirements and delivers value to the user.

The Agile User Story technique has been documented in a separate file. You can check by on [Agile file](AGILE.md)

### Design Thinking

In order to optimize user experience on the developed website, it is important to apply a Design Thinking approach to determine the most useful features. However, given the time constraints of a hard deadline, it is necessary to assess the feasibility of a student developer delivering prioritized features. It is worth mentioning that the project must incorporate CRUD functionality, as per the assessment criteria, which provides a broad outline of the fundamental requirements.

During a preliminary brainstorming session, a few ideas were suggested to enhance the website's user experience:

| Feature                                 | Importance | Feasibility |
|:----------------------------------------|:----------:|:-----------:|
| Create personal account                 | 5          | 5           |
| Update account information              | 5          | 5           |
| Make an appointment                     | 5          | 5           |
| Review latest appointment date/time     | 3          | 4           |
| Able to change/cancel an appointment    | 3          | 4           |
| Send client booking detail via email    | 2          | 2           |
| View history of all appointments made   | 2          | 3           |
| Owner has a view of reservations made   | 4          | 4           |
| **Overall Score**                       | **29**     | **32**      |

The analysis of the feasibility and importance scores indicates that the project is both practically achievable and highly valuable. Therefore, based on the data, the project is deliverable.

### Intuitive Design

The primary objective was to develop a restaurant website that is easy to use and navigate. To achieve this, several crucial factors were taken into account. 

Firstly, it was essential to choose an attractive layout that is simple to navigate. One approach used was to keep the navigation bar at the top of the page, where it can be easily accessed by users. Additionally, all pages and buttons were labeled with clear and concise titles that accurately describe their content. For instance, "Home," "Menu," and "Reservations." 

Another key aspect to consider is consistency in the website's design across all pages. This was achieved by maintaining the same font, color scheme, and size throughout the entire site. By keeping a consistent design, a cohesive and intuitive website was created that is easy for users to comprehend and navigate. 

Finally, the website was optimized for different devices, including desktops, laptops, tablets, and smartphones. This was accomplished using responsive design techniques that automatically adjust the website's layout depending on the user's device. By optimizing the website for various devices, a seamless user experience was provided to all visitors, regardless of the platform they use.

### Database Design

-----------------------------------

[Back to top](#it-restaurant)

## Features

### Existing Features

Landing Page

#### Remaining Bugs

- There are no remaining bugs found.

[Back to top](#it-restaurant)

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wikipedia")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wikipedia")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wikipedia")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JS Wikipedia")

### Frameworks, Libraries & Programs Used

- [GitHub](https://github.com/)
- [Heroku](https://id.heroku.com/)
- [Python3 ](https://docs.python.org/3/) with the following modules:
     - asgiref==3.7.2
     - backports.zoneinfo==0.2.1;python_version<"3.9"
     - dj-database-url==2.1.0
     - Django==5.0.1
     - django-allauth==0.59.0
     - django-summernote==0.8.20.0
     - gunicorn==20.1.0
     - oauthlib==3.2.0
     - psycopg2==2.9.6
     - PyJWT==2.3.0
     - python3-openid==3.2.0
     - requests-oauthlib==1.3.1
     - whitenoise==6.6.0
     - sqlparse==0.4.4
- [Bootstrap](https://getbootstrap.com/)
- [JQuery](https://jquery.com/) 
- [Django](https://www.djangoproject.com/)
- [Django Templating](https://docs.djangoproject.com/en/4.0/ref/templates/language/)
- [PostgreSQL](https://www.postgresql.org/)
- [Font Awesome](https://fontawesome.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [W3C Markup Validator](https://validator.w3.org/)
- [Jigsaw](https://jigsaw.w3.org/css-validator/)
- [JSHint](https://jshint.com/)
- [PEP8](https://www.pythonchecker.com/)

## Testing

This process has been documented separately in [Testing](testing.md)


## Deployment

The site was deployed early closely following Code Institute guides.

This process has been documented separately in [deployment.md](deployment.md)


## Credits

 - Using Multiple Database Tables With Django - CodeMy.com

[Back to top](#it-restaurant)


### Code

Various sources were consulted to gain a better understanding of the code being implemented. The following sites were most frequently utilized:

- [Stack Overflow](https://stackoverflow.com/) - Link to Stack Overflow page.
- [W3Schools](https://www.w3schools.com/) - Link to W3Schools page.
- [Heroku](https://p3-battleships.herokuapp.com/) - Link to Code Institute game on Heroku.
- [Python Package Index](https://pypi.org/) - Link to Python Package Index page.
- [Pytlint Dev Documentation](https://pylint.readthedocs.io/en/latest/index.html) - Link to Pylint page.

[Back to top](#it-restaurant)

## Acknowledgements

- .............
