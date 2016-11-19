############################ a script to make API requests and print the returned data #############################

# 'requests' is a module (or 'library') that lets us make API requests
import requests

APIkey = [] # Stick your API key in here as a string

APIparam1 = [] # Put any parameters you need to specify for the API request in here
APIparam2 = [] # Delete this 2nd parameter if you don't need it
APIparam3 = [] # Delete this 3rd parameter if you don't need it

# Find out from your chosen API's documentation what the API request URL is, and stick your API parameters
requestURL = []

# Make your API request!
APIresponse = requests.get(requestURL)

# Convert the response into a dictionary, so you can easily access the information you want
data = APIresponse.json()

# Pick out the information you want from the returned API data (remember the data type is a dictionary) and print a
# string to the command line with this data embedded in it (e.g. it is 12 degrees celsius in London today)

print "Build your own string!"
