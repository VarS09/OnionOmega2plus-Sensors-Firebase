from firebase import firebase

firebase=firebase.FirebaseApplication('https://pushpulltest.firebaseio.com/')

resultPut=firebase.put('pushpulltest','five','0')

print(resultPut)