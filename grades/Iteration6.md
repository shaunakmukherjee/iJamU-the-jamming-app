#### Group Number: 18 IJamU

#### Presentation

Good pitch!

##### App demo comments.  Did any errors/glitches arise during the demo?

- Congrats, you did get your core features working and no bugs during demo.

- Good use of Django authentication

##### UI quality -- look and usability

- No active web beyond one alert,and you had  only the most bare-bones of static html content.  You didn't get anywhere near your conceived UIs which were very nice.

- Drop-down in corner for all options is somewhat lame.

- Should check if profile exists right after when you log in, don't show option when it doesn't work.

#### Iteration 6

Your project is generally running pretty well but I did get one error during testing - endorse did not work.

```
NameError at /endorse_new/eee/
global name 'Userdetails' is not defined
```

The final UI was a bit better than in the demo, but it still needs a lot of polishing.

##### Code inspection

During the code review of the presentation your code was hard to read due to short variable names, lots of commented out code etc. Generally this reflects a sloppy coding style you need to improve on.

During the demo you were confused about foreign keys and how an object-relational mapping (ORM) works - your implementation there is not the right way to do it.

##### Architecture - was the code cleanly structured in terms of packages, deployment, etc

Not deployed to Heroku.  Good use of auth on Django.  No real database yet, just sqlite.

##### Tests - good coverage?  Travis working?

You are a little light on tests but Travis is working.

##### Final code documentation

##### GitHub usage

Improving but still uploading files and you never got a proper .gitignore set up and pyc files removed from your repo.

#### Project difficulty in terms of lines of code, conceptual difficulty, non-CRUD features, degree of completion

You had a fairly simple app with not much non-CRUD.

#### Overall remarks

BIG improvement from previous iterations, good job guys!  You still are behind the other groups but are getting caught up.

**Grade: 85/100**
