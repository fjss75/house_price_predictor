The repository contains the next files in the folder housing_prices:
1. housing.csv.zip: file downloaded from kaggle link provided for the task.
2. housing.csv: extracted data from the downloaded file.
3. housing.ipynb: Python Notebook with instructions for analyzing the data and creating a model.
4. model.joblib: the model created with the notebook
5. app.py: a program that can use the model with FastAPI requests
6. requirements.txt: a file with the libraries used
7. Dockerfile: a configuration file to create the image of the application

Instructions to test the application.
We will use two terminals: one for the service and the other for the request.
1. For the service: As the image has already been pushed to my dockerhub public repository,
   it should be enough to run this command line in a machine with docker already installed:
   docker run -p 8000:8000 --name predictor fjsoto/house_price_predictor:1.0
   At the end of the execution lines it should say "Application startup complete"
   Leave this terminal open to use it with the second terminal.
   
2. For the request: In the seond terminal we will send a curl request specifying the json format of the data and the data itself
   as in the example below:
   curl -X 'POST' 'http://localhost:8000/prediction' -H 'accept: applicaiontion/json' -H 'Content-Type: application/json' -d '[-118.27, 34.00, 46.0, 600.0, 171.0, 377.0, 181.0, 2.4107, 1.0, 0.0, 0.0, 0.0, 0.0]'
   The prediction should appear as response to the request in json format: {"price":187063.94}
   There aslo should be a new line in the first terminal with a status of the request like the one below:
   172.17.0.1:35300 - "POST /prediction HTTP/1.1" 200 OK

   I decided to use jupyter notebook for the data sicence task because of interactivity when analyzing the data.
   Using a separate python application gives the possibility to update the model when needed, without modifying the application at its core.
   Using docker gives the posibility to encapsulate evertything someone neeeds to run the application and it can be deployed in arquitecures supporting it.

   With more time given, I would have tested other methods for dealing with null values, I would have tested more feature transformations and more models,
   I would have added also support for different possible handling of errors like diffent data types in the request.
