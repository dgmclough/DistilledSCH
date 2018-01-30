#!/bin/bash

echo 'Testing My Application'
echo '----------------------'
echo '1) Test for GET request for all cars in Database'
curl 'http://localhost:5000/car/'
echo 'Test 1 Complete'
echo '2) Test for GET request for specific car by ID'
curl 'http://localhost:5000/car/2'
echo 'Test 2 Complete'
echo '2.2) Test for Error Handling- non-existant ID'
curl 'http://localhost:5000/car/34'
echo 'Test 2.2 Complete'
echo '----------------------'
echo '3) Test for POST request to Database'
curl -d '{"make":"Seat","model":"Cordoba", "year":"2003","chassis_id":"12345F"}' -H "Content-Type: application/json" -X POST 'http://localhost:5000/car/'
echo 'Test 3 Complete'
echo '----------------------'
echo '4) Test for POST request to Database'
curl -d '{"make":"Seat","model":"Cordoba", "year":"2003"}' -H "Content-Type: application/json" -X POST 'http://localhost:5000/avgprice'
echo 'Test 4 Complete'
echo '----------------------'


