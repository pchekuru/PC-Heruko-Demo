# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:09:02 2020

@author: pchekuru
"""

#create a web app using flask or django

import numpy as np
from flask import Flask, request, jsonify, render_template ## anaconda will have flask app
import pickle

app = Flask(__name__) ## Create Flask app
model = pickle.load(open('model.pkl', 'rb')) ## read file

## This below will render the template
@app.route('/')  ##Home page, root page(/) will render the index.html file
def home():
    return render_template('index.html')

## Post method, provide features to model.pkl file and it will retung the predictions in below function
    ##Web api
@app.route('/predict',methods=['POST']) #/predict will hit the below predict function
def predict():
    '''
    for rendering results on HTML GUI:
    '''
    int_features = [int(x) for x in request.form.values()] ## request libarary take values from text fields in form 
    final_features = [np.array(int_features)] ## converting it to array
    prediction = model.predict(final_features) ## passign finall predction variable to predict
    
    output = round(prediction[0],2) ## finally i will print the output
    
    return render_template('index.html',prediction_text='Employee Salary should be $ {}'.format(output))
## again rendering the index.html template with prediction text match to file and print output

 ## main function which will run the whole flask

if __name__ == "__main__":
    app.run(debug=True)    