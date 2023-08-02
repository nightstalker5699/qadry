# MakeTheDogHappy
#### Video Demo: (https://youtu.be/xcLHVQvV6vM)
#### description:

# register
## register.py
 ![photo](https://github.com/nightstalker5699/cs50-final-project/blob/04a0ad7b2e6f54e9b234ef3126407e0a58a70f11/readme%20images/register/Screenshot%202022-03-05%20195340.png)
 first we check if user got here by get or post 
 if get then the register page will popup 
 else we create a class that have  all flask-wtform field and we assign that class to local variable called form
 ![photo](https://github.com/nightstalker5699/cs50-final-project/blob/c2c345c57abe95552020e31024ed93ff99beb242/readme%20images/first.png)
 after that we check for validation if it didn't validate right then user will get apology page (pset 9 for used to display user error)
 else we check for password and confirmation to be same if not you get apology :D
 after that, we put your information in the database using sqlite3 and generate a hash of the password not the password itself for security reasons
 ![photo](https://github.com/nightstalker5699/cs50-final-project/blob/fa95bdcb694c51829cecd0c9d7b3655f12691a89/readme%20images/register/Screenshot%202022-03-05%20195400.png)
 ![photo] (https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/register/Screenshot%202022-03-05%20195422.png)
 # login
 ![photo](https://github.com/nightstalker5699/cs50-final-project/blob/6ca58106c2673d0da8ca04448c769e65bda2bfcc/readme%20images/login/Screenshot%202022-03-05%20195449.png)
 same as register with getting and post 
 first we the list of all users who have account on the site then we iterate on the list until we found a username that matches the user typed then we use the check password hash function to dehash the password and if the password is the same then it will return true else return false
 if we found the username and password then the user will be redirected to the home page with his session-id 
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/6ca58106c2673d0da8ca04448c769e65bda2bfcc/readme%20images/login/Screenshot%202022-03-05%20195508.png)
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/login/Screenshot%202022-03-05%20195527.png)
# Donate
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/donate/Screenshot%202022-03-05%20195552.png)
also the same as login 
in the POST route if the form is validated + i used a normal HTML date tag (the wtform one was not working sadly :/)
after that, we get picture of dog data and we make 2 copies 
one that contains the name of the file that will be stored in the database along with the other information
and the second one will get uploaded to the static folder inside a folder called images
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/donate/Screenshot%202022-03-05%20195628.png)
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/donate/Screenshot%202022-03-05%20195658.png)
# home page
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/home/Screenshot%202022-03-05%20194853.png)
the home page is simple it just gives the HTML the animal information
then on the homepage, it gets rendered in a blocks shape like this 
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/home/Screenshot%202022-03-05%20195237.png)
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/home/Screenshot%202022-03-05%20195258.png)
i placed the photo using the direct root then using the name of the file that i store in the database and made adopt submit put in each of the dogs that will redirect you to adopt HTML 
# Adopt
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/adopt/Screenshot%202022-03-05%20195844.png)
first when you click on the adopt button the id of the dog will be passed to adopt URL as key-value 
then we use request.args.get to get the id then we search through the database for the dog with that id 
then we return the dog name and the email of the owner to contact him in the adopt.html file 
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/main/readme%20images/adopt/Screenshot%202022-03-05%20195913.png)
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/adopt/Screenshot%202022-03-05%20195949.png)
# change password
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/change%20password/Screenshot%202022-03-05%20195809.png)
same as login and register 
if they entered the old password right and new equal to confirm then we replace the old with a new one (both are hash :D)
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/change%20password/Screenshot%202022-03-05%20195733.png)
![photo](https://github.com/nightstalker5699/cs50-final-project/blob/569ae1b422c6510997a65df17cd98b4f731fa8ff/readme%20images/change%20password/Screenshot%202022-03-05%20195824.png)
