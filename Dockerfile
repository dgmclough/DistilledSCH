# Set the base image
FROM python:2.7

# Update the sources list
RUN apt-get update

# Update the sources list
RUN apt-get -y upgrade

# Copy the application folder inside the container
ADD . /my_application 

# Set the default directory where CMD will execute
WORKDIR /my_application

# Get pip to download and install requirements:
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN python database.py

# Expose listener port
EXPOSE 5000

# Set the default command to execute    
# when creating a new container
CMD python my_application.py
