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
gpio0=onionGpio.OnionGpio(0) #Connected IR flame sensor to gpio 0
status=gpio0.setInputDirection()
initialvalue=gpio0.getValue()

#Initializing MQ9 sensor
gpio11=onionGpio.OnionGpio(11) #Connected MQ9 sensor to gpio 11
status=gpio0.setInputDirection()
initialvalue=gpio0.getValue()

#Loop to sense data indefinitely
while(1):

	try:
		#Fetching DHT sensor data in json format
        	info=subprocess.check_output("dht-sensor 19 DHT11 json",shell=True) #Connected DHT11 to gpio 19
		data=json.loads(info)
       		#Just to verify
        	print('Sensor data')
		print(info)
        	#Pushing DHT sensor data to firebase
		result1=firebase.put('/sensor data','temperature',data['temperature'])
		result2=firebase.put('/sensor data','humidity',data['humidity'])
		print(result1) #Just to verify
		print(result2) #Just to verify
		
        	#Fetching Flame sensor data and pushing it to firebase
        	value=gpio0.getValue()
        	if value!=initialvalue:
			print('Flame ON!!') #Just to verify
			result3=firebase.put('/sensor data','checkfire','1')
		else:
			print('Flame OFF??') #Just to verify
			result3=firebase.put('/sensor data','checkfire','-1')
		
		print(result3) #Just to verify
		
		#Fetching MQ9 sensor data and pushing it to firebase
        	value=gpio11.getValue()
        	if value!=initialvalue:
			print('1') #Just to verify
			result4=firebase.put('/sensor data','check_hazardous_gas','1')
		else:
			print('-1') #Just to verify
			result4=firebase.put('/sensor data','check_hazardous_gas','-1')
		
		print(result4) #Just to verify
		
		time.sleep(5)
		
	except KeyboardInterrupt:
		onionGpio.OnionGpio(19)._freeGpio
		exit(0)
		
