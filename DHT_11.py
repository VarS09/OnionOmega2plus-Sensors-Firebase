import time
import onionGpio

def bin2dec(string_num):
    return str(int(string_num,2))

data=[]

gpio4=onionGpio.OnionGpio(4)
status=gpio4.setOutputDirection()
stat=gpio4.setValue(1)
time.sleep(0.025)
stat=gpio4.setValue(0)
time.sleep(0.02)
status=gpio4.setInputDirection()

for i in range(0,500):
    data.append(gpio4.getValue())

bit_count=0
tmp=0
count=0
HumidityBit=""
TemperatureBit=""
crc=""
try:
    while data[count]==1:
        tmp=1
        count=count+1
    
    for i in range(0,32):
        bit_count=0

        while data[count]==0:
            tmp=1
            count=count+1

        while data[count]==1:
            bit_count=bit_count+1
            count=count+1

        if bit_count > 3:
            if i>=0 and i<8:
                HumidityBit=HumidityBit+"1"

            if i>=16 and i<24:
                TemperatureBit=TemperatureBit+"1"

        else:
            if i>=0 and i<8:
                HumidityBit=HumidityBit+"0"

            if i>=16 and i<24:
                TemperatureBit=TemperatureBit+"0"

except:
    print("ERR_RANGE")
    exit(0)

try:
    for i in range(0,8):
        bit_count=0
        
        while data[count]==0:
            tmp=1
            count=count+1

        while data[count]==1:
            bit_count=bit_count+1
            count=count+1

        if bit_count > 3:
            crc=crc+"1"
        else:
            crc=crc+"0"
except:
    print("ERR_RANGE")
    exit(0)

Humidity=bin2dec(HumidityBit)
Temperature=bin2dec(TemperatureBit)

if int(Humidity)+int(Temperature)-int(bin2dec(crc))==0:
    print("Humidity:" + Humidity + "%")
    print("Temperature:" + Temperature + "C")
else:
    print("ERR_CRC")