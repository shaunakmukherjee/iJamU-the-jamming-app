# iJamU - The Jamming App 
iJamU is a musician collaboration platform that allows prospective 'jammers' to search for, send requests and connect with each other. It uses a recommendation algorithm to make sure that the jammers are matched with their 'best' counterparts, based on genre, instruments, etc. It involves a small social network architecture that will make sure they're connected with the best people possible.


### How to run this app 

1. Just unzip all of this or clone the repository. Then go on your Unix command line and type : 'python manage.py makemigrations'
2. Then, 'python manage.py migrate'
3. To run the app : 'python manage.py runserver (whatever port number you want)'
4. Go to your browser and type 'localhost:(your port number)'

VOILA. The app will work ! 

### Complete featues

The complete app contains the following functionalities : 

1. REGISTRATION for new users, followed by the ADDING of the DETAILS (filling in details of genre, instruments, bio, name, etc.)
2. LOGIN for existing users (username and password) - _subject to validation_
3. UPDATE PROFILE for updating details as and when required
4. SEARCH to search for users based on the same instruments/genres - one can CONNECT to interesting users _based on the non-CRUD algorithm designed by us_
5. REQUESTS to see what requests have been sent to the aforementioned user, to either ACCEPT or REJECT them
6. CONNECTIONS to manage connections (accepted requests) - to either view details or DELETE them
7. MESSAGING to message the users via e-mail 

**Note : G-Mail in 2016 has stopped allowing third-party applications like Django to send/receive mails through its transfer protocol (SMTP), however we have managed to exclude the two-phase authentication system. Howevr,the final SMTP permission can't be achieved without proper licenses and permissions.**

