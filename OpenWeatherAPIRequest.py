############################ a script to make API requests and print the returned data #############################
###################################### Maryam Ahmed, University of Oxford, 2016 ####################################

# 'requests' is a module (or 'library') that lets us make API requests
import requests

APIkey = "007b9467e4bd58d2a90527fe2532398c" # an API key lets us make a request
cityname = "London" # this is the parameter we're passing to the APi

# Stick the API request URL together with the city name and our API key
requestURL = "http://api.openweathermap.org/data/2.5/weather?"+"q="+cityname+"&APPID="+APIkey

# Make the API request!
APIresponse = requests.get(requestURL)

# Let's take a look at the data we get back from the API
print APIresponse.content

# Let's convert it to a dictionary to make it easier to access bits of information
data = APIresponse.json()

# What TYPE of data are we getting back from our API?
print type(APIresponse.content)

# Let's print out our data again and figure out which dictionary element we want to access
print data






# Access the dictionary element we're interested in and convert to Kelvin
#temp = data['main']['temp']

# Print the result to a string
# print "The temperature in "+str(cityname)+" is "+ str(data['main']['temp']-273.15) + "C"
