
# Powerof3**
This is a 3rd project for my [codeinstitute](codeinstitute.net) bootcamp. The aim of the project is to demonstrate knowledge and skills gained while learning the datacentric development part in the course. In order to do that I created a fully functional application which is a Smoothie recipe app. Inspiration I got by using similar [apps](https://simplegreensmoothies.com/app) on the web and/or cell phone. The main goal of the project is to demonstrate ability to use CRUD functionality (CREATE,READ,UPDATE,DELETE)


## Database Schema
I used relational db engine [SQLite](https://www.sqlite.org/index.html) which comes as default db for flask web framework. Database scheme that I used is very simple. It connected users with recipes as one to many relationship. It means that one user could make as many recipes as he can, but one recipe can belong only to one user. 

USER ===> [recipe1, recipe2,recipe3] 
recipe1 ===> USER
recipe2 ===> USER

## UX/UI
### UI
The wireframes for this site were created using Figma. Wireframes for the site can be found in the folder [additional_stuff](https://github.com/rcesonis/powerof3/tree/master/additional_stuff)

After browsing through food blogs and recipe apps online I decided that i'm going to use light and vivid tones. Colour palette was generated using [coolors](https://coolors.co/) app. I designed the logo ![Image of Yaktocat](https://power-of-3.herokuapp.com/static/img/logo.svg) with Figma.

Fonts I choose as much readable as possible. So 'Roboto 'and 'Ubuntu' was chosen for the site.
### UX
##### User stories
-   As a user - I can see purpose and goal of the website
-   As a user - I can navigate through the recipes filtering them by author
-   As a user - I can browse the site without being logged as a registered user
-   As a user - I can create a user profile, and log in and log out
-   As a user - I can add, edit and delete my own recipes through my user account
-   As a user - I can change my profile picture, first name, last name and username, email,
also I can write short story about myself.
-   As a user - I am able to access the site on mobile or tablet and have a similar experience as a desktop device
-   As a user - I can filter recipes by author
-   As a user - I am able to see the details of the recipe

## Features

##### Existing Features

The site can be used as a guest or as a logged in user, however, some features are only available to logged in users.

Any visitor of the site can view three latest recipes in the homepage,  by pressing menu button user can choose BROWSE option and see all recipes that is created on the website. There is also a possibility to filter recipes by author by clicking on author name.

Visitors have the option of create an account. Information required to create an account is First name, Last name, Username (which must be unique), password and profile picture(which is set to default), but after registration should be updated in account section . The First name, Last name and Username are stored as plain text but the password is stored in a hashed format using bcrypt. Profile picture can be saved as .svg or .jpg format.

When a visitor has created an account and logged in they are given the option to Add a recipe to the system, Edit their recipes or Delete their recipe from the system. Users can view recipes they have added to the site by filtering recipe by author.

A user has the option to edit or delete a recipe that they have added to the site only. Editing the recipe allows the user to update/or add to the existing recipe information. Deleting the recipe permanently removes the recipe from the system.

The site features custom error pages for both 403 and 404 errors.

##### Future Features

**Images** - could be improved by letting the user to upload an image from their computer. Also a gallery of images for a smoothie would be a nice feature. Now it is only possible to add URL to youtube.com video with recipe guidlines.

**Reviews/Comments** - Add the system to allow users to leave a detailed review/comment about a recipe.

**User accounts** - Passwords are currently stored in a hash format but it is an important requirement to make sure that user logins are made more secure. Possibility to remind password.

**User Dashboard** - A dashboard where the user could update their details including password.


## Technologies Used

The website is designed using following technologies:

-   HTML
-   CSS
-   JavaScript
-   [Python](https://www.python.org/)
-   [Flask](http://flask.pocoo.org/)
-   [SQLite](https://www.sqlite.org/)
-   [Jquery](https://code.jquery.com/jquery-3.2.1.js)
-   [Line Awesome library](https://icons8.com/line-awesome)
-   [Bootstrap](https://getbootstrap.com/)
-   [Google Fonts](https://fonts.google.com/)

## Testing

**Responsiveness Testing:**

Developer Tools, android mobile phone were used to test the appearance of website on mobile screen size.

**User Testing:**

Manual tests were carried out and the testing process was as follows:

**Homepage**

-   Hover and click on navbar items - to verify that all links opens related(view) .
-   If visitor is not logged in “Login” should be displayed in the navigation and clicking this link will bring you to the login page.
-   If visitor is logged in the navigation should see “Account”  and  "Add" view and Logout. 
-   Home page should display three latest recipes added to the site with button to the  recipe info.
-   Clicking on the “Browse” button brings you to the All recipes page.
-   Clicking on the author link, should bring you to page where recipes filtered by author.
-   Confirmed that the social links in the footer open in a new browser window and go to the correct links

**Contact page**

-   Tried to leave one field in the input form empty, should raise "Fill out this field error"
-   If email input is incorrect("Without @") email won't be sent and page reloads. 
-  If email send successfully it should raise message  "Thank you for your message. We'll get back to you shortly."

**User Account**

###### Register Page

-   Confirmed that clicking on the "join our community button" or "register" link brings the user to the registration page
-   All fields are required on the registration form
- If field is missed input field border becomes red.
-  If registration successful web returns log in page.

###### Login Page

-   Confirm that the login link brings the user to the login page
-   If user enters an incorrect username then page reloads. 
-   If user enters a correct username but an incorrect password page reloads to try again.
-   If the user enters the correct login details they are brought to the homepage with a welcome message. Navigation changes from Login to navbar with option to Add and Logout also you can see profile picture.

###### Add Recipe

-   User can only see add a recipe link if they are logged in.
-   Confirmed that all fields are required.
-   If recipe preparation URL to youtube entered incorrectly instead of video user will see 403 error.

###### Edit Recipe

-   User can only edit a recipe if they are logged in and they have added the recipe to the site. 
-   Confirmed that this page is working by clicking on the edit button and seeing the results that are returned.
-   Verify that the edit recipe is working correctly by making a change to the recipe and updating it.

###### Delete Recipe

-   On the Recipe page, verified that the delete button is only displayed to the logged in user that added that recipe to the system.

###### My Recipes

-   Confirm that only recipes added by the user are displayed here
-   Confirm that the user can only see this page once logged in.
-   Confirm that pagination is displayed when user has more than 6 recipes added.

###### Logout

-   Verified that the user is returned to the homepage and logged out of the system.

**Recipe Page**

-   Confirm that clicking on a recipe link, ie through the slider, category cards brings the user to a detailed version of the recipe.
-   Verified that the correct details are being displayed in the correct positions for each recipe.
-   Checked that the social share links are working correctly.
-   Confirmed that the user rating is displaying correctly.
-   User must be logged in to rate a recipe. User is prompted to login if they are not. If the user is logged in they are prompted to rate the recipe. If the user has previously rated the recipe they are not given the option to rate it again.
-   Verified that the recipe tags are working correctly.

**Error Pages**

-   Try going to [403](https://power-of-3.herokuapp.com/sd) and observe the custom 403 error.
-   Confirmed that there was a working link back to the homepage and that links in the navigation are working on the 403 error page.


## Deployment

Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:[https://github.com/rcesonis/powerof3](https://github.com/rcesonis/powerof3)

Heroku App Location is at [https://power-of-3.herokuapp.com/](https://power-of-3.herokuapp.com/)

## Credits

**Content**

All site images are royalty free from [pixabay](https://pixabay.com/) and [unsplash](https://unsplash.com/).

**Code References**

-   [Side navbar](https://bootstrapious.com/p/bootstrap-sidebar)
-   [Project structure](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
-   [bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
-   [pagination](https://www.youtube.com/watch?v=hkL9pgCJPNk)
-   [profile picture](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars-legacy)
-  [blueprints](https://realpython.com/flask-blueprint/)
- [picture handler](https://github.com/jmportilla) - code was taken from his course on [periendata](https://www.pieriandata.com/)

**Acknowledgements**

I would like to thank my tutors and mentor at the Code Institute for all their help and support during the development of this project.



