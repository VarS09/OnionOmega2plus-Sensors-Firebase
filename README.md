# Pushing sensor data to Firebase Realtime Database from Onion Omega 2+
Onion Omega 2+ is a single board computer that  runs OnionOS that is based on OpenWRT which is a Linux kernel based lightweight operating system for embedded system. In this project we collect the data from digital sensors such as DHT11/22, IR flame detection sensor, MQ9 gas sensor interfaced to the onion omega 2+ and push it to Firebase : Realtime Database. The environmental parameters pertaining the sensors are periodically updated in the database by user defined time intervals. 
## Hardware Requirements
* Onion omega 2+
* Expansion dock (which is optional, as the process can be setup and carried out without it and the dock is only meant for flexibility and convenience) 
* Connecting wires
* Power Source (for standalone operation, else connect to laptop/pc)
## Software Requirements
* OnionOS (which is up-to-date)
* Python
* [Firebase's REST API by Ozgur](https://github.com/ozgur/python-firebase)
## Getting Started
Firstly we need to install the Firebase's REST API, a python package which provides an interface between the Omega and Firebase. The installation is done using pip. For additional information on using python and pip on Omega can be found in [omega's documentation](https://docs.onion.io/omega2-docs/installing-and-using-python.html).
The commands used for installing the API and its dependencies are as follows:

`pip install requests`

![pip install requests](http://community.onion.io/assets/uploads/files/1525774842761-picture1-resized.png)

`pip install python-firebase`

![pip install python-firebase](http://community.onion.io/assets/uploads/files/1525774930559-picture2-resized.png)

## Interfacing sensors and the python script
DHT11/22 requires additional package to be installed on the omega for interfacing and data collection. The package provides a command `dht-sensor` that can be run on the terminal with additional parameters specified to obtain the data from the sensor. The installation process and information about the command arguments are documented by the [onion community](https://onion.io/2bt-reading-dht-sensor-data/). The remaining digital sensors donot require any additional packages to be installed.

This repository holds a generalized code that can be tweaked accordingly to the number of sensors being used. Additional sensors can also be augmented and they can be made functional by adding a few lines of code to the provided python script. The script consists some functions that authenticate the Firebase user to the Firebase database through the Omega.

![authenctication](http://community.onion.io/assets/uploads/files/1525777109144-picture3-resized.png)

A guide to find out your database secret is [mentioned here](https://stackoverflow.com/questions/37418372/firebase-where-is-my-account-secret-in-the-new-console?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa). Fill in your gmail account which you used for logging into Firebase in the next field. Fill in the project URL given in your Firebase database console.

When you run the script and the authentication to the Firebase database is completed successfully, the result should look something similar to the following in your Omega's terminal.

![output](http://community.onion.io/assets/uploads/files/1525777588706-picture4.png)

The values are updated accordingly in your Firebase database almost concurrently in the respective nodes on your Firebase database console representing each environmental parameter pertaining to the interfaced sensors.

![Firebase Console](https://user-images.githubusercontent.com/34755328/65387198-6276d800-dd62-11e9-832a-15cb33877d9d.PNG)

The values will be updated periodically in the respective nodes by the Omega with the data from the interfaced sensors.
