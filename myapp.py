############################ a web app written with the Flask web framework for Python #############################
###################################### Maryam Ahmed, University of Oxford, 2016 ####################################

# Your challenge, should you choose to accept it, is:
# 1. Edit template.html to add a form element, and embedded CSS styling including a link to normalize.css
# 2. Pull the user's form input from the HTML template back into the Flask app
# 3. Make an API request based on the user's form input
# 4. Clean up the received information from the API and display it back via the HTML template

# Import the web framework Flask, and the requests module
from flask import Flask, render_template, request
import requests

# Initialise an instance of the 'Flask' class and call it 'app'
app = Flask(__name__)

# Let's define what happens on the landing page of our app
@app.route("/")
def index(): # This is the function that executes when the landing page loads
    return "Hello world! This is my app's landing page!"
    # Isn't this a bit boring? Wouldn't it be great if we could format and style our app with HTML/CSS?
    #return render_template('template.html')

# Let's define what happens when the user submits the form via the HTML template
#@app.route("/", methods=['POST'])
#def API_request():
    #APIparam1 = request.form['APIparam1']
    #APIkey = []
    # Make the API request using the API key and parameters above, just like we did in APIrequest.py
    # API_message = [] # Clean up and format the API data and create a string to pass back to the HTML template
    #return render_template('OpenWeatherMapTemplate.html', **locals()) # re-render the HTML template

# Execute this code when this file is called as a script
if __name__ == "__main__":
    app.run()

