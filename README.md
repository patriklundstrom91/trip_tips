# Trip Tips

Explore the world togheter by sharing all those hidden gems and wonderful places you have seen and inspire others to exlpore and experience some of all the wonderful spots that excist on our planet. 

Device picture

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
* As a traveller I can serach for a country and see if there is any tips/posts about it. (Could-have)

#### Admin goals

* As a admin I want to have access (login) to an admin page when I can approve posts. (Must-have)
* As a admin I want to approve comments so no bad propaganda is written on the site. (Must-have)
* As a admin I want to be able to delete all posts no matter the author. (Must-have)
* As a admin I want to be able to delete all comments no matter the author. (Must-have)
* As a admin I want to be able to create new posts. (Must-have)


Font Lato and headlines Lobster

## Bugs

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

## Images
[default blog picture from unsplash](https://unsplash.com/photos/airplane-on-sky-during-golden-hour-ONpGBpns3cs)
[Thailand boats from unsplash](https://unsplash.com/photos/five-brown-wooden-boats-jWKk-0ZBUyg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)  
[Hero index image Rio from Unsplash](https://unsplash.com/photos/aerial-photography-of-cityscape-near-sea-7F65HDP0-E0?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
[Hero North America from Unsplash](https://unsplash.com/photos/gray-rock-formation-under-white-clouds-during-daytime-caxORE4n3ic?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
[Hero Europe from Unsplash](https://unsplash.com/photos/a-view-of-a-city-with-a-church-steeple-in-the-background-e1a1rPN_G_o)
[Hero Africa from Unsplash](https://unsplash.com/photos/pride-of-lion-on-field-L4-BDd01wmM)
[Hero Asia from Unsplash](https://unsplash.com/photos/red-boat-near-mosque-painting--1h_NN3nqzI)
[Hero Australia from Unsplash](https://unsplash.com/photos/sydney-opera-house-near-body-of-water-during-daytime-JmuyB_LibRo?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
[Kuala Lumpur from unsplash](https://unsplash.com/photos/high-rise-building-during-night-time--9B08uduMyY?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)

## Credits
(customizing django 404 and 500 error pages)[https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages]