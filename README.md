# DistilledSCH

A python application using a flask web-framework with an SQLite database.
The "database.py" script creates the database, a database table and populates
the database table with the data found in the csv file, "cars.csv". The "cars.csv"
contains the records provided in the assignment description. 
The "my_application.py" script contains the flask web-framework structure to
create the different views using the @route modifier. It runs the application
and binds it to the localhost on port 5000. 

To run the application locally, download both of the python scripts ('database.py' and 'my_application.py') and csv file 
containing the data into an application folder. Download myscript.sh and make sure it is executable. Ensure that Python 2.7 or above is installed locally. 
1) From the command line cd into the application folder where the downloaded scripts are
2) In terminal run the command "python database.py" to create database and populate it (it gets saved in application folder)
3) In terminal run the command "python my_application.py" to run the application and bind it to port 5000 on localhost
4) Open browser or terminal to interact with application (eg. for command line interaction: curl http://localhost:5000/car/2)
5) Execute the 'myscript.sh' bash script in the terminal to run the commands provided in te doumentation

####The Docker setup was not fully tested. The above implementation is fully functioning however####
The Dockerfile contains the script for creating the docker image. This requires 
docker to be installed on the local machine. 
1) The command to build the docker image from the command line is: "docker build -t <image_name>" 
2) The command to run the docker application is "docker run -p 4000:5000 <image_name>"
The requirements.txt file includes the names of modules required for the application to run. 



