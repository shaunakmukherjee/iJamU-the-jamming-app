# 2016-group-18
# iJamU - Alpha release 

*Project members :* 

1.     Chi Young Shin    (@tlscldud)
2.     Rohit Ravoori     (@rohitravoori)
3.     Shaunak Mukherjee (@shaunakmukherjee)

### Notes on the Beta release (1.2)

All bugs have been fixed and the app is complete. The algorithm has been integrated, and the results are reflected during the 'Search' and any other functions. 

Things needed to be done to make this better, in the future would be :

1. As mentioned in the external features, to implement the Google Maps API to seamlessly integrate the distance functionality.
2. Making the algorithm a bit more optimal, it currently runs in O(n^2) time.
3. Making a complete chatting app for seamless switching of real-time messages (as in Facebook, LinkedIn, etc.)

### Notes on the Alpha release (1.1)

The alpha build of the project is up and running.
The Master file here contains the complete buildable code for the app, which consists of the entire front-end as well as back-end functionality. 
It contains the following functionalities : 

1. REGISTRATION for new users, followed by the ADDING of the DETAILS (filling in details of genre, instruments, bio, name, etc.)
2. LOGIN for existing users (username and password) - _subject to validation_
3. UPDATE PROFILE for updating details as and when required
4. SEARCH to search for users based on the same instruments/genres - one can CONNECT to interesting users 
5. REQUESTS to see what requests have been sent to the aforementioned user, to either ACCEPT or REJECT them
6. CONNECTIONS to manage connections (accepted requests) - to either view details or DELETE them
7. MESSAGING to message the users via e-mail 

**Note : G-Mail in 2016 has stopped allowing third-party applications like Django to send/receive mails through its transfer protocol (SMTP), however we have managed to exclude the two-phase authentication system. Howevr,the final SMTP permission can't be achieved without proper licenses and permissions.**


Also, **test cases** have been written for the backend:
 - The models (database) test cases have been written.
 - Framework for the views has been written (test has not yet been implemented)
 - Travis test harness has been implemented
 - Below is a coverage report of currently available tests

### Test Coverage
```
Jamming/__init__                                                                                                             0      0   100%   
Jamming/settings                                                                                                            19      0   100%   
Login/__init__                                                                                                               0      0   100%   
Login/admin                                                                                                                  3      0   100%   
Login/forms                                                                                                                 10      0   100%   
Login/migrations/0001_initial                                                                                                8      0   100%   
Login/migrations/0002_userdetail_address                                                                                     5      0   100%   
Login/migrations/0003_search                                                                                                 5      0   100%   
Login/migrations/__init__                                                                                                    0      0   100%   
Login/models                                                                                                                20      0   100%   
Login/test_script                                                                                                           24      2    92%   85-86
Login/views                                                                                                                 46     28    39%   20, 23-35, 38, 42-43, 46-47, 50-58, 61-64
manage                                                                                                                       6      0   100%   
------------------------------------------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                                                    40205  24611    39% 
```

The Aux contains all the auxiliary, previous files used in the iterations preceding this. They've been kept for the sake of coverage.

###PREVIOUS ITERATION WORKFLOW has been shown below for reference:

## Vision Statement/Overview
>We will be attempting to build a service that will allow musicians to interact, collaborate and basically, produce music together. The whole concept of 'jamming' will be redefined, as users will be given the opportunity to view profiles of musicians in their area - who play different instruments (guitar, drums, keyboards, etc.), with varying skills in different genres - and connect with them to produce music together. Our app will enable users to either search for other musicians for a gig; search for bands to join; or simply look for like-minded individuals to play some music, relax and socialize through 'jamming'.

>The user will be able to search for other musicians based on instruments, genres, technical level, and years of experience. Our ranking algorithm will take in to account various factors such as number of previous collaborations, technical level, user ratings and proximity to offer you the best people to connect with for you! This non-trivial algorithm first calculates the user's technical level, and correlates that with previously obtained ratings, to rank and sort the musicians in your search results to conveniently recommend the best people to connect with.

