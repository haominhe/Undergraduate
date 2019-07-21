"""
Configuration of 'memos' Flask app. 
Edit to fit development or deployment environment.

"""
import random 
from passlib.apps import custom_app_context
### My local development environment

#--------------------------------------------------------------------------------------------#
#--------------------Configuration Variables-------------------------------------------------#
#--------------------------------------------------------------------------------------------#
test = True   # this will enable test menus on templates and unlock the test functions
phone = False  # this will enable/disable texting feature
#--------------------------------------------------------------------------------------------#


PORT=6528
DEBUG = False
#MONGO_URL = "mongodb://tracker:greentea56@ix.cs.uoregon.edu:4293/memos"  # on Gnat

### On ix.cs.uoregon.edu (David Zimmerly's instance of MongoDB)
#PORT=random.randint(5000,8000)
#DEBUG = False # Because it's unsafe to run outside localhost
#MONGO_URL =  "mongodb://SafeRider29210556:q567njiPOg6@ix.cs.uoregon.edu:4014/safe"  # on ix
MONGO_URL =  "mongodb://SafeRider29210556:q567njiPOg6@ds013192.mlab.com:13192/safe" #on mlab
GOOGLE_DISTANCE_API_KEY = "AIzaSyBah6_83Y6pDFnDNxIyvM8pG0bJKEr9uL0"
GOOGLE_MAPS_API_KEY = "AIzaSyC7UxEWiniVER3jS3MJpdp0FMhlIKaNccA"
HASH_KEY = custom_app_context.encrypt("password")
v1_KEY = custom_app_context.encrypt("vdriver1")
v2_KEY = custom_app_context.encrypt("vdriver2")
v3_KEY = custom_app_context.encrypt("vdriver3")
v4_KEY = custom_app_context.encrypt("vdriver4")
EKEY = 'This is a key123'
IV = 'This is an IV456'
home_address = "1228 University St" #saferide's home address
# twilio credentials:
ACCOUNT_SID = "ACd9b14134aa8fea763e8347139cb6b549" 
AUTH_TOKEN = "5952071fa40f5678768a0ef26196e2dc" 
sKey = 'A0Zr98j/3y9964RHH!jmN]LWX/,?RT'
