					________________________________________
					How to Run the MySpaceID-Python SDK
					________________________________________
1. Enter the consumer key and consumer secret in ckeynsecret.py file. (Each sample app has separate ckeynsecret.py file). 



2. Enter the appropriate call back on developer.myspace.com, e.g: if your application is running at local server at port 8083 specify
		http://localhost:8083


					________________________________________
					Python Settings/Setup:
					________________________________________

1) Download Eclipse or any other IDE. 

2) If you are using Eclipse download Python add on for eclipse and make interpreter settings in Eclipse. 

3) Create a new project and copy every thing in that folder. 


					________________________________________
					How to run Sample Apps and Test Cases
					________________________________________
1) copy every thing in source folder to both sample app folders.
2) Specify consumer key/secret
3) Configure an app in your server and run it (make sure you are using same port which you have specified in call back url on developer.myspace.com 

4) To run the test cases specify token,secret, authtoken,secret and app id in constructor of test_myspace_api 
5) click on run_test and hit run to execute all test cases. 