>Once a user decides on a musician to collaborate with, he is able to send a request for a connection that will enable the users to communicate with each other through a direct messaging application. Users will have the ability to reject or accept a connection and will also have the ability to endorse fellow musicians that they have connected with following a successful collaboration. The number of endorsements and the ratings you receive in these endorsements will be integral in improving your profile which will enable you to connect with more active and prominent musicians by enhancing your visibility to other users.


## Features List:
- New users can __sign up__ and make an account
    - Required fields (Email ID, password, User name)
- New users will be designated as __'new members'__ until users receives a certain number of endorsements
- Existing users need to **log in** through a specific username and password generated by them during the signup
- User can update profile information
    - Instruments and the corresponding genres that the user plays (e.g. guitar - rock)
    - Personal info (address, Bio, profile picture, etc.)
- User can indicate whether they want to be searched or not (available: boolean)
- User can filter jammers according to : 
     - Instrument/s played
     - Genre of music most comfortable with
     - Maximum distance from user
     - skill (based on technical level/yrsExp/endorsements)]
     - Username and name
- User can send a request to **connect** to users found on searches
- User can accept/deny requests to connect
- User can delete users they are connected to
- User can view the profile of a connected user
- User can **endorse** and give ratings/comments to a connected user
     - Users can only endorse a connected user once
     - Users can update their endorsements change ratings/comment
- Chat service between connected users (Direct Messaging App)
- Current **technical level** and **rating** of the user will be determined by an algorithm using endorsements (see below)
      - Endorsed technical level and rating
      - number of endorsements received
- User can build his profile (increase rating, technical level) through receiving endorsements

## Extended Features:
- Retrieve current location of user or user designated address in search instead of address
- Users can view a list of endorsements showing ratings and comment of a searched or connected user
- Multiple endorsements to the same user using a time limit between endorsements
- Sample clips (video, audio) in profiles to demonstrate skill
- Certification and/or links to gigs and events in profiles
- Notification on incoming messages from connected users
- Endorsements on the user's skill of a certain instrument instead of/in addition to profile
- Algorithm on technical level calculation that takes into account the rating/technical level of endorser
- Use time instead of finite number of endorsements to calculate current technical level and rating
- Factor number of connections in ratings
- A detailed "LEVEL-UP" plan has also been brainstormed, as to how the user can **level up** from one TL to another (or a separate level system with achievements and challenges) after accumulating a certain number of points, based on previous collaborations, ratings obtained, etc.
- Also, the extended feature of the Google Maps is going to be incorporated, so as to achieve geographical functionality.


## User Interface

LOGIN 

