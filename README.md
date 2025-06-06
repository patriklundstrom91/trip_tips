# Trip Tips  

![Multi-device mockup image](/assets/mockup.png)  

Explore the world togheter by sharing all those hidden gems and wonderful places you have seen and inspire others to exlpore and experience some of all the wonderful spots that excist on our planet. 

[Link to deployed project Trip-Tips](https://trip-tips-b37d3fb90f1a.herokuapp.com/)

## Contents  

* [User Experience](#user-experience-ux)  
  * [Business Goals](#business-goals)  
  * [User Goals / User Stories](#user-goals--user-stories)  
    * [Traveller Goals](#traveller-goals)  
    * [Admin Goals](#admin-goals)

* [Design](#design)  
  * [Wireframes](#wireframes)  
  * [Colour Scheme](#colour-scheme)  
  * [Fonts](#fonts)  
  * [Logo](#logo)  
  * [Favicon](#favicon)  

* [Database Schema](#database-schema)  

* [Agile development](#agile-development)

* [Features](#features)  
  * [Navbar](#navbar)  
  * [Post index page](#post-index-page)  
  * [Filter on continent](#filter-on-continent)  
  * [Post detail](#post-detail)  
  * [Register / login / logout](#register--login--logout)  
  * [Add Post](#add-post)  
  * [Comments](#comments)  
  * [My Posts](#my-posts)  
  * [Favourites](#favourites)  
  * [Footer](#footer)  
  * [Delete confirmation](#delete-confirmation)  

* [Used Technologies](#used-technologies)  
  * [Languages, Frameworks and libraries](#languages-frameworks-and-libraries)  
  * [Platforms and Software](#platforms-and-software)  
  * [Other Tools and Resources](#other-tools-and-resources)   

* [Testing](#testing)  
  * [Manual Testing](#manual-testing)  
  * [Bugs](#bugs)  
    * [Fixed Bugs](#fixed-bugs)  
    * [Unfixed Bugs](#unfixed-bugs)  
  * [Code Validation](#code-validation)  
  * [Lighthouse](#lighthouse)  
  * [Waveapp Accessibility Test](#waveapp-accessibility-test)  

* [Deployment](#deployment)  
  * [Version Control](#version-control)  
  * [How to Fork](#how-to-fork)  
  * [How to Clone](#how-to-clone)  
  * [Deploy on Heroku](#deploy-on-heroku)  

* [Content](#content)  
  * [Images](#images)  
  * [Code Used and sources](#code-used-and-sources)  

* [Credits](#credits)   


## User Experience (UX)

### Business goals

The goa for the site is to create a environment where travellers can share and get tips on travel destinations around the world and promote exploring new parts of the world. 

### User Goals / User Stories

The target audience is backpackers and travellers who have experinces to share or who needs tips on places to visit. 

#### Traveller goals

* As a traveller I want to be able to register/login on the site so I can access functions like post/comment. (Must-have)
* As a traveller I want to be able to read posts with travel tips so I can get inspired to explore new places. (Must-have)
* As a traveller I want to be able to create my own post with tips of places I reccomend others to visit. (Must-have)
* As a traveller I want to be able to comment on posts. (Must-have)
* As a traveller I want to be able to save posts to my favorites so I easily can find them again. (Should-have)
* As a traveller I want to be to update/edit or delete my posts. (Must-have)
* As a traveller I want to be able to edit or delete my comments. (Must-have)
* As a traveller I want to be able to access the site on all devices, mobile, tablet, laptop/desktop and it still looks appeling. (Must-have)
* As a traveller I can filter based on continent. (Should-have)

#### Admin goals

* As a admin I want to have access (login) to an admin page when I can approve posts. (Must-have)
* As a admin I want to approve comments so no bad propaganda is written on the site. (Must-have)
* As a admin I want to be able to delete all posts no matter the author. (Must-have)
* As a admin I want to be able to delete all comments no matter the author. (Must-have)
* As a admin I want to be able to create new posts. (Must-have)

## Design  

### Wireframes  

Below is the wireframes that guided the layout, the end result is very similar to the wireframes with minor adjustments.

* Index page  
![Index, wireframe](/assets/Index.png)  

* Post not logged in  
![Post not logged in,wireframe](/assets/Post.png)  

* Register  
![Register, wireframe](/assets/Register.png)  

* Index, logged in  
![Index logged in, wireframe](/assets/Logged%20in%20index.png)  

* Post, logged in  
![Post logged in, wireframe](/assets/Post%20logged%20in.png)  

* Favourites, logged in  
![Favourites logged in, wireframe](/assets/Favourites.png)  

### Colour Scheme  

The colour scheme was picked with inspiration from different colourschemes related to travel and I wanted softer colours, made a colour scheme in Coolors. 

[Link to Coolors website and colour pallet](https://coolors.co/000000-357266-b0d9d9-fffaf0-ffa5a0)
![Coulor scheme](/assets/colors.png)

### Fonts  

Google fonts is used and imported in CSS, the font Lato is standard and headlines are Lobster. [Link to Google fonts and Lobster, Lato goes in same family](https://fonts.google.com/specimen/Lobster)

### Logo  

Custom logo of airplane made with [freelogodesign.org](https://app.freelogodesign.org/design/0c3cde4a80434003872a184858e444fc/edit)  

![Logo](/static/images/logo-white.png)  

### Favicon  

Favicon converted from logo with [favicon.io](https://favicon.io/favicon-converter/)  

![Favicon](/static/images/favicon-32x32.png)  

## Database Schema

The database is designed to allow full CRUD functionality on both posts and comments for all logged in users. The ERD show the database models and relationships, User is Django default then have Post, Comment and Favourite. Post is related to user. Comment is related to user and post. Favourite is related to user and post.  

![Database ERD](/assets/Database%20ER%20diagram.png)  

## Agile development  

This project was my first project using Agile development guidelines and I used a Kanban board in Github project linked [here.](https://github.com/users/patriklundstrom91/projects/11/views/1) Since I was very time constrained I developed in two short cycles, first cycle focused on basic MVP functionality with the database and planned functionality and the second cycle more focus on styling and refining/ bugfixes and documentation/testing. (1 week per cycle) 

![Kanban board](/assets/kanban%20board.png)  

## Features  

### Navbar  

The page has a navbar that adapts depending on logged in or not. If not logged in you have the following functionality/links:

* Home - Back to index page
* Continents - Filter continents (shown in drop down menu)
* Register
* Login
* Info at right corner or at bottom if small screen saying not logged in

![Navbar not logged in](/assets/nav%20not%20logged%20in.png)  

If logged in the navbar show you the following functionality/links:

* Home - Back to index page
* Continents - Filter continents (shown in drop down menu)
* Add Post - Upload your own blog post with travel tips
* My Posts - see and manage all posts created by you, edit or delete if needed and can also see unpublished posts here waiting for approval
* Favourites - See the posts listed here that you saved to favourites by clicking the heart symbol
* Logout
* Info at right corner or bottom if small screen saying Logged in as "name"  

![Navbar logged in with continents open](/assets/nav%20logged%20in.png)  

 
### Post index page  

When entering the page logged in or not, the first thing you meet is the post index page. Here all published (admin approved) posts gets listed with a pagination of 6. All posts is fetched from the database and rendered in bootstrap cards, for mobile 1 card per row, tablet 2 cards per row and desktop/laptop 3 cards per row to provide a nice and responsive design.  

![Post index page](/assets/post%20index.png)  

### Filter on continent  

If you click on continent in the navbar and pick a specific continent, let's say Europe, then you get all post related to Europe together with a filter visible above the posts to make it easy to change continent without going through the navbar.  

![Post filtered on Europe](/assets/post%20filter%20europe.png)  

If you click on a continent that has no posts yet then a text will tell you so with a link to add a new post if you wish.  

![No posts yet](/assets/filter%20no%20posts.png)  

### Post detail  

If you click on a published post-card then you get sent to a post detail page where you can read the post in full as well as read and write comments and save post to favourites. If you are logged in and are the author of the post you will also get buttons to edit or delete the post, and the same on comments that's written by you.  

![Post open in post detail](/assets/post%20detail.png)  

### Register / login / logout  

The page uses Django allauth for registration and authentication. A simple registration form is given if clicking register in the navbar. Same with login, a simple form is given when clicking login, asking for username and password. In the right top corner of the page in the navbar you will see if logged in or not. You will also get a custom success message after login.  

![Register](/assets/signup.png)![sign in](/assets/signin.png)  

### Add Post  

When logged in you can add your own posts. Click Add Post in the Navbar and you get sent to the Add Post page where you get a simple form with title, image upload, content text, summary (shown on cards) and continent.  

![Add Post form](/assets/add%20post.png)  

### Comments  

The page has a comment function that you can use after opening a post in post detail while logged in. If not logged in, you're asked to login to write a comment. You can submit a comment directly on post detail and will see it faded while it awaits approval from admin. You can edit or delete your own comments both approved comments and those still waiting for approval to be public.  

![Comment section](/assets/comments.png)  

### My Posts  

Under My Posts you will find all posts created by you. Manage your posts with the easy access edit and delete button directly in list view and find all your posts in one spot. Here you also see your unpublished posts awaiting approval from admin and can edit or delete it before it gets public.  

![My Posts view](/assets/my%20posts.png)  

### Favourites  

When logged in you can reach the favourites function. If you click favourites you get all posts listed in a more list format view one post per row on all devices. you can open the post to read it or click the heart to un-favourite the post and it gets removed from the list.  

![Favourites list](/assets/fav_list.png)  

### Footer  

The page has a basic footer with the text Made by Patrik L (me) and follow us on socials with empty redirects to social sites index pages.  

![Footer](/assets/footer.png)  

### Delete confirmation  

As a safety all deletions have a confirmation before executed. For comments its a modal that pop up asking if your are sure with option to delete or close. For posts it's a separate confirmation page asking you to confirm deletion or if you want to go back.  

![Delete comment modal](/assets/confirm%20delete%20comment.png)![Delete post confirmation page](/assets/confirm%20delete%20post.png)  

## Used Technologies  

### Languages, Frameworks and libraries

In this project the following mix of languages, frameworks and libraries was used:

* Languages
    * Python 3.12.8
    * JavaScript
    * HTML
    * CSS

* Frameworks
    * Django 4.2.20
    * [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

* Libraries
    * [Google Fonts](https://fonts.google.com/)
    * [FontAwesome](https://fontawesome.com/search)  

* Django dependencies:
    * asgiref==3.8.1
    * cachetools==5.5.2
    * certifi==2025.4.26
    * charset-normalizer==3.4.1
    * cloudinary==1.44.0
    * crispy-bootstrap5==0.7
    * dj-database-url==0.5.0
    * dj3-cloudinary-storage==0.0.6
    * django-allauth==65.8.0
    * django-ckeditor-5==0.2.18
    * django-crispy-forms==2.4
    * google-auth==2.39.0
    * google-auth-oauthlib==1.2.2
    * gspread==6.2.0
    * gunicorn==20.1.0
    * idna==3.10
    * oauthlib==3.2.2
    * packaging==25.0
    * pillow==11.2.1
    * psycopg2==2.9.10
    * pyasn1==0.6.1
    * pyasn1_modules==0.4.2
    * requests==2.32.3
    * requests-oauthlib==2.0.0
    * rsa==4.9.1
    * setuptools==80.3.1
    * six==1.17.0
    * sqlparse==0.5.3
    * typing_extensions==4.13.2
    * tzdata==2025.2
    * urllib3==2.3.0

[Cloudinary](https://cloudinary.com/) is used for hosting images and static files and django-allauth for authentication. 

### Platforms and Software  

* VS Code IDE
* [Github](https://github.com/patriklundstrom91/trip_tips) Version control and online resp.
* [Heroku](https://dashboard.heroku.com/) Deployment of django app.
* Balsamiq Wireframes.

### Other Tools and Resources  

* [Lucidchart](https://lucid.app/lucidchart/5e9cfbcc-2896-42e0-82c1-ada5a73174c2/edit?invitationId=inv_678ea2db-46a5-4af1-b50d-10c5f7eba965&page=0_0#) for ERD diagram.  
* [Cloudinary](https://cloudinary.com/) is used for hosting images and static files.  
* [Freelogodesign](https://app.freelogodesign.org/design) for logo.
* [Coolers](https://coolors.co/0a369d-92b4f4-cfdee7) for colour palett. 
* [Favicon.io](https://favicon.io/) for favicon.
* [Unsplash](https://unsplash.com) for default and page specific images.

## Testing  

### Manual Testing  

I have executed manual testing of the page to make sure everything works as intended. Friends have also played around and tested the site on android phone and tablet without any issues reported on final version. Test chart for my manual testing provided below:

Test Chart:  

Action   | Expectation   | Outcome   | Pass/Fail   
----- | ----- | ----- | -----
Open page | Cards with posts load when you enter page | As expected | Pass   
Click on a card | Card open the post you click | As expected | Pass   
Click nav continent > South/central America | The posts related to South/central America shows | As expected | Pass
Click nav continent > North America | No posts related to North America so no posts text show | As expected | Pass
Click nav continent > Europe | The posts related to Europe shows | As expected | Pass
Click nav continent > Africa | The posts related to Africa shows | As expected | Pass
Click nav continent > Asia | The posts related to Asia shows | As expected | Pass
Click nav continent > Australia | No posts related to Australia so no posts text show | As expected | Pass   
Click nav register | Register form shows | As expected | Pass   
Click signup | Gets signed up after filling out the form and press signup | As expected | Pass   
Click nav login | Login form shows | As expected | Pass   
Click sign in | Gets signed in after adding username and password and click sign in | As expected | Pass   
Click on a card (logged in) | Card open the post you click | As expected | Pass 
Click nav continent > South/central America (logged in) | The posts related to South/central America shows | As expected | Pass
Click nav continent > North America (logged in) | No posts related to North America so no posts text show | As expected | Pass
Click nav continent > Europe (logged in) | The posts related to Europe shows | As expected | Pass
Click nav continent > Africa (logged in) | The posts related to Africa shows | As expected | Pass
Click nav continent > Asia (logged in) | The posts related to Asia shows | As expected | Pass
Click nav continent > Australia (logged in) | No posts related to Australia so no posts text show | As expected | Pass  
Click nav Add Post | Add Post form shows to user | As expected | Pass
Click upload post | Filled out form gets sent in and success message shown | As expected | Pass   
Click My Posts | Show posts created by user also unpublished as faded and not openable | As expected | Pass   
click edit on unpublished post | open edit post form and let you send in a updated post | As expected | Pass   
Click delete on a unpublished post | send you to confirmation delete page and lets you go back or delete post | As expected | Pass 
Click on a published post under my posts | Open the selected post in post detail | As expected | Pass   
Click edit on published post | Open edit post form and let you edit, changes status to unpublished after update is sent in | As expected | Pass   
Click delete on published post | Open confirm delete page and lets you go back or delete post | As expected | Pass  
Click edit and delete buttons on a open post in post detail when your own post | lets you edit or delete the post same like under my post | As expected | Pass
Click submit comment on open post in post detail | lets you upload a comment when logged in and gives a success message (comment shows faded on post for user who wrote it) | As expected | Pass  
Click delete comment on post detail | open a confirm delete modal, lets you close or confirm delete, if confirm comment gets deleted | As expected | Pass 
Click delete comment then close on post detail | open a confirm delete modal, lets you close or confirm delete, if close you get sent back to post and comment is not deleted | As expected | Pass 
Click edit comment on post detail | prepopulate comment body, let's you update text and upload again, changes comment to unpublished if it was published before edit | As expected | Pass 
Click favourite icon on a open post in post detail | Heart gets filled and post saved to favourites | As expected | Pass   
Click favourite icon again after filled on a open post in post detail | Toggle favourite so removed from favourites again | As expected | Pass   
Click nav favourites | Show favourite posts in cards in a list style 1 card per row | As expected | Pass   
Click heart symbol on card in Favourites | Removes post from | As expected | Pass   
logged in status show in navbar | logged in as user or not logged in shows in navbar | As expected | Pass   
Need to be logged in to post, edit, delete comment | No functionality to create, edit delete comment available when not logged in | As expected | Pass   
Need to be logged in to create, edit, delete post | No functionality to create, edit delete post available when not logged in | As expected | Pass   
Can only edit/delete your own posts and comments | functionality to edit and delete posts and comments only available to creater of the post/comment | As expected | Pass
Click logout | get confirmation to log out and gets logged out, says not logged in in navbar | As expected | Pass  
Responsiveness when showing posts listed | The cards are responsive and adapt to screen size, 1,2,3 cards per row | As expected | Pass  
Responsiveness when changing screen size on all pages | The pages are responsive and look good on different screen sizes | As expected | Pass


Browsers:   

Action   | Expectation   | Outcome   | Pass/Fail   
----- | ----- | ----- | -----   
All tests in Chrome (PC & Mac)| All tests should pass | All tests passed | Pass   
All tests in Edge (PC)| All tests should pass | All tests passed | Pass   
All tests in Firefox (PC)| All tests should pass | All tests passed | Pass  
All tests in Safari (Mac)| All tests should pass | All tests passed | Pass    
All tests in Safari (Iphone 11)| All tests should pass | All tests passed | Pass  
All tests in Safari (Ipad Air, old version)| All tests should pass | All tests passed | Pass  

### Bugs  

#### Fixed Bugs

After creating the base.html and index.html I tried to open after runserver to see how it looks but got error page saying template base.html does not exist. 
![Bug template base.html does not exist](/assets/bug%20template%20does%20not%20exist.png)

Fix: Forgot to att TEMPLATEs_DIR in DIRS and add TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') in settings.py file. after that it worked. 
![bugfix template base does not exist](/assets/bugfix%20template%20does%20not%20exist%20temp%20dir.png)
![bugfix template base does not exist](/assets/bugfix%20template%20does%20not%20exist%20dirs.png)


Default image not showing if no pic is uploaded when creating post, shows alt text instead, uploaded default pic to cloudinary and then vs code preview the pic on the link src="{% static 'images/default.jpg' %}" alt="default travel image" but not in browser.
![default pic not showing, only uploaded pics when creating post](/assets/bug%20default%20img%20not%20showing.png)

Fix: Need to add STATICFILES_DIRS in settings.py even if adding STATICFILES_STORAGE code for hosting static on cloudinary later in production. 
![default pic shows after STATICFILES_DIRS is added](/assets/bugfix%20default%20img.png)  

The post.title showed first above content even if not supposed to:
![Faulty title showing](/assets/bug%20title%20show%20above%20content.png)  

Fix: Had to move {% block title %}{{ post.title }}{% endblock %} from last of top of page to before {% block content %} then it stopped to render it.
![Move code](/assets/bug%20title%20show%20above%20fix%20move%20code.png)  
![Title gone](/assets/bug%20title%20show%20above%20fixed.png)  

The heart was hard to see on Iphone 11, rendered white instead of black.

Fix: Set color of heart icon to black so it renders black on all devices.  

#### Unfixed Bugs  

The console in chrome dev tools give an error:
Uncaught TypeError: Cannot read properties of undefined (reading 'backdrop')
    at kn._initializeBackDrop (modal.js:160:39)
    at new kn (modal.js:71:27)
    at script.798c0903abc8.js:18:21

Has to do with the modal but everything works so guess it's a load/timing issue when modal is not yet created.  

No other known unfixed bugs at this point.  

### Code validation  

All code is validated and no errors found. py files in CI pep8 Python linter, javascript in JSHint and HTML/CSS in W3C validator.

HTML Validator W3C, No errors  

![HTML validator](/assets/html%20validator.png)  

CSS Validator, No errors  

![CSS Validator](/assets/css%20validator.png)  

JavaScript Validator JSHint, No error just warnings  

![JavaScript Validator](/assets/js%20validator.png)  

Python Linter Pep8 Validator, all py files modified by me, No errors

![views.py in CI python Linter](/assets/pep8%20linter.png)  

#### Lighthouse  

Index page and post page.  
![Index lighthouse](/assets/lighthouse%20index.png)![post lighthouse](/assets/lighthouse%20post.png)  

#### Waveapp Accessibility Test

Page tested at wave app accessibility test No errors. [Link to test](https://wave.webaim.org/report#/https://trip-tips-b37d3fb90f1a.herokuapp.com/)  

![Waveapp](/assets/waveapp.png)  

## Deployment  

### Version Control

The website was created in VS Code and pushed to GitHub repository and later deployed with Heroku. Every push to GitHub repository can be seen so easy to fall back on earlier version if any problems with new code. Following steps were taken.

You push from VS code to GitHub repository by creating a repository in GitHub and then enter the given code, in VS code terminal to make a first push and also create a readme.md file.

You can now push regularly to GitHub with the VS code terminal using the comands:
git add . (press enter)
git commit -m "commit message about changes" (press enter)
git push (press enter)

! Note if any secret keys has been added make sure to put them in a env.py file and add env.py to a .gitignore file before first push. 
When developing a Django project make sure to put DEBUG = False before pushing to Github

### How to Fork  

1. Go to GitHub and sign in or sign up  
2. Go to the repository of this site [link here](https://github.com/patriklundstrom91/trip_tips)  
3. Press Fork button on upper right part of the page  

### How to Clone  

1. Go to GitHub and sign in or sign up  
2. Go to the repository of this site [link here](https://github.com/patriklundstrom91/trip_tips)  
3. Press the green Code button, from there you can clone or download the code as zip  

### Deploy on Heroku  

After pushing code with Debug=False and using .gitignore to make sure no secret keys are public then go to [Heroku](https://dashboard.heroku.com/apps/trip-tips/deploy/github) and register or login. Create a new app, pick region near you (Europe or US). In Deploy choose Deployment method Github and connect to repo (trip_tips in this case).  

Go to Settings and config vars and add your secret keys and API:s needed to make the site work, save and then go to Deploy and Deploy branch under manual deploy. If Procfile, requirements.txt and the code from github is not faulty the site should be processed and deployed! Make sure to add Heroku in Allowed Hosts in settings.py. ('.herokuapp.com')

[Link to Heroku.](https://dashboard.heroku.com/apps/trip-tips/deploy/github)  
[Link to deployed project Trip-Tips](https://trip-tips-b37d3fb90f1a.herokuapp.com/)  

## Content  

Users can create their own content and upload their own pictures on the site. The page is for educational use only. 

### Images  

Some images are used on the site from the development side. These are taken from Unsplash, links below.  

[default blog picture from unsplash](https://unsplash.com/photos/airplane-on-sky-during-golden-hour-ONpGBpns3cs)
[Thailand boats from unsplash](https://unsplash.com/photos/five-brown-wooden-boats-jWKk-0ZBUyg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)  
[Hero index image Rio from Unsplash](https://unsplash.com/photos/aerial-photography-of-cityscape-near-sea-7F65HDP0-E0?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
[Hero North America from Unsplash](https://unsplash.com/photos/gray-rock-formation-under-white-clouds-during-daytime-caxORE4n3ic?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
[Hero Europe from Unsplash](https://unsplash.com/photos/a-view-of-a-city-with-a-church-steeple-in-the-background-e1a1rPN_G_o)
[Hero Africa from Unsplash](https://unsplash.com/photos/pride-of-lion-on-field-L4-BDd01wmM)
[Hero Asia from Unsplash](https://unsplash.com/photos/red-boat-near-mosque-painting--1h_NN3nqzI)
[Hero Australia from Unsplash](https://unsplash.com/photos/sydney-opera-house-near-body-of-water-during-daytime-JmuyB_LibRo?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
[Kuala Lumpur from unsplash](https://unsplash.com/photos/high-rise-building-during-night-time--9B08uduMyY?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)

### Code Used and sources

The basic functions in the blog are very similar and inspired by what we learned in the walkthrough project in the learning material- Think before I blog. customization and adoptions have been made and wider functionality with users adding posts and favourites etc. 

Other resources are:

[Video guide on Django by Dee Mc on youtube](https://www.youtube.com/watch?v=vXMTp_1_L7Y&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=10)  

[Video tutorial by CI teacher Matt with others](https://www.youtube.com/watch?v=YH--VobIA8c)  

[Youtube tutorial by Cloud with Django on django and cloudinary together with other instructions and tips](https://www.youtube.com/watch?v=fQo9ivqX4xs)

[customizing django 404 and 500 error pages](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)

[W3Schools](https://www.w3schools.com/)

Got tips about using javaScript history.back() on back button on confirmation page by my mentor Spencer. This so I return to previus page instead of a specific revert_back address. 

Using Bootstrap cards and navbar as base of the site. 

The book Django 5 by Example by Antonio Mele.

## Credits

I want to send thanks to my mentor Spencer Bariball who support and give guidence as well as good tips. Also My previous cohort facilitator Kristyna who now left code institute have been supportive an checking in. A big thanks also to Kay who now took over as Cohort facilitator and need to handle even more people, you are doing a great job! 

Also want to say thanks to friends and family who supported me and tested the page while I developed it. 
