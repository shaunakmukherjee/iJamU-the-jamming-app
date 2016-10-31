# Iteration 12 Evaluation - Group 18

**Evaluator: [Smith, Scott](mailto:scott@cs.jhu.edu)**

## Positive Points:

* You have continued to refine your features 
* Good initial proposal for your ranking algorithm.
* Improved use-case presentation

## Things to Improve:

* A little light on the prototyping code.
* You didn't include PyDoc for your core classes as was required.  You also did not include the RESTful server API.   *-10 points* but can give some back if you include in iteration 3.
* In your UML, connect() sounds more like a method on User with another User as parameter?  I don't understand why it is on Search class.  Users should have "their" endorsements and instruments so it seems there should be filled-in diamonds on the user side of those associations.  The "Instrument" should really be unique to a user as it includes their technical level at it.  Thinking about it what you may want is InstrumentType which has just guitar etc and then Instrument has an InstrumentType tied to it as well as the individual user data such as technical level.  A Connection should point to 2 users, not 0..* - each connection is associated with 2 user objects. *-3 points*

### Architecture

* You should think more about the front-end aspect of your project, you list no particular JavaScript libraries/frameworks.  You at least should list e.g. JQuery if you are going to avoid using one of the larger frameworks. *-1 point*

## Overall:

Your project is overall coming along well; read the assignment better next time to get the max points.

**Grade: 84/100**

