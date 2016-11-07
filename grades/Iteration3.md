# Iteration 3 Evaluation - Group 18

**Evaluator: [Smith, Scott](mailto:scott@cs.jhu.edu)**

## Positive Points

* You have begun to work on both the front-end and back-end


## Needs work issues

* You still mostly look to be in the prototyping phase, you should have been fleshing out more of the back-end even if it was not hooked up.

## Code

 * why do you still have prototypes hanging around?  You are supposed to be building the app now.
 * You should have code for your underlying classes, endorsement, search, instrument, user, etc - at least the headers, and hopefully more than that.
 * Also you could start stubbing in some more endpoints.
 * Your code is not well-organized, it looks more like a prototype with all the files at the top level and no subdirectories.  Your css is embedded in your html; remember "separation of concerns".
 
**-14 points**

## Github

* You have only one person committing code -- whats going on there?
* No real effort to use github issues so far.
* Whats going on with the iteration-3 branch?  We are always going to be only looking at your master branch.

**-5 points**

## Tests

* Yes you have a test but it looks like it has syntax errors in it so it doesn't really qualify.  Make sure to get tests with coverage for iteration 4.

**-3 points**

## Build

* Your Readme.md needs to be changed from the design doc to the code readme, in particular with instructions on how exactly to run your project and what software is needed (e.g. you seem to need MySQL, MySQL-python?).  You also have no Travis configuration.  Make sure to test your iteration 4 master so you can freshly clone it and based on the instructions in the readme (i.e. copy and paste the lines in from the Readme, that is what I will do) the app will successfully run.

* Here is what I concretely got when I tried running your files after getting the external dependencies to resolve:

```python
$ python Prototype_1.py 
Traceback (most recent call last):
  File "Prototype_1.py", line 6, in <module>
    import signup
ImportError: No module named signup
~/oose/github/2016-group-18 $ python tests.py       
  File "tests.py", line 10
    while n
          ^
SyntaxError: invalid syntax
```

## Iteration Plan

* You mention you have travis running but you have no travis config file in your repo and I only see failing on travis - ?

## Code Docs

* I can't find them.  You already lost enough points but get these for the next iteration.  See last line in the iteration 3 assignment.

## Overall:

I had expected to see more progress on this iteration, make your app and not a prototype.


**Grade: 78/100**

**+5 on iteration 2 for getting RESTful API specified**
