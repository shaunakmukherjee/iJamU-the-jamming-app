# 2016-group-18 - JAMMING APP

*Project members :* 

1.     Chi Young Shin    (tlscldud)
2.     Rohit Ravoori     (rohitravoori)
3.     Shaunak Mukherjee (shaunakmukherjee)

## ITERATION 1

### Vision Statement
>In this project, we will be attempting to build a service that will allow musicians to interact, collaborate and basically, produce music together. The whole concept of 'jamming' will be redefined, as interested people can view profiles of prospective collaborators, and select who they want to have. There might yet be a parameter as to define how 'good' the musician/group is and how frequently they collaborate, also depending on ‘endorsements’ that users might give and ‘recommendations’ users might write. We would preferably want this to have an on-campus geography initially, but it will cover almost all bases when it comes to genres and/or instruments played.

### Features List
- New users can __sign up__ to the service, giving their details
- Existing users need to **log in** through a specific username and password generated by them during the signup
- User can indicate whether they are :
    - Musicians searching for a band
    - Band searching for a musician
- User can filter jammers according to : 
     - instrument/s played
     - genre of music most comfortable with
     - geography/region
     - most "popular" (based on previous user ratings)
     - skill (based on ratings/endorsements)
- User can indicate interest on a jammer
      - Accept
      - Reject
- Connections
      - User can manage his/her connections
- Chat service between connected users (Messenger)
      - Basically, a messenger system to connect users who've "liked" each other
- Endorsements
      - Users can endorse a jammer's profile, or his/her skill in a particular instrument/genre/vocals
- Recommendations
      - User can recommend (write review) a musician
- Current **technical level/skill** of the user will be determined by an algorithm based on :
      - User's original technical level (beginner/amateur/professional/expert)
      - Endorser's current level
      - No. of previous collaborations



### User Interface

### UML Activity Diagram
![Activity Diagram] (https://www.gliffy.com/go/publish/image/11225211/L.png)

### Domain Model
![Domain Model] (https://www.gliffy.com/go/publish/image/11227061/L.png)

### Use Cases

**User Sign Up**

1. User visits the sign up page.
2. User enters an email id.
    1. Email id already exists. User asked to login.
    2. Email id is unique and user continues with step 3.
3. User fills in username and password.
4. User gets a sign up confirmation and asked to login.

**User Login**

1.	User visits login page.
2.	User enters email id and password
    1. Email id does not exist. Prompt user to sign up.
    2. Email id and password don’t match. Prompt user to retry login.
        1. User clicks on forget password. Email is sent to the user to reset password.
3.	User’s customized main page opens up.

**User sets up/updates his profile**

1.	User logs in.
2.	User clicks on profile tab.
3.	User fills in his profile details.
4.	User gets a confirmation of the update to his profile.

**User sets up a search for band members**

1.	User logs in.
2.	User sets the genre, instrument, technical level and distance for the search.
3.	The system returns a set of profiles relevant to the search filled in by the user using the recommendation system.
4.	User clicks on the connect button with prospective bandmates.

**User shows interest in playing for a band**

1.	User logs in.
2.	User’s profile is marked as available.
3.	User’s profile will be returned as part of the results when the profile is relevant to search using the recommendation.
4.	User will receive a request to connect.
    1. User accepts the connection. 
    2. User ignores the connection.

**Messenger (inside "Connections" tab)**

1.	User logs in.
2.	User 1 checks for a connection with User 2.
    1. A connection exists and a message option is present. Go to step 2.
    2. A connection does not exist. Request a connection and wait to connect.
3.	User 1 clicks on the message button next to User 2’s profile.
4.	User 1 types up a message and hits the send button. 
5.	The system delivers the message to User 2 the next time he logs in.
6.	User 2 receives the message.
    1. User 2 replies by writing a message and clicking on the reply button.
    2. User 2 ignores the message and the message cycle ends.
7.	System delivers the message to user 1 the next time he logs in.
8.	User 1 receives a message.
    1. User 1 responds, looping back to step 4.
    2. User 1 ignores the message and the message cycle ends.

**Endorsing a jammer’s profile**

1.	User logs in.
2.	User clicks on connections tab.
3.	User 1 visits User 2’s profile.
    1. User 1 chooses to endorse the user 2’s profile.
4.	The system reflects the endorsement on User’s 2 profile.
5.	The system recalculates user 2’s ratings and updates it using the recommendation system.

**Rating a jammer’s profile**

1.	User logs in.
2.	User clicks on the connections tab.
3.	User 1 visits User 2’s profile
4.	User 1 chooses the skill to rate or update.
5.	The system updates the ratings of user 2 using the recommendation system.



### System Architecture

The system will use a MySQL database at the server side to store details and preferences of each user. Each user will connect to the server to use the jamming application. The messenger application will make use of TCP along with a MySQL database to exchange messages and to store the messages. 

The system will be divided into these major packages –

- The RecommendationSys package will contain the complex algorithm which is responsible for calculating the skills of the user and the overall level of the user along with handling endorsements and returning the results for the queries.
- The MessengerSys package will contain the code that handles the communication between 2 users and will be responsible for the TCP and database implementation.
- The UserSys package will contain the controller along with the code to maintain the user’s profiles in the database. This includes the signup and login classes.
- The View package will contain the code for our front end and will run on the client side. This package will interact with the UserSys package.

### Resources

We plan to use the following software and repositories/libraries for the project : 

- Python and Django
- SocketServer Library
- Python RecSys Library
- MySQL
 
 



