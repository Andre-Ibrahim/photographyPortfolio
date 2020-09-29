Upadted 2020
Here is an explanation of the several task required in this assignment

Admin:
Username: AndreIbrahim
password: adminadmin


1.  there are 4 forms in this website using flask forms
    1.1 login form that allows users to login
    1.2 registration form that allow users to create an account using an email
    1.3 contact form that allows the user to send an email to the photographer through the site
    1.4 Feedback form this one is really simple its just a text area and a submit
        that allows a logged in user to post feedback

2.  The data of the website is stored in an SQLite date base
    there are two models
    2.1 A users model which allows the website to keep track of the registered users
    2.2 A Feedback model that keeps track of the posted feedback from the users

3. The content of the website
    3.1 As explained in #1 there are 4 forms in this website
    3.2 There is a dynamic table which is the feedback table where it displays the feedback of the
        logged in user. This table is updated every time there's a post by a user
        There is a users list which is only accessible by the admin of the website
    3.3 This website allows for login and registration being logged in unlocks the abillity to post Feedback on the website
        The navbar indicates if the user is logged in in the top right along side a logout button

    3.4 Special Features
        3.4.1 Database
            as mentioned before I am using a SQLite3 instead of a regular .txt file to store data
            it is also important to note that the password are hashed using bcrypt
        3.4.2 Sending Email's
            Using flask mail and the gmail server stmp.gmail.com the website is able to contact the
            photographer through the contact form mentioned earlier.
            Obviously the website doesn't have access the email of the user so what it does is that
            the email of the photographer sends an email to itself with a message at the top
            saying it has been sent with the website alongside the username and the email address of the user
        3.4.3 Reset password
            using the Email feature setup for the above task and the Serializer TimedJSONWebSignatureSerializer
            from the package itsdangerous this website allows the user to reset there password.
            At the login page there is a link to reset password. Once pressed it redirect the user for that page where it promps
            for there email address. Then the backend checks for a match and if it does it sends a link with a token
            to the email address that token is then verified once the user clicks on the link and is asked to enter a new password.


