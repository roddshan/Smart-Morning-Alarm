import conf, json, time
from boltiot import Bolt

limit=105     #This is distance b/w sensor and wall
max_time=20   
min_time=18

mybolt=Bolt(conf.bolt_api_key, conf.device_id)
response=mybolt.serialRead('10')
print(response)

def buzzer_action(pin, value):
  response=mybolt.digitalWrite(pin, value)
  
ticks=time.time() #gets the current time
ltime=time.localtime(ticks) #gets the local time
current_hour=ltime.tm_hour  #gets the current hour

while True:
  response=mybolt.serialRead('10')
  data=json.loads(response)
  distance= data['value'].rstrip()
  print("Distance:", distance)  #distance recieved from Arduino
  
  if(current_hour<max_time and current_hour>=min_time):
    print("Current Hour:", current_hour)
    if int(distance) < limit:   #If the person is sleeping then the distance will decrease
      print("Limit Exceeded || Buzzer Action")
      buzzer_action(1, "HIGH")    #buzzer beeps
      time.sleep(5)
      buzzer_action(1, "LOW")     #buzzer stops
      continue
    else:
      time.sleep(10)      #waits for 10 seconds
      continue
  time.sleep(10)    #waits for 10 second and again repeats all steps
