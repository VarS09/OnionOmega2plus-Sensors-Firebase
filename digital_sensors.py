from firebase import firebase
import subprocess
import onionGpio
import json
import time

#Authenticate and initialize firebase  
authentication=firebase.FirebaseAuthentication('<YOUR_DATABASE_SECRET>','<YOUR_GMAIL>',extra={'id':123})
firebase.authentication=authentication
firebase=firebase.FirebaseApplication('<YOUR_PROJECT_URL>',authentication)
user = authentication.get_user()

#Initializing Flame sensor
gpio0=onionGpio.OnionGpio(0)
status=gpio0.setInputDirection()
initialvalue=gpio0.getValue()

#Initializing Hazardous gas detector sensor
gpio1=onionGpio.OnionGpio(1)
status=gpio1.setInputDirection()
initialvalue1=gpio1.getValue()

#Loop to sense data indefinitely
while(1):

	try:
		#Fetching DHT sensor data in json format
        info=subprocess.check_output("dht-sensor 19 DHT11 json",shell=True)
		data=json.loads(info)
        #Just to verify
        print('Sensor data')
		print(info)
        #Pushing DHT sensor data to firebase
		result1=firebase.put('/sensor data','temperature',data['temperature'])
		result2=firebase.put('/sensor data','humidity',data['humidity'])
		
        #Fetching Flame sensor data and pushing it to firebase
        value=gpio0.getValue()
        if value!=initialvalue:
			print('Flame ON!!') #Just to verify
			result3=firebase.put('/sensor data','checkfire','1')
		else:
			print('Flame OFF??') #Just to verify
			result3=firebase.put('/sensor data','checkfire','-1')
		
        #Fetching Hazardous gas detector sensor data and pushing it to firebase
        value1=gpio1.getValue()
        if value1!=initialvalue1:
			print('Hazardous gas detected!!') #Just to verify
			result4=firebase.put('/sensor data','checkair','1')
		else:
			print('Air Quality OK!!') #Just to verify
			result4=firebase.put('/sensor data','checkair','-1')
		
		time.sleep(5)
		
	except KeyboardInterrupt:
		onionGpio.OnionGpio(19)._freeGpio
		exit(0)
		