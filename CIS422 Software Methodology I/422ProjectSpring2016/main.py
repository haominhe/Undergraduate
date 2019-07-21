"""
Flask web app connects to Mongo database.
Keep a simple list of dated memoranda.

Representation conventions for dates: 
   - In the session object, date or datetimes are represented as
   ISO format strings in UTC.  Unless otherwise specified, this
   is the format passed around internally. Note that ordering
   of ISO format strings is consistent with date/time order
   - User input/output is in local (to the server) time
   - Database representation is as MongoDB 'Date' objects
   Note that this means the database may store a date before or after
   the date specified and viewed by the user, because 'today' in
   Greenwich may not be 'today' here. 
"""

import flask
from flask import Flask, render_template, redirect, request, url_for, make_response, session

import json
import logging
import random


# Date handling 
import arrow # Replacement for datetime, based on moment.js
import datetime # But we may still need time
from dateutil import tz  # For interpreting local times

# Mongo database
from pymongo import MongoClient
import re #regex for removing non numeric data from string

###
# Globals
###
import CONFIG
import urllib
import flask_sslify
import os
from twilio.rest import TwilioRestClient 

app = flask.Flask(__name__)

 #On Heroku, debugging must be off to run https
if 'DYNO' in os.environ: 
    app.debug=False
    sslify = flask_sslify.SSLify(app)
else:
    app.debug=CONFIG.DEBUG


try:
    app.logger.debug("Opening mongo client")
    dbclient = MongoClient(CONFIG.MONGO_URL)
    db = dbclient.safe
    collection = db.dated
    app.logger.debug("Successfully opened mongo")
except:
    print("Failure opening database.  Is Mongo running? Correct password?")
    sys.exit(1)

#import uuid
app.secret_key = CONFIG.sKey


from geopy.geocoders import Nominatim
geolocator = Nominatim()
import shapely.geometry
import requests  #for the API request json handling

from passlib.apps import custom_app_context     #password
from Crypto.Cipher import AES
from flask import jsonify # For AJAX transactions

#
# keeping track of these two lists when autoscheduling forms our data for priority queue structure
#
van_number_list = ['intialization_data']
free_time_list = ['intialization_data']
new_entry_list=[]

@app.route("/_count_vans")
def _count_vans():
  log("VAN COUNT\n")

  van_number_list = []

  van1 = request.args.get('van1', 0, type=int)
  van2 = request.args.get('van2', 0, type=int)
  van3 = request.args.get('van3', 0, type=int)
  van4 = request.args.get('van4', 0, type=int)

  if (van1 == 1):
    van_number_list.append(1)
    flask.session['van1operating'] = 1
  else:
    flask.session['van1operating'] = 0 
  if (van2 == 1):
    van_number_list.append(2)
    flask.session['van2operating'] = 1
  else:
    flask.session['van2operating'] = 0 
  if (van3 == 1):
    van_number_list.append(3)
    flask.session['van3operating'] = 1
  else:
    flask.session['van3operating'] = 0 
  if (van4 == 1):
    van_number_list.append(4)
    flask.session['van4operating'] = 1
  else:
    flask.session['van4operating'] = 0 

  log(str(van_number_list) + "\n")

  end_of_day()


  return jsonify(result=0)


@app.route("/_test")
def _test():
  a = request.args.get('a', 0, type=int)
  return jsonify(result=a)

@app.route("/_get_a_new_entry")
def _get_a_new_entry():
  current = len(new_entry_list)
  if (current>0):
    temp = new_entry_list.pop()
    if current==len(new_entry_list):
      new_entry_list.pop()
    #print("returning "+str(temp))
    return(jsonify(result={"id":temp['id'], "time":temp['time'], "name":temp['tname'], "pickup":temp['pickup'], "dropoff":temp['dropoff'], "phone":temp['phone'], "comments":temp['comments'], "bike":temp['bike'], "uoid":temp['uoid'], "riders":temp['riders'], "platlong":temp['platlong'], "dlatlong":temp['dlatlong'], "hour":temp['hour'], "minute":temp['minute']}))
  else:
    #print("returning nothing?")
    return(jsonify(result=0))










@app.route("/_delete_record")
def _delete_record():
  the_id = request.args.get('the_id', 0, type=str)
  the_div = request.args.get('the_div', 0, type=str)
  try: 
        
    delete_id(the_id)
  except:
    return "(memo not found?)"
  return jsonify(result=the_div)

@app.route("/_text_message")
def _text_message():
  number = request.args.get('the_number', 0, type=str)
  message = request.args.get('the_message', 0, type=str)
  client = TwilioRestClient(CONFIG.ACCOUNT_SID, CONFIG.AUTH_TOKEN) 
  client.messages.create(to=number,from_="+15412142386",body=message)
  return jsonify(result=1)



to_encrypt = ['name', 'uoid', 'comments','phone']
@app.route("/_modify_db")
def _modify_db():
  the_id = request.args.get('the_id', 0, type=str)
  the_field = request.args.get('the_field', 0, type=str)
  #the_div = request.args.get('the_div', 0, type=str)
  new_stuff = request.args.get('new_stuff', 0, type=str)
  for check_me in to_encrypt:
    if the_field==check_me:
        new_stuff = encrypt_stuff(new_stuff)

  try: 
    modify_db(the_id,the_field,new_stuff)
  except:
    return "(memo not found?)"
  return jsonify(result=1)


@app.route("/_return_record_from_db")
def _return_record_from_db():
  the_id = request.args.get('the_id', 0, type=str)
  record = collection.find_one({ "type": "dated_memo", "my_id":the_id})
  record['name'] = decrypt_stuff(record['name'])
  record['phone'] = decrypt_stuff(record['phone'])
  record['phone'] = phonenumber(record['phone'])
  record['uoid'] = decrypt_stuff(record['uoid'])
  record['uoid'] = formatUOID(record['uoid'])
  record['comments'] = decrypt_stuff(record['comments'])
  
         

  # we return just the needed data to display that we have pre formatted and decrypted.
  return jsonify(result={"name":record["name"], "phone":record["phone"],"uoid":record["uoid"],"time":record["time"],"riders":record["riders"],"pickup":record["pickup"],"dropoff":record["dropoff"],"bike":record["bike"],"comments":record["comments"],"distance":record["distance"],"estimate":record["estimate"],"van":record["van"]})