![signup](https://cloud.githubusercontent.com/assets/22137960/19027247/7c142d48-88fc-11e6-997f-c72e969404ab.jpg)

SIGNUP (New User)

![signup_2](https://cloud.githubusercontent.com/assets/22137960/19027248/7c15692e-88fc-11e6-9ccb-fadfb3260a8d.jpg)

PROFILE (MAIN PAGE)

![profile](https://cloud.githubusercontent.com/assets/22137960/19027244/7c1181b0-88fc-11e6-9782-eb90bc0a8f50.jpg)

SEARCH 

![search](https://cloud.githubusercontent.com/assets/22137960/19027246/7c1342ca-88fc-11e6-938e-2851d267eac0.jpg)

CONNECTIONS 

![connections](https://cloud.githubusercontent.com/assets/22137960/19027245/7c1236c8-88fc-11e6-8771-2c8a99460297.jpg)


### Class Diagram

![class_diag](https://www.gliffy.com/go/share/image/slmn4b13fqnrp5ingx4l.png?utm_medium=live-embed&utm_source=custom)


### UML Activity Diagram

![Activity Diagram] (https://www.gliffy.com/go/publish/image/11225211/L.png)


### Basic Algorithm for Ranking Search Results

The user will first indicate search criteria : **genres**, **instruments**, etc. Then, the user indicates boundaries to limit the search in :
 1. Minimum technical level 
 2. Minimum years of experience 
 3. Minimum no. of previous endorsements 
 4. Distance from user 

_Key variables :_
- Technical Level = tl 
- Years of experience = n_y
- No. of endorsements = n_e
- Distance away from user = d
- Technical rating = r
- Overall rating = r_o

_Points to be noted :_
- The user may choose not to fill the boundaries; however, the search will be broader, and hence, less accurate.
- There will be two types of ratings that can be given to users through endorsements: 'r' for the technical rating, and 'r_o' for the overall rating, _ that factor the user's personality, punctuality, collaboration experience etc._

**_Calculation of technical level:_**

`TL = (r_1 + r_2 + ...... + r_m)/ m ` for the first 'm' endorsements.

**'m'** is the constant number of endorsements (say, **=20**) that will be taken into account when calculating the user's technical and overall rating, **"r_i"** being the rating given (out of 5) in the 'i'th endorsement received by the user. Essentially, the TL can be calculated as __(r_1 + r_2 + .... r_20)/20__ for the first 20 endorsements, and then it can be __(r_2 + r_3 + .... r_21)/20__ then __(r_3 + r_3 + .... r_22)/20__ once the user receives more than **'m' (20)** endorsements, and so on. this enables the user's technical level to stay current and relevant. Users will only be able to endorse a connected user once. The user may update the endorsement (ratings, comments); however, if the specific endorsement does not fall within the 'm' range of most current endorsements, the ratings given will not affect the user's ratings on profile.

For new users who have yet to receive **'m'** endorsements, the TL will still be calculated with **'m'** endorsements. During such time until the user reaches **'m'** endorsements, the user will be designated as a **'new member'** whose TL has yet to reflect the user's true technical level. This system is implemented to encourage users to connect and collaborate with fellow users to receive endorsements. Every user begins as a **'new member'** and subsequently builds his/her profile to connect with user's with higher technical levels and ratings. The **'TL'** will be out of 5.

- 0-1 : Newbie
- 1-2 : Beginner
- 2-3 : Amateur
- 3-4 : Professional
- 4-5 : Expert. 

**_Calculation of overall rating:_**

Same as technical rating (for now)


**_Optimization of Search:_**

Profile are shown in order of rank based on : 
 1. Retrieve tl, n_y, n_e, r, d from the search criteria and user's technical profile.
 2. Calculate final rating 'R' as : 

`R = { n_y + n_e + (tl*f1) + (r_o*f2) }/ (40 + f1 + f2)`

_f1 = factor of multiplying technical level, f2 = factor of multiplying overall rating_

The number of years of experience, and the no. of endorsements are set to a maximum of 20, and hence the weighted sum is calculated as (40 + f1 + f2). The factors f1 > f2 are used as the technical rating should factor slightly more than the overall when it comes to ranking.

The Rating calculated by us (R), will show up alongside the distance parameter (d), which will then give the user a perfect trio to judge his/her best possible match! The distance parameter was not included in the ranking equation, as it's prudent that for the sake of music, the better person should be found irrespective of how far he/she is! User's lacking the ability to travel far may reduce the max distance boundary when searching.

### Use Cases (Updated)

**User Sign Up**
 1. User visits the sign up page.
 2. User enters an email id.
     - 2.1. Email id already exists. Take 2.2.
     - 2.2. Prompt user to login 
     - 2.3 Email id is unique. Continue with 3.
 3. User fills in username and password.
 4. User gets a sign up confirmation and asked to login.

**User Login**
 1. User visits login page.
 2. User enters email id and password.
     - 2.1. Email id does not exist. Take 2.2
     - 2.2. Prompt user to sign up.
     - 2.3. Email id and password don’t match. Take 2.4
     - 2.4. Prompt user to retry login and provide a forgot password link. 
     - 2.5. User re-enters details. Loop back to 2.
     - 2.6. User clicks on forget password. Continue with 2.6.
     - 2.7. Email is sent to the user to reset password.
 3. User’s customized dashboard opens up.

**User sets up/updates his profile**
 1. User logs in.
 2. User clicks on profile tab.
 3. User fills in his profile details.
 4. User gets a confirmation of the update to his profile.

**User sets up a search**
 1. User logs in.
 2. User sets the genre, instrument, technical level and distance for the search.
 3. The system returns a set of profiles relevant to the search filled in by the user using the recommendation system.
 4. User clicks on the connect button with prospective bandmates.

**User shows interest in playing for a band**
 1. User logs in.
 2. User’s profile is marked as available.
 3. User’s profile will be returned as part of the results when the profile is relevant to search using the recommendation.
 4. User will receive a request to connect.
     - 4.1. User accepts the connection. Message option now opens up.
     - 4.2. User ignores the connection. 

**Messenger**
 1. User logs in.
 2. User 1 checks for a connection with User 2.
     - 2.1. A connection exists and a message option is present. Go to step 3.
     - 2.2. A connection does not exist. Request a connection and wait to connect. Go to step 2.
 3. User 1 clicks on the message button next to User 2’s profile.
 4. User 1 types up a message and hits the send button. 
 5. The system delivers the message to User 2 the next time he logs in.
 6. User 2 receives the message.
     - 6.1. User 2 replies by writing a message and clicking on the reply button. Go to step 7.
     - 6.2. User 2 ignores the message. Go to 9. 
 7. System delivers the message to user 1 the next time he logs in.
 8. User 1 receives a message.
     - 8.1. User 1 responds, looping back to step 4.
     - 8.2. User 1 ignores the message.
 9. Message cycle ends.

**Endorsing a jammer’s profile**
 1. User logs in.
 2. User clicks on connections tab.
 3. User 1 visits User 2’s profile.
     - 3.1. User 1 chooses to endorse the user 2’s profile.
 4. The system reflects the endorsement on User’s 2 profile.
 5. The system recalculates user 2’s ratings and updates it using the recommendation system.

**Rating a jammer’s profile**
 1. User logs in.
 2. User clicks on the connections tab.
 3. User 1 visits User 2’s profile
 4. User 1 chooses the skill to rate or update.
 5. The system updates the ratings of user 2 using the recommendation system.

##RESTful Interface
```
_Login_
Method               POST
URL                  r/jamming/Login
Body                 { userID : <string><PK>, password : <string><unique>, createdOn: <date string> }
Success Response     Code: 201 user logged in
                     Body: {}
Failure              404 (invalid userid/password)

_Sign up_
Method               POST
URL                  r/jamming/Signup
Body                 { emailID : <string>, password : <string><unique>, userName <string><unique> }
Success Response     Code: 201 user signed up
                     Body: {}
Failure              404 (invalid userid/password)

_Update profile information_
Method               PUT
URL                  r/jamming/Profile
Body                 { firstName : <string>, lastName : <string>, bio : <string>, address :              
                     <string>, availability : <boolean> }
Success Response     Code: 200 updated
                     Body: { firstName : <string>, lastName : <string>, bio : <string>, address :              
                     <string>, availability : <boolean> }

_Add instrument_
Method               PUT
URL                  r/jamming/Profile/instrument
Body                 { type : <string>, genre : <string>, tl : <int> }
Success Response     Code: 200 added
                     Body: { type : <string>, genre : <string>, tl : <int> }

_Retrieve genres of instrument_
Method               GET
URL                  r/jamming/Profile/instrument
Body                 (none)
Success Response     Code: 200 OK
                     Body: { genre : <string><list> }
Failure              422 (no instruments)

_Retrieve current technical level_
Method               GET
URL                  r/jamming/Profile/tl
Body                 (none)
Success Response     Code: 200 OK
                     Body: { tl : <int> }

_Update technical level_
Method               PUT
URL                  r/jamming/Profile/tl
Body                 { tl : <int> }
Success Response     Code: 200 updated
                     Body: { tl : <int> }

_Request a connection_
Method               POST
URL                  r/jamming/Connection
Body                 { emailID1 : <string>, emailID2 : <string> }
Success Response     Code: 201 requested
                     Body: {}
Failure              410 (invalid emailID)

_Accept or reject a connection_
Method               PUT
URL                  r/jamming/Connection
Body                 { response : <boolean> }
Success Response     Code: 200 OK
                     Body: { response : <boolean>, emailID1 : <string>, emailID2 : <string> }

_Make a search_
Method               POST
URL                  r/jamming/Search
Body                 { genres : <string><list>, instruments : <string><list>, minTL : <int>, minYrsExp : <int>, minNE : 
                     <int>, maxDist : <int>, userName : <string>, name : <string> }
Success Response     Code: 201 searched
                     Body: { users: <list> }
Failure              404 (invalid search parameters)

_Make an endorsement_
Method               POST
URL                  r/jamming/Endorsement
Body                 { emailID1 : <string>, emailID2 : <string>, tl : <int>, rating : <int>, comment : <string> }
Success Response     Code: 201 endorsed
                     Body: {}
Failure              410 (invalid emailID)

_Retrieve the endorsed technical level_
Method               GET
URL                  r/jamming/Endorsement
Body                 { emailID: <string> }
Success Response     Code: 200 OK
                     Body: { tl : <int> }
Failure              410 (invalid emailID)

_Update endorsement_
Method               PUT
URL                  r/jamming/Endorsement
Body                 { emailID : <string>, tl : <int>, rating : <int>, comment : <string> }
Success Response     Code: 200 updated
                     Body: { emailID : <string>, tl : <int>, rating : <int>, comment : <string> }
Failure              410 (invalid emailID)

_Send a Direct Message_
Method               PUT
URL                  r/jamming/Connection
Body                 { emailID : <string>, message: <string>, sentOn : <date string> }
Success Response     Code: 200 sent
                     Body: { emailID: <string>, message: <string> }
Failure              410 (invalid emailID)

_Retrieve the Direct Message messages_
Method               GET
URL                  r/jamming/Connection
Body                 { emailID: <string> }
Success Response     Code: 200 retrieved
                     Body: { messageHistory : <string><list>, sentOn : <date string> }
Failure              410 (invalid emailID)
```


### Architecture

<img width="714" alt="screen shot 2016-11-14 at 11 04 38 am" src="https://cloud.githubusercontent.com/assets/22307828/20666921/a8d751e8-b534-11e6-9de0-8fdf9bce481e.png">

The system will use a MySQL database at the server side to store details and preferences of each user. Each user will connect to the server to use the jamming application. The messenger application will make use of TCP along with a MySQL database to exchange messages and to store the messages. The system might implement a Google Map API as part of the extended features to display the location of user and a prospective jammer. The front end will be built using HTML, CSS and JavaScript. 

We're using two main JavaScript frameworks : _Angular.js_ and _jQuery_. As shown, we have already used Angular to create some new features in the HTML, but we also aim to use jQuery as well to make the front-end more comprehensive.

The system will be divided into these major packages:

- The **RecommendationSys** package will contain the complex algorithm which is responsible for calculating the skills of the user and the overall level of the user along with handling endorsements and returning the results for the queries.
- The **MessengerSys** package will contain the code that handles the communication between 2 users and will be responsible for the TCP and database implementation.
- The **UserSys** package will contain the controller along with the code to maintain the user’s profiles in the database. This includes the signup and login classes.
- The **Template** package will contain the code for our front end and will run on the client side. This package will interact with the **UserSys** package.

We plan to use:
-	Python (2.7) and Django (1.8.1)
-	HTML, CSS and JavaScript
-	SocketServer Library
-	Python RecSys Library
-	MySQL
-	Google Maps API – (Extended Features)
-	Facebook API – (Extended Features)
-	Skype API – (Extended Features)
