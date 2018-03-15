import time
import onionGpio
from firebase import firebase

firebase=firebase.FirebaseApplication('https://sensortest-db5d6.firebaseio.com/')

gpio0=onionGpio.OnionGpio(0)

status=gpio0.setInputDirection()

invalue=gpio0.getValue()
	
while(1):
	
	value=gpio0.getValue()
	
	print(value)
	
	try:
		if value!=invalue:
			print('Flame ON!!')
			resultPut=firebase.put('sensortest-db5d6','checkfire','1')
		else:
			print('Flame OFF??')
			resultPut=firebase.put('sensortest-db5d6','checkfire','-1')
	
		time.sleep(5)
		
	except KeyboardInterrupt:
		exit()

gpio0._freeGpio
		
	
	