@app.route("/_find_next_id")
def _find_next_id():
  search_id = request.args.get('id', 0, type=str)
  hour = request.args.get('hour', 0, type=str)
  minute = request.args.get('minute', 0, type=str)
  temp = "0"
  count = 0
  closestHour = 0
  closestMinute = 0
  closestID = ""
  isbeforeAll = True
  for record in collection.find( { "type": "dated_memo" } ):
    #print("searching record with id="+str(record['my_id']))
    try:
      
      if record['history']=="current":
        print("record['hour']= "+str(record['hour']))
        print("(hour)= "+str(hour))
        if int(record['hour'])<int(hour):
          print("lalalalalallalalalal")
          isbeforeAll=False
        if search_id!=record['my_id']:#errors here
          count=count+1  
          if int(hour)>int(record['hour']):
            closestID = record['my_id'] 
            closestID = closestID[2:]
          if int(record['hour'])>=closestHour and int(record['hour'])<=int(hour):
            print("0testing hour:"+str(record['hour'])+" minute: "+str(record['minute'])+ "id: "+str(record['my_id']))
            
            if int(record['hour'])==int(hour) and int(record['minute'])<=int(minute):#within the closest hour, but not past time
              print("00000")
              print("record['minute']= "+record['minute'])
              print("str(minute)= "+str(minute))
              closestID = record['my_id'] 
              closestID = closestID[2:]
              if int(record['minute'])==int(minute):
                print("if1")
                print("1testing hour:"+str(record['hour'])+" minute: "+str(record['minute'])+ "id: "+str(record['my_id']))
                closestHour = int(record['hour'])
                closestMinute = int(record['minute'])
                closestID = record['my_id'] 
                closestID = closestID[2:]
                break;
              if int(record['minute'])<int(minute) and int(record['minute'])>=closestMinute:#should be new closer
                print("if2")
                print("2testing hour:"+str(record['hour'])+" minute: "+str(record['minute'])+ "id: "+str(record['my_id']))
                closestHour = int(record['hour'])
                closestMinute = int(record['minute'])
                closestID = record['my_id'] 
                closestID = closestID[2:]
              #if int(record['minute'])>int(minute) and int(record['minute'])>closestMinute:  
              #else:
                #print("else")
                #closestHour = int(record['hour'])
                #closestID = record['my_id'] 
                #closestID = closestID[2:]
                #if int(record['minute'])>=closestMinute and int(record['minute'])>=int(minute):
                  #print("3testing hour:"+str(record['hour'])+" minute: "+str(record['minute'])+ "id: "+str(record['my_id']))
                  #closestHour = int(record['hour'])
                  #closestMinute = int(record['minute'])
                  #closestID = record['my_id'] 
                  #closestID = closestID[2:]
          ###elif int(record['hour'])>closestHour and int(record['hour'])int(hour):
          
        #elif int(record['hour'])==closestHour:
          #if int(record['minute'])<closestMinute

          #int(record['minute'])<closestMinute and int(record['hour'])<int(hour):
    except:
      print("some error???????")
  print("loop done")
  if count==0 and cloesetHour==0:
    closestID = search_id
    closestID = closestID[2:]
    closestHour=0#for test
    closestMinute=0    #for test
  elif count==0 or closestHour==0:
      if isbeforeAll==True:
        closestID = "#isbeforeall"
  
        
  print("hmmm")
  print("returning hour:"+str(closestHour)+" minute: "+str(closestMinute)+ "id: "+str(closestID))
  return jsonify(result=closestID)



# ajax route for returning a list of appointments for a specific van number
@app.route("/_find_van_schedule")
def _find_van_schedule():
  #the_id = request.args.get('the_id', 0, type=str)
  the_van = request.args.get('the_van', 0, type=int)
  pickups = []
  count = 0;
  first_day = 15  # Arbitrary day in the middle of the month to make display on chart between multiple days easy to read
  next_day = 16   # The day after first_day
  rollover_time = 4 # Arbitrary time between end of one shift and start of next day
  for record in collection.find( { "type": "dated_memo" } ).sort('ttime',1):
    try:
      if (int(record['van'])==the_van):
        count = count + 1
        pickups.append("Ride "+str(count))

        pickups.append(str(record['ttime'].year))
        pickups.append(str(record['ttime'].month))
        #pickups.append(str(record['ttime'].day))

        if (int(record['hour']) > rollover_time):
            pickups.append(str(first_day))
            start_hour = int(record['hour']) + 12
        else:
            pickups.append(str(next_day))
            start_hour = int(record['hour'])
        pickups.append(start_hour)
        pickups.append(record['minute'])

        trip_estimate = int(record['estimate'].split(' ')[0]) * 2 + 5   #Intentionally over estimates time for safety
        time_hours = start_hour
        time_minutes = trip_estimate + int(record['minute'])
        if (time_minutes > 60):
            time_minutes -= 60
            time_hours += 1
            if (time_hours > 23):
                time_hours -= 24
        record['next_time_hour'] = time_hours
        record['next_time_minute'] = time_minutes

        pickups.append(str(record['ttime'].year))
        pickups.append(str(record['ttime'].month))
        if (int(record['next_time_hour'])<rollover_time): #case of past midnight
            #pickups.append(str(record['ttime'].day+1))
            pickups.append(str(next_day))
        else:
            #pickups.append(str(record['ttime'].day))
            pickups.append(str(first_day))
        pickups.append(str(record['next_time_hour']))
        pickups.append(str(record['next_time_minute']))
        pickups.append("Pickup:"+record['pickup']+"<br>"+"Dropoff:"+record['dropoff'])
        
    except:
        pass
  
  return jsonify(results=pickups)

"""
find me, reverse geocode function, takes geolocate input, uses webapi and returns formatted address
"""
@app.route("/_find_address")
def _find_address():
  longi = request.args.get('the_longi', 0, type=float)
  lat = request.args.get('the_lat', 0, type=float)
  url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(lat)+','+str(longi)+'&key='+str(CONFIG.GOOGLE_DISTANCE_API_KEY)
  theStuff = requests.get(url)
  theJsonData = theStuff.json()
  temp = theJsonData['results'][0].get('formatted_address')
  t = temp.find(",")
  temp = temp[0:t]
  return jsonify(result = temp)





###
# Pages
###



