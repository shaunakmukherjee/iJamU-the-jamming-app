# Iteration 4 Evaluation - Group 18

**Evaluator: [Smith, Scott](mailto:scott@cs.jhu.edu)**

## Code

You have still not made much progress, overall you have very little code on either front or back-end and the two are still not yet integrated.

For the front-end I see only three html templates.  Most front-end directories just have copies of the back-end code in them -- ??

**-25 points**

## Tests

You have a few tests but not many.  I didn't find them at first since they were on their own branch, something you should not do as the whole point of tests is to be validating the code on your master branch.

You do not yet have Travis integration working.

**-12 points**

## Build / run / deploy

You do not give instructions on how to run your server or the tests.  I don't know your MySQL setup and just get an error message from the database when I try to fire it up.

Your server is currently not deployed on Heroku or similar.

Overall you did not meet this objective for this iteration.

**-10 points**

## Github

You are still not using issues in your regular coding cycle.

You are committing binary files (pyc) to git, don't do that.  Delete them from the repo and make a .gitignore file to keep them out.

You are not really using git to commit line-by-line changes, you are uploading files instead.

Don't use two separate branches for the front and back-end, that is an abuse of git and only leads to trouble.  Same with tests, they should be merged on to master.

On your master branch you currently have two versions of your code, iter and iter4.  Don't do that, you should have only one version of your code.  Get rid of any directory called "iter" anything, the directory should be named something like ijamu or the like as that is the app name.

Much of the above you got dinged before on so this time you get hit harder to get your attention  -- your git workflow overall is in great need of improvement.


**-10 points**

## Iteration Plan

You are supposed to put the iteration 4 update on your wiki, there is only iterations 1-3 there now.  It looks like you put some of it in your main README, that is not where it goes.

## Code Docs

## Overall Comments

Your project is in serious trouble at this point.

**Grade: 43/100**

## Revision

I looked at your revised project a week later. You have finally started using git issues; you still are not integrating your code or using git commit to stage individual changes.  You do have very basic features such as login integrated, that is good to see.  You also have a few basic tests running.  Overall, you did make progress and I will give you **+20 points** boost.

**Overall Grade: 63/100**

