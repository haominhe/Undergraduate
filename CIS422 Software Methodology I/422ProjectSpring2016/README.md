# Hadabase system for SafeRide requests and dispatch #



### Introduction for SafeRide Project ###

SafeRide is a service aims to uphold mission of providing a free and reliable assault prevention shuttle service to the students, faculty and staff of the University of Oregon who would otherwise walk alone at night and risk possible assault.

We are building a web based application that makes SafeRide requesting service more efficient. Users can request rides on a computer or on their phones in moments instead of calling the SafeRide office. We have three sets of users. First set of users are people requesting rides, the second set of users are dispatchers/headquarter at SafeRide, and the third set of users are van drivers.

[For your information - This is a class project (project for CIS 422 Spring 2016) but with a real client, and that the client is the UO SafeRide system that provides scheduled rides to UO students and staff within a certain area.]

For project overview and application architecture, please refer to our wiki page: https://bitbucket.org/davidzimmerly/422saferide/wiki/Home 

Client side user manual: https://bitbucket.org/davidzimmerly/422saferide/wiki/Client_Pages

Dispatcher side user manual: https://bitbucket.org/davidzimmerly/422saferide/wiki/Headquarter_Pages

Driver side user manual:
https://bitbucket.org/davidzimmerly/422saferide/wiki/Driver_Pages

### Detailed information ###

For source code base, please visit: https://bitbucket.org/davidzimmerly/422saferide/src

Concept of operations: 
https://bitbucket.org/davidzimmerly/422saferide/wiki/Concept_of_Operations

Code organization:

Please also see client page, headquarter page, and driver page in wiki.

![2391181895-Picture20.png](https://bitbucket.org/repo/azzoa5/images/1214352788-2391181895-Picture20.png)

### Preparing installation on a shared Linux server ###

(Here, we use ix.cs.uoregon.edu, a shared ubuntu server, as an example) 

**FOR LATEST BUILD (currently behind on heroku build):

http://ix.cs.uoregon.edu:6508

http://ix.cs.uoregon.edu:6508/dispatch

**
Install Instructions**

(database install optional)

to install your own on your unix server:
-. set up mongodb (outside scope of this tutorial, mlabs makes it easy though and accounts are free)

-. clone repo

-. run make

-. edit the CONFIG.pyBASE to point to your database (if you want, pretty sure it will work okay if you don't want to install your own database), copy to CONFIG.py

-. create and activate a Python virtual environment:

```
#!bash

. env/bin/activate 

```


-. then run:


```
#!bash

python main.py


```

-. if you are missing for something you added run pip install <dependency> on each one as needed.


-. and then you can access it with the browser with the port it assigns. if you want it to stay running you can add a & after, like:

```
#!bash

python main.py &

```

-. and it will run after you logout (must actually logout), until you kill the process (ps -ux finds old processes, kill pid to cancel one)


### Preparing a Heroku installation ###


Client side prototype link:
https://hadabase.herokuapp.com/

Server side prototype link:
https://hadabase.herokuapp.com/dispatch

(You may need this website for further instruction: https://toolbelt.heroku.com/)



**To enable gunicorn & heroku:**

-. install heroku toolbelt, get heroku account
```
#!bash
 heroku login
```
-. clone repsoitory on your system (locally)
-. navigate to folder
-. create a virtual environment on your system and activate:
```
#!bash
virtualenv env
. env/bin/activate
```

```
#!bash

pip3 install -r requirements.txt 

```

-. heroku create applicationname

```
#!bash

git push heroku master

heroku open

```

(will open https page with address in browser)

---------------------------------------------------------
### Dispatch page access ###

Temporary dispatch page user name and password:

User name: admin

Password: password

### Drivers page access ###

We are providing an interface for drivers as well.

Temporary drivers page user name and password:

User name: driver1        

Password: vdriver1


User name: driver2        

Password: vdriver2


User name: driver3        

Password: vdriver3


User name: driver4        

Password: vdriver4


---------------------------------------------------------
### Developers contact information ###

If you have any questions, feel free to contact us (Hadabase).

Haomin He: hhe6@uoregon.edu

Andy Smith: asmith15@uoregon.edu

David A Zimmerly: daz@uoregon.edu