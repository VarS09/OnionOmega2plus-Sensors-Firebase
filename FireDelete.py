from firebase import firebase

firebase=firebase.FirebaseApplication('https://test-872f-01.firebaseio.com/')

result=firebase.delete('random/two',None)

print(result)