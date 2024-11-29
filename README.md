![GlucoGroove logo](/workspace/Diabetes-App/staticfiles/images/default.jpg)

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

