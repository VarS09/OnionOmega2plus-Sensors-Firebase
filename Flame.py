import time
import onionGpio

gpio0=onionGpio.OnionGpio(0)

status=gpio0.setInputDirection()

invalue=gpio0.getValue()
	
while(1):
	
	value=gpio0.getValue()
	
	print(value)
	
	try:
		if value!=invalue:
			print('Flame ON!!')
		else:
			print('Flame OFF??')
	
		time.sleep(1)
		
	except KeyboardInterrupt:
		exit()

gpio0._freeGpio
		
	
	