#manually run the auto scheduler
@app.route("/auto")
def auto_schedule():#need to add input of #vans
    redirect_to_dispatch = redirect('/dispatch')      
    response = app.make_response(redirect_to_dispatch)  
    fill = 0;
    today_start = today_start_hour()
    today_end = today_end_hour()
    total_hours = 24-int(today_start)+int(today_end)
    minutes=['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
    hours = []
    # we set up hours array with todays hours
    for x in range(total_hours):
        nextHour = fill+today_start
        if nextHour>23:
            nextHour = nextHour-24
        hours.append(nextHour)
        fill = fill+1
    
    
    #clear lists
    while (len(van_number_list)>0):
        van_number_list.remove(van_number_list[0])
    while (len(free_time_list)>0):
        free_time_list.remove(free_time_list[0])
    
    # these need to come from input
    num_vans =4;
    
    
    #set up the initial queue with free vans at start time
    for index in range(num_vans): 
        insert_van_into_queue(int(index)+1,int(today_start)*100)#600 for 600 etc
    
    for hour in hours:
        for minute in minutes:
            pickup_ids = count_number_pickups(hour,int(minute))

            # after midnight fix for integer time representation
            mod_hour = hour
            if (hour<3):
                mod_hour = mod_hour+12
            time_int = mod_hour * 100+int(minute) #integer code for time for priority use
            
            #if len(pickups)>van_number_list: #catch excess riders here and deal with contacting and/or rescheduling

            for pickupid in pickup_ids:
                if (len(van_number_list)>0): #while we have vans in queue, don't schedule excess now deal with above, could remove this condition when properly deal with above.
                    #need to check assignment status here, and ignore if already assigned
                    record = collection.find_one({ "type": "dated_memo", "my_id":pickupid})
                    
                    if (record['van']=="" and record['pickup'] !="??" and record['dropoff'] !="??"):#entry has no assignment  #will need else blocks to handle exceptions
                        if (int(queue_min_time())<=time_int):#there is an available van at this timeslot #will need else blocks to handle exceptions
                            
                            van_to_assign = remove_min_from_queue()
                            
                            trip_estimate = record['estimate']
                            if trip_estimate=="????":
                                insert_van_into_queue(van_to_assign,time_int+30)# unknown locations,buffer 30 minutes    
                            else:
                                
                                modify_db(pickupid,"van",str(van_to_assign))

                                total_trip_estimate = calculate_total_trip_time(record['dropoff'],record['pickup'],trip_estimate)


                                #trip_estimate = re.sub("[^0-9^.]", "", trip_estimate) #gets rid of the 'min' in answer(example'7 minutes' -> '7', and we are assuming we're not getting hours due to boundary check and 'eugene, or' hardcoded.
                                #to_estimate = calculate_time_between_two_addresses(CONFIG.home_address,record['pickup'])
                                #to_estimate = re.sub("[^0-9^.]", "", to_estimate)
                                #from_estimate = calculate_time_between_two_addresses(record['dropoff'],CONFIG.home_address)
                                #from_estimate = re.sub("[^0-9^.]", "", from_estimate)
                                #total_trip_estimate = int(to_estimate)+int(trip_estimate)+int(from_estimate)
                                

                                # i thought integer time representation would simplify things, but perhaps i was mistaken..
                                if (total_trip_estimate%100>=60):
                                    new_time_for_van = int(time_int)+int(total_trip_estimate)-60+100
                                else:
                                    new_time_for_van = int(time_int)+int(total_trip_estimate)
                                if (new_time_for_van%100>=60):
                                    new_time_for_van = new_time_for_van -60+100  
                                record['next_time_hour'] = int(new_time_for_van/100)
                                record['next_time_minute'] = int(new_time_for_van%100)
                                record['total_trip_estimate'] = int(total_trip_estimate)
                                modify_db(pickupid,"total_trip_estimate",str(total_trip_estimate))
                                modify_db(pickupid,"next_time_minute",str(record['next_time_minute']))
                                modify_db(pickupid,"next_time_hour",str(record['next_time_hour']))
                                
                                #print("trip_estimate="+str(trip_estimate))
                                #print("to_estimate="+str(to_estimate))
                                #print("from_estimate="+str(from_estimate))
                                #print("+  =total_trip_estimate="+str(total_trip_estimate))
                                #print("(iteration)timeint="+str(time_int))
                                #print("new time for van:"+str(van_to_assign)+" is "+str(new_time_for_van))
                                insert_van_into_queue(van_to_assign,new_time_for_van)
                        
    
    return response

# route for logging out of dispatch, return to login
@app.route('/logout')
def logout():
    if (flask.session['logged_in']):
      flask.session['logged_in'] = False
      log("Dispatch logged out.")
    elif (flask.session['d1_logged_in']):
      flask.session['d1_logged_in'] = False
      log("Driver 1 logged out.")
    elif (flask.session['d2_logged_in']):
      flask.session['d2_logged_in'] = False    
      log("Driver 2 logged out.")
    elif (flask.session['d3_logged_in']):
      flask.session['d3_logged_in'] = False
      log("Driver 3 logged out.")
    elif (flask.session['d4_logged_in']):
      flask.session['d4_logged_in'] = False      
      log("Driver 4 logged out.")
    return redirect(url_for('login'))

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        the_name = request.form['username']
        if (the_name != 'admin' and the_name != 'driver1' and the_name != 'driver2' and the_name != 'driver3' and the_name != 'driver4'):# or request.form['password'] != 'admin':
            error = 'Invalid Username. Please try again.'#get rid of this step in final build, here for testing
        elif (the_name == 'admin' and custom_app_context.verify(request.form['password'], CONFIG.HASH_KEY)):
            log("Dispatch Logged In.\n")
            flask.session['logged_in'] = True
            flask.session['d1_logged_in'] = False #maintain state if multiple logins on same system
            flask.session['d2_logged_in'] = False
            flask.session['d3_logged_in'] = False
            flask.session['d4_logged_in'] = False
            return redirect(url_for('dispatch'))
        elif (the_name == 'driver1' and custom_app_context.verify(request.form['password'], CONFIG.v1_KEY)):
            log("Driver 1 Logged In.\n")
            flask.session['d1_logged_in'] = True
            flask.session['logged_in'] = False
            flask.session['d2_logged_in'] = False
            flask.session['d3_logged_in'] = False
            flask.session['d4_logged_in'] = False
            return redirect(url_for('driver'))
        elif (the_name == 'driver2'  and custom_app_context.verify(request.form['password'], CONFIG.v2_KEY)):
            log("Driver 2 Logged In.\n")
            flask.session['d2_logged_in'] = True
            flask.session['logged_in'] = False
            flask.session['d1_logged_in'] = False
            flask.session['d3_logged_in'] = False
            flask.session['d4_logged_in'] = False
            return redirect(url_for('driver'))
        elif (the_name == 'driver3'  and custom_app_context.verify(request.form['password'], CONFIG.v3_KEY)):
            log("Driver 3 Logged In.\n")
            flask.session['d3_logged_in'] = True

            flask.session['logged_in'] = False
            flask.session['d1_logged_in'] = False
            flask.session['d2_logged_in'] = False
            flask.session['d4_logged_in'] = False
            return redirect(url_for('driver'))
        elif (the_name == 'driver4'  and custom_app_context.verify(request.form['password'], CONFIG.v4_KEY)):
            log("Driver 4 Logged In.\n")
            flask.session['d4_logged_in'] = True
            flask.session['logged_in'] = False
            flask.session['d1_logged_in'] = False
            flask.session['d2_logged_in'] = False            
            flask.session['d3_logged_in'] = False
            return redirect(url_for('driver'))
        else:
            error = 'Invalid Password. Please try again.'#will combine these later, left 2 errors for testing purposes
    return render_template('login.html', error=error)



'''
TEST Clear Schuedule Completely function
'''
@app.route("/clear_schedule")
def clear_schedule():
    for record in collection.find( { "type": "dated_memo" } ):
        if (not(record['van']=="")):
            modify_db(record['my_id'],"van","")
    return redirect(url_for('dispatch'))
            
    

    
'''
TEST Write function
'''
@app.route("/testw")
def testw():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
        for entry in json_data:
            plat = entry.get('pickup_latitude')
            plongi = entry.get('pickup_longitude')
            url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(plat)+','+str(plongi)+'&key='+str(CONFIG.GOOGLE_DISTANCE_API_KEY)
            geo_locate_stuff = requests.get(url)
            ReverseGeoCodeJsonData = geo_locate_stuff.json()
            try:
                pickup = ReverseGeoCodeJsonData['results'][0].get('formatted_address')
                t=pickup.find(",")
                pickup=pickup[0:t]
            except:
                pickup = "??"
            dlat = entry.get('dropoff_latitude')
            dlongi = entry.get('dropoff_longitude')
            url2 = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(dlat)+','+str(dlongi)+'&key='+str(CONFIG.GOOGLE_DISTANCE_API_KEY)
            geo_locate_stuff2 = requests.get(url2)
            ReverseGeoCodeJsonData2 = geo_locate_stuff2.json()
            try:
                dropoff = ReverseGeoCodeJsonData2['results'][0].get('formatted_address')
                t=dropoff.find(",")
                dropoff=dropoff[0:t]
            except:
                dropoff = "??"


            hour = entry.get('hour')
            if (hour<3):
                hour = hour + 12;
            minute = entry.get('minute')
            minString = str(minute)
            if int(minute)<10:
                minString = "0"+str(minString)
            time = str(hour) + ":" + minString
            platlong = [plat, plongi]
            dlatlong = [dlat, dlongi]

            put_memo(time,str(entry.get('name')),str(entry.get('uoid')),'5416543745',str(dropoff),str(pickup),str(entry.get('riders')),"False","no comment - Fake Data","current",str(hour),minString,"True",platlong,dlatlong,True)
            

    return redirect(url_for('dispatch'))

@app.route("/")
@app.route("/index")
def index():
  app.logger.debug("Main page entry")
  flask.session['memos'] = get_memos()
  flask.session['findme'] = "false"
  log("OPENING INDEX PAGE\n")
  return flask.render_template('index.html')

@app.route("/test")
def test():
    flask.session['memos'] = get_memos()
    return flask.render_template('test.html')

@app.route("/dtallies")
def dtallies():
    if flask.session.get('logged_in') == True:
        flask.session['tallies'] = get_tallies()
        log("OPENING TALLY PAGE\n")
        return flask.render_template('dtallies.html')
    else:
        return redirect(url_for('login'))

@app.route("/dhistory")
def dhistory():
    if flask.session.get('logged_in') == True:
        flask.session['memos'] = get_memos()
        log("OPENING DHISTORY PAGE\n")
        return flask.render_template('dhistory.html')
    else:
        return redirect(url_for('login'))

@app.route("/dispatch")
def dispatch():
    if flask.session.get('logged_in') == True:
        flask.session['memos'] = get_memos()
        log("OPENING DISPATCH PAGE\n")
        return flask.render_template('dispatch.html')
    else:
        return redirect(url_for('login'))
    
@app.route("/dedit")
def dedit():
    if flask.session.get('logged_in') == True:
        flask.session['memos'] = get_edit_memos()
        log("OPENING DEDIT PAGE\n")
        return flask.render_template('dedit.html')
    else:
        return redirect(url_for('login'))

@app.route("/dispatchnew")
def dispatchnew():
    if flask.session.get('logged_in') == True:
        log("OPENING DISPATCHNEW PAGE\n")
        return flask.render_template('dispatchnew.html')
    else:
        return redirect(url_for('login'))

@app.route("/riderequest")
def riderequest():
    flask.session['memos'] = get_memos()
    flask.session['findme'] = "false"
    log("OPENING REQUEST PAGE\n")
    return flask.render_template('riderequest.html')

@app.route("/entry_confirmed")
def confirmed_entry():
    log("OPENING ENTRY_CONFIRMED PAGE\n")
    return flask.render_template('entry_confirmed.html')

@app.route("/out_of_bounds")
def out_of_bounds():
    log("OPENING OUT_OF_BOUNDS PAGE\n")
    return flask.render_template('out_of_bounds.html')

@app.route("/driver")
def driver():
    if ( (flask.session.get('d1_logged_in') == True) or (flask.session.get('d2_logged_in') == True) or (flask.session.get('d3_logged_in') == True) or (flask.session.get('d4_logged_in') == True)):
        log("OPENING DRIVER PAGE\n")
        flask.session['memos'] = get_memos()
        return flask.render_template('driver.html')
    else:
        return redirect(url_for('login'))



@app.route("/sendVanNumtoDB", methods=['POST'])
def sendVanNumtoDB():
    
    try: 
        modify_db(request.form["my_id"],"van",request.form["van"])
    except:
        return "(memo not found?)"
    flask.session['memos'] = get_memos()
    redirect_to_dispatch = redirect('/dispatch')        
    response = app.make_response(redirect_to_dispatch )

    return response






@app.route("/create2", methods=['POST'])
def create2():
    #log("create2():    In create2 function\n")
    redirect_to_confirm = redirect('/entry_confirmed')      
    response = app.make_response(redirect_to_confirm )     
    minute = request.form["time_minutes"]
    hour = request.form["time_hours"]
    print("create2 received hour:" + hour+" minute:"+minute)
    hour = hour[0:2]
    if (hour[1]==" "):
        hour = hour[0:1]
    time = hour + ":" + minute
    name = request.form["name"]
    uoid = request.form["uoid"].replace("-", "").replace(" ", "")
    phone = request.form["phone"].replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    dropoff = request.form["dropoff"]
    pickup = request.form["pickup"]
    platlong = None
    dlatlong = None

    pickup_info = find_coordinates(pickup)
    dropoff_info = find_coordinates(dropoff)
    showpickup = pickup_info[0]
    platlong = pickup_info[1]
    showdropoff = dropoff_info[0]
    dlatlong = dropoff_info[1]

    riders = request.form["optradio"]
    bike = request.form["bike"]
    rememberme = request.form["rememberme"]
    comments = request.form["comments"]
    history = "current"
    on_campus = "false"

    if ( (platlong != None) and (dlatlong != None) ):
        if ( (check_address_campus(platlong) == True) and (check_address_campus(dlatlong) == True) ):
            on_campus = "true"
    
    if (rememberme=="true"):
        flask.session['name'] = name
        flask.session['uoid'] = uoid
        flask.session['phone'] = phone
        flask.session['dropoff'] = dropoff
        flask.session['pickup'] = pickup
        flask.session['comments'] = comments
        flask.session['rememberme'] = rememberme
        flask.session['bike'] = bike
    else:
        flask.session['name'] = None
        flask.session['uoid'] = None
        flask.session['phone'] = None
        flask.session['dropoff'] = None
        flask.session['pickup'] = None
        flask.session['comments'] = None
        flask.session['rememberme'] = None
        flask.session['bike'] = None
              #checks the address to make sure is in boundaries
    if ( platlong != None ):
        pbounds = check_address( platlong )  
    else:
        pbounds = True
    if ( dlatlong != None ):
        dbounds = check_address( dlatlong)
    else:
        dbounds = True
    
    if ( (pbounds == False) or (dbounds == False) ):
        response1 = app.make_response(redirect('/out_of_bounds'))
        flask.session['platlong'] = platlong
        flask.session['showpickup'] = showpickup
        flask.session['dlatlong'] = dlatlong
        flask.session['showdropoff'] = showdropoff
        if (pbounds == False):
            flask.session['pbounds'] = False
        if (dbounds == False):
            flask.session['dbounds'] = False
        return response1
    else:
        #log("create2():    About to put_memo\n")
        
        
        #this will handle the database submission async, making it seem more responsive to user
        #threading.Thread(target=
        put_memo(time,name,uoid,phone,showdropoff,showpickup,riders,bike,comments,history,hour,minute,on_campus,platlong,dlatlong, False);
        return response  

"""
This function is idential to create2, except that it is used by dispatch instead of a client
except no functionality for a 'rememberme' and a different response page
"""
@app.route("/dcreate2", methods=['POST'])
def dcreate2():
    if flask.session.get('logged_in') == True:
        redirect_to_dispatch = redirect('/dispatch')        
        response = app.make_response(redirect_to_dispatch )     
        minute = request.form["time_minutes"]
        hour = request.form["time_hours"]
        hour = hour[0:2]
        if (hour[1]==" "):
            hour = hour[0:1]
        time = hour + ":" + minute
        name = request.form["name"]
        uoid = request.form["uoid"].replace("-", "").replace(" ", "")
        phone = request.form["phone"].replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        dropoff = request.form["dropoff"]
        pickup = request.form["pickup"]
        riders = request.form["optradio"]
        bike = request.form["bike"]
        comments = request.form["comments"]

        pickup_info = find_coordinates(pickup)
        dropoff_info = find_coordinates(dropoff)
        showpickup = pickup_info[0]
        platlong = pickup_info[1]
        showdropoff = dropoff_info[0]
        dlatlong = dropoff_info[1]
       
        history = "current"
        on_campus = "false"

        if ( (platlong != None) and (dlatlong != None) ):
            if ( (check_address_campus(platlong) == True) & (check_address_campus(dlatlong) == True) ):
                on_campus = "true"

        put_memo(time,name,uoid,phone,showdropoff,showpickup,riders,bike,comments,history,hour,minute,on_campus,platlong,dlatlong, False)
        return response  
    else:
        return redirect(url_for('login'))

@app.route("/savechanges", methods=['POST'])
def savechanges():
    if flask.session.get('logged_in') == True:
        redirect_to_dispatch = redirect('/dispatch')
        response = app.make_response(redirect_to_dispatch )
        time = request.form["time"]
        name = request.form["name"]
        uoid = request.form["uoid"]
        phone = request.form["phone"]
        dropoff = request.form["dropoff"]
        pickup = request.form["pickup"]
        riders = request.form["riders"]
        bike = request.form["bike"]
        comments = request.form["comments"]
    
        pickup_info = find_coordinates(pickup)
        dropoff_info = find_coordinates(dropoff)
        showpickup = pickup_info[0]
        platlong = pickup_info[1]
        showdropoff = dropoff_info[0]
        dlatlong = dropoff_info[1]

        name = encrypt_stuff(name)
        uoid = encrypt_stuff(uoid)
        comments = encrypt_stuff(comments)
        phone = encrypt_stuff(phone)
     
        id_to_modify = request.form["my_id"]
        on_campus = "false"

        if ( (platlong != None) and (dlatlong != None) ):
            if ( (check_address_campus(platlong) == True) & (check_address_campus(dlatlong) == True) ):
                on_campus = "true"

        update(id_to_modify,time,name,uoid,phone,showdropoff,showpickup,riders,bike,comments,on_campus,platlong,dlatlong)
        return response
    else:
        return redirect(url_for('login'))


'''
TEST FUNCTION(REMOVE IN FINAL): deletes all the records using the delete method
'''
@app.route("/testd")
def testd():
    
    redirect_to_dispatch = redirect('/dispatch')        
    response = app.make_response(redirect_to_dispatch )     
    for record in collection.find( { "type": "dated_memo" } ):
        delete_id(record['my_id'])
    return response

'''
TEST FUNCTION(REMOVE IN FINAL): deletes all the tallies using the delete method
'''
@app.route("/deltallies")
def deltallies():
    
    redirect_to_dtallies = redirect('/dtallies')        
    response = app.make_response(redirect_to_dtallies )     
    collection.remove( {"type" : "tally"} )
    return response






'''
this handles the put item into history request
'''
@app.route("/puthistory", methods=['POST'])
def puthistory():
    if flask.session.get('logged_in') == True:
        redirect_to_dispatch = redirect('/dispatch')        
        response = app.make_response(redirect_to_dispatch )  
        try: 
            id_to_modify = request.form["my_id"]
            modify_db(id_to_modify,"history","old")
        except:
            return "(memo not found?)"
        return response
    else:
        return redirect(url_for('login'))
'''
this handles the take item from history request
'''
@app.route("/takehistory", methods=['POST'])
def takehistory():
    if flask.session.get('logged_in') == True:
        redirect_to_dhistory = redirect('/dhistory')        
        response = app.make_response(redirect_to_dhistory )  
        try: 
            modify_db(request.form["my_id"],"history","current")
        except:
            return "(memo not found?)"
        return response
    else:
        return redirect(url_for('login'))


'''
this handles the edit item reqeust
'''
@app.route("/editrecord", methods=['POST'])
def editrecord():
    if flask.session.get('logged_in') == True:
        redirect_to_dedit = redirect('/dedit')
        response = app.make_response(redirect_to_dedit )
        try:
            modify_db(request.form["my_id"],"history","editing")
        except:
            return "(memo not found?)"
        return response 
    else:
        return redirect(url_for('login'))


'''
this handles the delete request
'''
@app.route("/delete", methods=['POST'])
def deleteRecord():
    if flask.session.get('logged_in') == True:
        redirect_to_dispatch = redirect('/dispatch')        
        response = app.make_response(redirect_to_dispatch )  
        try: 
            delete_id(request.form["my_id"])
        except:
            return "(memo not found?)"
        return response
    else:
        return redirect(url_for('login'))

'''
this handles the end of day routines
'''
#@app.route("/endofday")
def end_of_day():
    if flask.session.get('logged_in') == True:
        #log("Doing end of day routines\n")
        redirect_to_dhistory = redirect('/dhistory')
        response = app.make_response(redirect_to_dhistory )
        #log("Doing end of day tally\n")
        tally_results()
        #log("Doing end of day merge_geocache\n")
        merge_geocache()
        return response
    else:
        return redirect(url_for('login'))


'''
this handles the end of day tally
'''
def tally_results():
    num_rides = 0
    num_oncampus = 0
    num_offcampus = 0
    
    for record in collection.find( { "type": "dated_memo" } ).sort('ttime',1):
        record['date'] = arrow.get(record['date']).isoformat()
        
        if (record['history']=="old"):
            num_rides += 1
            if (record['oncampus']=="true"):
                num_oncampus += 1
            else:
                num_offcampus += 1

    log("End of day:    number of rides = " + str(num_rides) + "\n      number on campus = " + str(num_oncampus) + "\n      number off campus = " + str(num_offcampus) + "\n")

    dateSet = arrow.utcnow().to('US/Pacific')
    record = { "type": "tally", 
               "date": dateSet.to('utc').naive,
               "numrides": num_rides,
               "num_oncampus":num_oncampus,
               "num_offcampus":num_offcampus
             }
    collection.insert(record)
    for record in collection.find( { "type": "dated_memo" } ):
        if (record['history']=="old"):
                delete_id(record['my_id'])
    return

'''
this handles merging the new geocache with the old one
'''
def merge_geocache():
    old_cache = open("geocache.json", 'r')
    old_data = json.load(old_cache)
    old_cache.close()

    #log("merge_geocache():    opening new geocache file\n")
    with open("new_geocache.json",'r') as new_data:
        for line in new_data:
            line = line.strip('\n')
            #log("    " + line + "\n")
            new_value = True
            #log("merge_geocache():    about to load line into new_entry\n")
            new_entry = json.loads(line)
            #log("    Success\n")
            new_coords = new_entry['latlong']
            #log("merge_geocache():    coords = " + str(new_coords) + "\n")
            for old_entry in old_data:
                old_coords = old_entry.get('latlong')
                if (old_coords == new_coords):
                    #log("merge_geocache():    found coordinate match in geocache\n")
                    old_entry['alt_names'].append(new_entry['alt_names'][0])
                    new_value = False
                    break

            if (new_value == True):
                old_data.append(new_entry)
        
    old_cache = open("geocache.json", 'w')
    json.dump(old_data, old_cache)
    old_cache.close()

    new_cache = open("new_geocache.json",'w')
    new_cache.write( "" )
    new_cache.close()

    return

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('page_not_found.html',
                                 badurl=request.base_url,
                                 linkback=url_for("index")), 404

#################
#
# Functions used within the templates
#
#################


@app.template_filter( 'is_this_current_term' )
def is_this_current_term(input):
  if (input==current_term()):
    return True
  else:
    return False




#
#  This template will display 10 digit number as phone number 
#
@app.template_filter( 'phonenumber' )
def phonenumber( input ):
    output1 = input[0:3]
    output2 = input[3:6]
    output3 = input[6:10]
    output = "("+output1+")"+output2+"-"+output3
    return output

#
#  This template will display 10 digit number as phone number 
#
@app.template_filter( 'formatUOID' )
def formatUOID( input ):
    output1 = input[:3]
    output2 = input[3:6]
    output3 = input[-3:]

    output = output1+"-"+output2+"-"+output3
    return output






# NOT TESTED with this application; may need revision 
#@app.template_filter( 'fmtdate' )
# def format_arrow_date( date ):
#     try: 
#         normal = arrow.get( date )
#         return normal.to('local').format("ddd MM/DD/YYYY")
#     except:
#         return "(bad date)"

@app.template_filter( 'humanize' )
def humanize_arrow_date( date ):
    """
    Date is internal UTC ISO format string.
    Output should be "today", "yesterday", "in 5 days", etc.
    Arrow will try to humanize down to the minute, so we
    need to catch 'today' as a special case. 
    """
    try:
        then = arrow.get(date).to('local')
        now = arrow.utcnow().to('local')
        if then.date() == now.date():
            human = "Today"
        else: 
            human = then.humanize(now)
            if human == "in a day":
                human = "Tomorrow"
    except: 
        human = date
    return human


#
# This filter will decrypt an item using the sites' key to the jinja2 interface
# To use this functionality inside python, just call the function
#
@app.template_filter( 'decryptMe' )
def decrypt_stuff( to_decrypt ):
    decryption_suite = AES.new(CONFIG.EKEY, AES.MODE_CBC, CONFIG.IV)
    decrypted_stuff = decryption_suite.decrypt( to_decrypt )
    output = unpad_string ( decrypted_stuff )
    return output



#############
#
# Functions available to the page code above
#
##############

def calculate_total_trip_time(from_address, to_address, trip_estimate):
  trip_estimate = re.sub("[^0-9^.]", "", trip_estimate) #gets rid of the 'min' in answer(example'7 minutes' -> '7', and we are assuming we're not getting hours due to boundary check and 'eugene, or' hardcoded.
  to_estimate = calculate_time_between_two_addresses(CONFIG.home_address,to_address)
  to_estimate = re.sub("[^0-9^.]", "", to_estimate)
  from_estimate = calculate_time_between_two_addresses(from_address,CONFIG.home_address)
  from_estimate = re.sub("[^0-9^.]", "", from_estimate)
  total_trip_estimate = int(to_estimate)+int(trip_estimate)+int(from_estimate)
  return total_trip_estimate



def delete_id(id_to_delete):
    '''
    delete collection item with my_id string
    '''
    collection.remove({ "my_id": id_to_delete }) 
    return



def modify_db(id_to_modify,field_to_modify,value):
    '''
    change id_to_modify's field_to_modify to value
    this can be used for any database modification we need currently.
    '''
    if (field_to_modify=="name" or field_to_modify=="uoid" or field_to_modify=="comments" or field_to_modify=="phone"):
        encrypt_stuff(value)

    collection.update_one(
    {"my_id": id_to_modify},
    { "$set": {field_to_modify:value}})
    return    

def check_address_campus( coordinates ):
    """
    checks string address to see if the address is in the campus boundary
    returns boolean
    """   
    point = shapely.geometry.Point( coordinates[1], coordinates[0] )
    polygon = shapely.geometry.Polygon([ (-123.085155,44.049596),(-123.077344,44.049534),(-123.070778,44.04975),(-123.067259,44.04938),(-123.065457,44.048825),(-123.064727,44.048485),(-123.065457,44.047005),(-123.063097,44.046881),(-123.060822,44.045555),(-123.060736,44.043118),(-123.065242,44.04281),(-123.065328,44.040712),(-123.068461,44.040681),(-123.068375,44.03883),(-123.080863,44.038953),(-123.085327,44.047838),(-123.085155,44.049596)])
    return (polygon.contains(point))

def check_address( coordinates ):
    """
    checks string address to see if the address is in the boundary
    returns boolean
    """   
    point = shapely.geometry.Point( coordinates[1], coordinates[0] )

    polygon = shapely.geometry.Polygon([ (-123.1002188, 44.0776585), (-123.1005192, 44.0701663), (-123.10433860000002, 44.0701971), (-123.1060553, 44.0709988), (-123.112363799999983, 44.0712146), (-123.1124496, 44.0639374), (-123.117299100000011, 44.0639991), (-123.117384900000019, 44.0570603), (-123.118457800000016, 44.0555491), (-123.118457800000016, 44.0521255), (-123.122792200000021, 44.0522181), (-123.122921, 44.0478381), (-123.127856300000019, 44.047869), (-123.1278133, 44.0308088), (-123.128242500000013, 44.0302225), (-123.1299591, 44.0296671), (-123.1315899, 44.0296671), (-123.1321478, 44.0293895), (-123.132576900000018, 44.0296054), (-123.133993100000012, 44.0296054), (-123.134594, 44.0292969), (-123.134851500000011, 44.0286798), (-123.133950199999987, 44.0284638), (-123.131504099999987, 44.0289266), (-123.126268399999987, 44.0285563), (-123.1246376, 44.0273221), (-123.1178999, 44.0270752), (-123.1178999, 44.0236809), (-123.1172132, 44.021922), (-123.1171703, 44.0210888), (-123.117857, 44.0201938), (-123.1179428, 44.0149165), (-123.114960199999985, 44.0148085), (-123.107686, 44.0157652), (-123.1075788, 44.0176787), (-123.09257980000001, 44.0177867), (-123.0926657, 44.0114289), (-123.082602, 44.0113209), (-123.0749846, 44.0113671), (-123.074383699999984, 44.0121079), (-123.0734396, 44.0122314), (-123.0723238, 44.0130647), (-123.0724096, 44.014361), (-123.071808800000014, 44.0147313), (-123.072624200000021, 44.0169226), (-123.072753, 44.0216442), (-123.072238, 44.0216134), (-123.0721951, 44.0241129), (-123.0628395, 44.0240821), (-123.059792500000015, 44.0286181), (-123.060565, 44.0288649), (-123.060865400000012, 44.030346), (-123.0598783, 44.0311482), (-123.0561018, 44.0311173), (-123.056016, 44.0285563), (-123.0542564, 44.0284329), (-123.052067799999989, 44.0290809), (-123.0519819, 44.031179), (-123.0505657, 44.031179), (-123.050050700000014, 44.0412059), (-123.048977900000011, 44.0633515), (-123.0482054, 44.0696113), (-123.044986699999981, 44.0698271), (-123.042154300000021, 44.0706905), (-123.0421114, 44.0768569), (-123.0475187, 44.0768877), (-123.04842, 44.0696729), (-123.051939, 44.0697963), (-123.0639982, 44.0695804), (-123.0652857, 44.0691796), (-123.069577200000012, 44.0697346), (-123.0694485, 44.0774735), (-123.1002188, 44.0776585) ])
    return (polygon.contains(point))

def update(id_to_modify,time,name,uoid,phone,dropoff,pickup,riders,bike,comments,on_campus,pickup_coords,dropoff_coords):
    """
    function for updating data via the dispatch window
    """
    collection.update_one(
    {"my_id": id_to_modify},
    { "$set": {"history": "current",
               "time": time,
               "name": name,
               "uoid": uoid,
               "phone": phone,
               "dropoff": dropoff,
               "dlatlong": dropoff_coords,
               "pickup": pickup,
               "platlong": pickup_coords,
               "riders": riders,
               "bike": bike,
               "comments": comments,
               "oncampus": on_campus }})
    return




def get_edit_memos():
    """
    Returns all memos in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    records = [ ]
    for record in collection.find( { "type": "dated_memo" } ).sort('ttime',1):
        record['date'] = arrow.get(record['date']).isoformat()
        del record['_id']
        records.append(record)
    return records 

def format_address(address1):
    """
    this function will interface with the Google Maps Geocoding API 
    input : string address
    output : list containing formatted address and the coordinates of the address, or None
    """
    if (address1 == ""):
        return(address1)
    address = address1.replace(" ","+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+str(address)+"Eugene+%20OR&key="+CONFIG.GOOGLE_DISTANCE_API_KEY
    theStuff = requests.get(url)
    theJsonData = theStuff.json()
    try:
        if (theJsonData != None):
            #log("format_address():   Formatted " + address1 + " --> " + str(theJsonData['results'][0]['formatted_address']) + "\n")
            #log("\nformat_address():\n\n" + str(theJsonData) + "\n\n")
            return( [ theJsonData['results'][0]['formatted_address'], theJsonData['results'][0]['geometry']['location']['lat'], theJsonData['results'][0]['geometry']['location']['lng'] ])
        else:
            log("format_address():   Could not format " + address1 + "\n")
            return(None)
    except:
        log("format_address():   Could not format " + address1 + "\n")
        return(None)
    

def clean_address(address):
    """
    this function will remove extraneous information from address names for comparing addresses to geocache
    input : string address
    output : cleaner address
    """
    address = address.split(",")[0]
    address =  address.lower()
    cleaned = ""
    for letter in address:
        if letter.isalnum():
            cleaned += letter
    return cleaned

def find_coordinates(address):
    """
    this function will perform all the actions to clean the address's name and to find an address's coordinates
    input : string address
    output : if coordinates are found --> [clean name, coordinates]
                                 else --> [clean name, None]
    """
    json_file = open("geocache.json", 'r')
    json_data = json.load(json_file)
    json_file.close()
    address_name = clean_address(address.split(',')[0])
    for entry in json_data:
        alt_names = entry.get('alt_names')
        if (address_name in alt_names):
            proper_name = entry.get('name')
            address_coords = entry.get('latlong')
            data = [proper_name, address_coords]
            #log("\nfind_coordinates():    " + proper_name + " is a geocache hit\n")
            #log("find_coordinates():    " + data[0] + " has coordinates " + str(data[1]) + "\n")
            return data

    show_address = address.split(',')[0]
    address_location = format_address(address)
    if (address_location != None):
        address_coords = [address_location[1], address_location[2]]
        #log("find_coordinates():    adding new entry to geocache\n")
        new_cache = open("new_geocache.json", 'a')
        new_hit = '{ "name" : "' + show_address + '", "alt_names" : ["' + clean_address(show_address) + '"], "latlong" : ' + str(address_coords) + '}'
        #log("find_coordinates():    " + new_hit + "\n")
        new_cache.write(new_hit + "\n")
        new_cache.close()

    else:
        #log("\nfind_coordinates():    " + show_address + " cannot geolocate\n")
        address_coords = None
    data = [show_address, address_coords]
    return data

def estimate_distance(id_to_modify,platlong,dlatlong):
    """
    this function will interface with the Google Distance Matrix API 
    input will be the 2 pairs of coordinates 
    will update database with output time estimate and distance
    """
    #pickup = pickup.replace(" ","+")
    #dropoff = dropoff.replace(" ","+")
    #url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+str(pickup)+"Eugene+%20OR&destinations="+str(dropoff)+"Eugene+%20OR&mode=driving&key="+CONFIG.GOOGLE_DISTANCE_API_KEY 
    if ( (platlong == None) or (dlatlong == None) ):
        return
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+str(platlong[0])+","+str(platlong[1])+"&destinations="+str(dlatlong[0])+","+str(dlatlong[1])+"&mode=driving&key="+CONFIG.GOOGLE_DISTANCE_API_KEY
    theStuff = requests.get(url)
    theJsonData = theStuff.json()
    try:
        distance = theJsonData['rows'][0]['elements'][0]['distance']['text']
        estimate = theJsonData['rows'][0]['elements'][0]['duration']['text']
        
    except:
        #print("address(s) not found")
        return
    modify_db(id_to_modify,"distance",distance)
    modify_db(id_to_modify,"estimate",estimate)
    return

def calculate_time_between_two_addresses(a,b):
    a = a.replace(" ","+")
    b = b.replace(" ","+")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+str(a)+"Eugene+%20OR&destinations="+str(b)+"Eugene+%20OR&mode=driving&key="+CONFIG.GOOGLE_DISTANCE_API_KEY
    theStuff = requests.get(url)
    theJsonData = theStuff.json()
    try:
        estimate = theJsonData['rows'][0]['elements'][0]['duration']['text']
        
    except:
        #print("address(s) not found")
        return
    return (estimate)
    
def get_memos():
    """
    Returns all memos in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    now = arrow.utcnow().to('US/Pacific')
    flask.session['today']=now.format('ddd')
    flask.session['todayopen'] = today_start_hour()-12
    temp = int(today_end_hour())
    if (temp==0):
        temp = 12
    flask.session['todayclose'] = temp
    flask.session['term'] = current_term()
    flask.session['test_enabled'] = CONFIG.test
    flask.session['phone_enabled'] = CONFIG.phone
    records = [ ]
    for record in collection.find( { "type": "dated_memo" } ).sort('ttime',1):
        record['date'] = arrow.get(record['date']).isoformat()
        
        if (record['history']=="editing"):
            modify_db(record['my_id'],"history","current")
            record['history']="current"
        del record['_id']
        records.append(record)
    
    return records 



def get_tallies():
    """
    Returns all tallies in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    log("get_tallies():    Attemtping to get tally\n")
    now = arrow.utcnow().to('US/Pacific')
    flask.session['today']=now.format('ddd')
    flask.session['todayopen'] = today_start_hour()-12
    temp = int(today_end_hour())
    if (temp==0):
        temp = 12
    flask.session['todayclose'] = temp
    flask.session['term'] = current_term()
    records = [ ]
    for record in collection.find( { "type": "tally" } ).sort('date',1):
        #record['date'] = arrow.get(record['date']).isoformat()
        del record['_id']
        records.append(record)
    
    #for record in records:
    #    log("get_tallies():    Type = " + str(record['type']) + "\n")
    #    log("get_tallies():    Date = " + str(record['date']) + "\n")
    #    log("get_tallies():    Num Rides = " + str(record['numrides']) + "\n")
    #    log("get_tallies():    On Campus = " + str(record['num_oncampus']) + "\n")
    #    log("get_tallies():    Off Campus = " + str(record['num_offcampus']) + "\n")
    
    return records 





def put_memo(time,name,uoid,phone,dropoff,pickup,riders,bike,comments,history,hour,minute,on_campus,pickup_coords,dropoff_coords,testing):
     """
     Place memo into database
        arg: all strings

        changes time to arrow time, and makes adjustments for post midnight submissions to correctly sort.

     """
     print("putmemo received hour:" + hour+" minute:"+minute)
     name_encrypted = encrypt_stuff(name)
     uoid_encrypted = encrypt_stuff(uoid)
     comments_encrypted = encrypt_stuff(comments)
     phone_encrypted = encrypt_stuff(phone)
     #dropoff = encrypt_stuff(dropoff)
     #pickup = encrypt_stuff(pickup)


     new_id = str(random.random())
     dateSet = arrow.utcnow().to('US/Pacific')
     h = int(dateSet.hour)
     
     afterMidnight = False #is it currently between midnight Pacific and 3am?
     if (dateSet.replace(hour = h).hour <= 3):
        afterMidnight = True
     if (afterMidnight): #after midnight, set arrow to current day
        if (hour=="12"):
            ttime = dateSet.replace(hour = 0, minute = int(minute))   
        elif (int(hour)<3):
            ttime = dateSet.replace(hour = int(hour), minute = int(minute))
        else:  # with below assumption, values should only be <3 here, this should be removed with proper input validation, so we can assume the below comment,
            temp = int(hour)+12
            day = int(dateSet.day)-1
            ttime = dateSet.replace(hour = temp, minute = int(minute),day=day)   # this assumes input validation on date so as to not schedule an appointment earlier than current time
     else:                #before midnight, set arrow schedule as needed if appt after midnight
        
        if (hour=="12"):
            day = int(dateSet.day)+1
            ttime = dateSet.replace(hour = 0, minute = int(minute), day = day)   
        elif (int(hour)<3):
            day = int(dateSet.day)+1
            ttime = dateSet.replace(hour = int(hour), minute = int(minute), day = day)   
        else:
            temp = int(hour)+12
            ttime = dateSet.replace(hour = temp, minute = int(minute))
     record = { "type": "dated_memo", 
                "date": dateSet.to('utc').naive,
                "time": time,
                "ttime": ttime.to('utc').naive, #this is the scheduled time, converted to arrow date object to solve sortation problem
                "name": name_encrypted,
                "uoid": uoid_encrypted,
                "phone": phone_encrypted,
                "dropoff": dropoff,
                "dlatlong": dropoff_coords,
                "pickup": pickup,
                "platlong": pickup_coords,
                "riders": riders,
            "bike": bike,
                "comments": comments_encrypted,
                "my_id": new_id,
                "history": history,
                "distance": "????",
                "estimate": "????",
                "van": "",
                "oncampus": on_campus,
                "pickedup": "",
                "droppedoff": "",
                "hour": str(hour),
                "minute": str(minute),
                "total_trip_estimate": "", #need to set these in manual operation!!!!!!!!!!!!
                "next_time_hour": "",
                "next_time_minute": "",
             }
     collection.insert(record)
     estimate_distance(new_id,pickup_coords,dropoff_coords)
     if (testing==False):#this refers to our testw function being the caller of this function
       newEntry = {}
       newEntry['time']=time;
       newEntry['id']=new_id;
       newEntry['tname']=name;
       newEntry['pickup']=pickup;
       newEntry['dropoff']=dropoff;
       newEntry['phone']=phonenumber(phone);
       newEntry['riders']=riders;
       newEntry['bike']=bike;
       newEntry['comments']=comments;
       newEntry['uoid']=formatUOID(uoid);
       newEntry['dlatlong']=dropoff_coords;
       newEntry['platlong']=pickup_coords;
       newEntry['hour']=str(hour);
       newEntry['minute']=str(minute);
       new_entry_list.append(newEntry)  #if during operating hours
         #if during operating hours         
     return 


#
# Returns string value of set { fall, winter, spring,summer} depending on current date.
#
#
# This could be improved by using exact days from academic calendar for next 5 years, this is an inclusive rule encompassing 2016-2019 dates
# and putting the data in a database or a form INSTEAD of having values here AT ALL
# here is current data: https://registrar.uoregon.edu/calendars/academic/five-year
#
# currently not in use, but necessary component for schedule building
#
def current_term():
    now = arrow.utcnow().to('US/Pacific')
    summer_start = now.replace(day = 21, month = 6)  
    summer_end = now.replace(day = 15, month = 9)  
    spring_start = now.replace(day = 1, month = 4)  
    spring_end = now.replace(day = 20, month = 6)  
    fall_start = now.replace(day = 22, month = 9)  
    fall_end = now.replace(day = 13, month = 12)  
    winter_start = now.replace(day = 7, month = 1)  
    winter_end = now.replace(day = 24, month = 3)  
    if(now>summer_start and now <summer_end):
        return "summer"
    elif(now>spring_start and now <spring_end):
        return "spring"
    elif(now>fall_start and now <fall_end):
        return "fall"
    elif(now>winter_start and now <winter_end):
        return "winter"        
    else:
        return "vacation"

#
# currently not in use, but necessary component for schedule building
#
def today_start_hour():
    term = current_term();
    now = arrow.utcnow().to('US/Pacific')
    if (term=="spring"):
        return 19
    elif (term=="summer"):
        return 21
    elif (term=="fall" or term=="winter"):
        return 18
    else:
        return -1 #vacation day
            
#
# currently not in use, but necessary component for schedule building
# need to fix past midnight rollover
#
def today_end_hour():
    now = arrow.utcnow().to('US/Pacific')
    if(now.format('ddd')=="Fri" or now.format('ddd')=="Sat"):
        return 2; #2am
    else:
        return 0; #12am


#
# this function logs any information into the given file
#
def log( message ):
    f = open ("log.txt", 'a')
    f.write(message)
    f.close()
    return
#
# this functions encrypts the given data with the app's key
#
def encrypt_stuff( to_encrypt ):
    encrypted_stuff = pad_string( to_encrypt )#string must be multiple of 16
    encryption_suite = AES.new(CONFIG.EKEY, AES.MODE_CBC, CONFIG.IV)
    output = encryption_suite.encrypt( encrypted_stuff )
    return output





#this will make a string a multiple of 16 by adding *'s'
def pad_string( input ):
    while (not(len(input)%16==0)):
        input+="*"
    return input;

#this will remove *'s from a string'
def unpad_string( input ):
    inString = input.decode('utf8')
    output = inString.replace("*","")
    return output;


#
# autoscheduling section:
#
    
def insert_van_into_queue(item,priority):
    van_number_list.append(item)
    free_time_list.append(priority)

def queue_min_time():
    return(min(free_time_list))

# this assumes you know the time has a matching entry in queue
def remove_min_from_queue():
    min_time = min(free_time_list)
    min_time_index = free_time_list.index(min_time)
    associated_van = van_number_list[min_time_index]
    van_number_list.remove(associated_van)
    free_time_list.remove(min_time)
    return(associated_van)


# this will count and return an id list of pickups for a certain time
def count_number_pickups(hour,minute):
    if hour>12:
        hour = hour-12;
    count = 0;
    pickups = []
    for record in collection.find( { "type": "dated_memo" } ):
        if (int(record['hour'])==hour and (int(record['minute'])==minute)):
            count = count+1
            pickups.append(record['my_id'])        
    return pickups




if __name__ == "__main__":
    
    #context = ('cert.crt', 'key.key')
    # App is created above so that it will
    # exist whether this is 'main' or not
    # (e.g., if we are running in a CGI script)
    ##app.debug=CONFIG.DEBUG
    ##app.logger.setLevel(logging.DEBUG)
    # We run on localhost only if debugging,
    # otherwise accessible to world
    if CONFIG.DEBUG:
        # Reachable only from the same computer
        app.run(port=CONFIG.PORT)

    else:
        # Reachable from anywhere 
        app.run(port=CONFIG.PORT,host="0.0.0.0") #https://hadabase.herokuapp.com

    


