# Iteration 5 Evaluation - Group 18

**Evaluator: [Smith, Scott](mailto:scott@cs.jhu.edu)**

## Progress Comments -- on target for iteration 6?

You are still quite a bit behind, with 600 lines of code or so total as one indication of that.

It is good to see that you have made progress, though.

## Code Inspection

Most of the code is plugging into various Django framework getter/setter operations so there is not a lot to say about your current code.

### non-CRUD feature code inspection

You don't have this done yet, try to get for iteration 6.  But you want to make sure you have the other stuff done first so you at least have an app to demo.

### Package structure of code and other high-level organization aspects

You are still very weak here, see problems I had building.  There is still a lot of junk and sloppiness in your codebase.  What is the Aux/ directory for example?  The code in there seems to be duplicates.  Also you have most of the code in the Login/ directory - ?  You probably should get rid of Login/ and just put it all into Jamming/, or divide it up more.

## Build / run / test / deploy

Your master branch server is not running for me now:

ImportError: No module named context_processors

It looks like you are using a library not advertised.  You are supposed to create a file requirements.txt at the top level of your app which lists all the packages and versions required.  I made that file and got your app to launch (turns out you are using a different Django version than I had installed).

I tried to make an account, after filling out the form I got the following (I thought I filled in all fields OK).  Note that when doing this I noticed I entered instruments and genres by hand, you probably want users to pick those from a list or else spelling errors will be introduced.


IntegrityError at /accounts/register/complete/
NOT NULL constraint failed: Login_userdetail.Username_id
Request Method:	POST
Request URL:	http://127.0.0.1:8000/accounts/register/complete/
Django Version:	1.8.1
Exception Type:	IntegrityError
Exception Value:	
NOT NULL constraint failed: Login_userdetail.Username_id
Exception Location:	/usr/local/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py in execute, line 318
Python Executable:	/usr/local/opt/python/bin/python2.7
Python Version:	2.7.12
Python Path:	
['/Users/scott/Work/oose/github/2016-group-18',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
 '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
 '/usr/local/lib/python2.7/site-packages',
 '/Library/Python/2.7/site-packages']
Server time:	Mon, 12 Dec 2016 20:14:12 +0000

Tests are running, but coverage is currently throwing an error:

test_user_creation (Login.test_models.UserdetailTest) ... ok
/usr/local/lib/python2.7/site-packages/django/core/management/commands/loaddata.py:225: UserWarning: No fixture named 'user_fixture' found.
  warnings.warn("No fixture named '%s' found." % fixture_name)

/usr/local/lib/python2.7/site-packages/django/core/management/commands/loaddata.py:225: UserWarning: No fixture named 'userdetail_fixture' found.
  warnings.warn("No fixture named '%s' found." % fixture_name)

test_login (Login.test_views.Test_Validations) ... ok
test_register (Login.test_views.Test_Validations) ... ok



## Github

You haven't made any progress I can see, you are still not committing and are instead uploading files.  You still have all the .pyc files in your repository.  etc.  You do have a few issues.

## Iteration Plan / Docs

Your iteration plan does not list the specific things accomplished and also does not list the goals for iteration 6.  I do see you put the things accomplished in your README at least.

Make sure to get pydocs linked to your iteration 6 submission wiki so I can read your code doc.

## Overall Comments

Your build is still not smooth at all but is much better than in previous iteration.  I see you have code for more than just login and setting the profile, but I could not get past the profile screen myself when I ran it.



**Grade: 75/100**
