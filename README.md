![GlucoGroove logo](/workspace/Diabetes-App/static/images/GlucoGroove_logo.jpg)

# Diabetes Blog Application 

## Overview 

This project is a Django-based blog application that allows users to register, log in, 
create new blog posts, leave comments, upvote or downvote comments, and interact with 
other users' posts. The application is designed to provide a platform for sharing and 
discussing experiences related to diabetes. 

## Features 

- User registration and authentication 
- Create, edit, and delete blog posts 
- Leave comments on blog posts 
- Upvote and downvote comments 
- Responsive design for mobile and desktop 

## Technologies Used 

- Django - SQLite (default database) 
- HTML/CSS 
- JavaScript (for interactive features) 

## Installation ### Prerequisites 

- Python 3.6+ 
- Django


## Bugs, debugging and fixes or action

- Attribute error indicating Comment model does not have a title
  when trying to access Comments in admin panel.
    
    - There is a __str__ method trying to reference a title fixed by updating
      statement in Comments model.

- Debug set to FALSE application would not launch through Heroku giving a server error 500.
  
  - Identified that compressed storage STATICFILES_STORAGE prevent the page loading so commented out.
    this prevented the server 500 error but the default image for blog posts would not load.
  
  - Image was trying to load from a media file rather than the static folder.
    Identified that a management command was over-writing the featured_image field.
    Commented out management command and STATICFILES_STORAGE which has fixed the error.

## Creits

- John Rearden for his fantastic support as a coding coach.
- Stack Overflow
- WECA cohort for help and advice at a time where we all had 
  the pressure of our capstone project.
