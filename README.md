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

### The Landing Page

When Users arrive at the restaurant's landing page, they will immediately notice the Navigation bar on the top of the page. The Navigation bar is designed to be easy to use, with the restaurant's name on the left-hand side and on the right-hand side three important links. These links include the Home link, which will redirect users back to the landing page, the Menu link, which provides a downloadable PDF file of the restaurant's menu, and the Reservations link, which redirects users to the booking webpage. 
    
In addition to the Navigation bar, the landing page will also feature a welcoming message addressed to the customer and also include a photograph of a delicious dish from the restaurant.

![Landing Page](static/readme/features/land-page.jpg)

[Back to top](#it-restaurant)

### Main Page Content

The main page of the restaurant is divided into three sections: Our Story, Our Food, and Reserve a Table. 

The Our Story section has a small text that explains about the restaurant. 

![Our Story](static/readme/features/our-story.jpg)

The Our Food section has three identical parts consisting of a picture of a dish, a brief description of the restaurant and its dishes, and two buttons - one for the Restaurant Menu and one for Reservations. These buttons are placed in all three sections to make it easier for the users to find what they need - the restaurant's menu and how to book a table.

![Our Food](static/readme/features/our-food.png)

The Reserve a Table section is designed to draw attention to the Menu Button and Reservations.

![Reserve a Table](static/readme/features/reserve-table.png)

### Footer

In the footer section, there are four parts. The first part displays the name of the restaurant along with a phrase. The second part is "Discover" and includes links to the menu and reservation pages. The third part is "Contact" and displays restaurant information such as the address and ways to contact them. The last part is "Social" and includes links to the restaurant's Facebook and Instagram pages.

![Footer](static/readme/features/footer.jpg)

[Back to top](#it-restaurant)

### Menu

The Menu link provides a downloadable PDF file of the restaurant's menu.

![Menu](static/readme/features/menu.jpg)

### Reservations

#### Sign Up or Sign In

When customers visit the reservations webpage, they will be presented with the option to either Sign Up or Sign In. If it is their first time accessing the restaurant site, they can click on the "Sign Up" button to create a new account. If they are returning customers who have already registered with us, they can choose to Sign In.

![Register or Login](static/readme/features/signup-signin.jpg)

- **Sign Up Page**

There is a Sign up form for new customer. It is a Standard allauth sign up page adapted to the site's theme.

![Sign Up](static/readme/features/signup.jpg)

- **Sign In Page**

There is a Sign In form to be filled in. Also is a Standard allauth sign in page adapted to the site's theme.

![Sign In](static/readme/features/signin.jpg)

[Back to top](#it-restaurant)

#### Already Registered Customer

When a customer is signed in, they will have access to the Booking webpage. On this page, they will find information about their own reservation along with two options - one to edit the booking they have already made and the other to cancel it. They will also be able to view information about other reservations, but they will not have the options to edit or cancel them. It's important to note that customers will not have access to the names of other customers. They will only have access to information such as the date, time, and number of people booked. It is intended that they use this information to book an appointment that doesn't overlap with an existing one.

On this same webpage, there will be two buttons available: one for booking and the other for logging out.

![Reservation Page](static/readme/features/iza-booking.jpg)

- **Booking Page**

On the booking page, users can select a date and time to reserve a table at the restaurant. The available timeslots are between 6:00 PM to 9:30 PM. To make things simpler, the form includes an HTML date picker and dropdown menus with options that are based on the booking model. This helps to streamline the data entry process.Users can also specify the number of people coming along, with a maximum limit of 10 people. If the number of guests exceeds 10, they will need to contact the restaurant directly for reservations. There are two buttons available on the page, one to submit the reservation and the other to go back to the reservations webpage.

![Booking](static/readme/features/booking.jpg)


- **Edit Page**

The Edit page contains the same information as the booking page. Users can modify the date, time, and number of guests(limited to 10 guests).

![Edit](static/readme/features/edit-booking.jpg)

- **Cancel Modal**

When users try to cancel a booking, a modal window will appear, prompting them to confirm their choice by selecting either "Yes" or "No."

![Cancel](static/readme/features/cancel-booking.jpg)

- **Sign out**

Users can log out of their page by clicking on the Logout button on the Reservations page. This will redirect the user to a confirmation page.

![Sign out](static/readme/features/signout.jpg)

### Alerts

The site has been designed using the Django framework, which enables the implementation of customised alerts that are tailored to the needs of the user. These alerts provide valuable feedback to the user. The use of Django also ensures that the alerts are delivered in a consistent and reliable manner, enhancing the overall user experience.

![Msg Booked](static/readme/features/msg-already.jpg)

![Msg No Booked Available](static/readme/features/msg-no-booking.jpg)

![Msg SigOut](static/readme/features/msg-signout.jpg)

![Msg Appo. Confirm](static/readme/features/msg-app-confirm.jpg)

![Msg Delete](static/readme/features/msg-delete.jpg)

![Msg Edit](static/readme/features/msg-edit.jpg)

![Msg Sign In](static/readme/features/msg-signin.jpg)

[Back to top](#it-restaurant)

#### Remaining Bugs

- There are no remaining bugs found.

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

- [Pixabay](https://pixabay.com/) - Link to Pixabay for Free Images.

Various sources were consulted to gain a better understanding of the code being implemented. The following sites were most frequently utilized:

- [Stack Overflow](https://stackoverflow.com/) - Link to Stack Overflow page.
- [W3Schools](https://www.w3schools.com/) - Link to W3Schools page.
- [Python Package Index](https://pypi.org/) - Link to Python Package Index page.
- [Pytlint Dev Documentation](https://pylint.readthedocs.io/en/latest/index.html) - Link to Pylint page.
- [CodeMy.com](https://www.youtube.com/@Codemycom) - Link to YouTube page.
- [Geeks for Geeks](https://www.geeksforgeeks.org/) - Link to Geeksforgeeks page.
- [Django Project Forum](https://forum.djangoproject.com/) - Link to Django Project Forum page.

## Acknowledgements

- I am grateful to my tutor Seun for her unwavering support throughout my project. Her expert guidance and motivation helped me excel and achieve my goals. Additionally.
- I would like to express my gratitude to my brother Rodrigo for his patience in helping and teaching me during difficult times.

[Back to top](#it-restaurant)