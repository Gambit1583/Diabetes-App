![GlucoGroove logo](static/images/GlucoGroove_logo.jpg)

# **GlucoGroove**

## Overview 

**GlucoGroove** is a Django-based online blog application that allows users to register, log in, 
create new blog posts, leave comments, upvote or downvote comments, and interact with 
other users' posts. The application is designed to provide a platform for sharing and 
discussing experiences related to diabetes. The hope is to create an online community for those with diabetes
while giving the user a private space to record and track their blood sugars, food intake and 
general record their daily lives in a safe space.

## Features 

- User registration and authentication 
- Create, edit, and delete blog posts 
- Leave comments on blog posts
- Reply to comments and reply to replies
- Upvote and downvote comments
- Track blood sugars
- View a graph illustrating blood sugar level input by user
- Keep a food diary
- Keep a daily diary 
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

  - Further issues in relation to static file storage were causing lack of responsiveness in heroku
    after starting a second application in my project. After running similar fixes to the previous ones 
    the issue was not resolved.
    This was eventually fixed by rewriting my entire settings.py and including the installation of
    Cloudinary within my project.

## Credits

- John Rearden for his fantastic support as a coding coach.
- Kevin Loughrey for his 1-1 support
- Stack Overflow
- WECA cohort for help and advice at a time where we all had 
  the pressure of our capstone project.
- Chat gpt for debugging snippets and recoomendations on structure/formatting 

