from firebase import firebase

firebase=firebase.FirebaseApplication('https://test-872f-01.firebaseio.com/')

result=firebase.get('/user','one')

print(result)