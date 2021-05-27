#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 13:34:54 2021

@author: umang
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)
pickle_in = open('classification.pkl','rb')
model = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'WELCOME ALL'


@app.route('/predict',methods = ['GET'])
def prediction_ip():
    """Let's Authenticate the Bank notes
    This is using  docstrings for specification.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true  
    responses:
        200:
            description: The output values
    """
    
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    return 'bank note classification is '+str(prediction)

@app.route('/predict_file',methods = ['POST'])
def prediction_file():
    """Lets authenticate the bank notes1
    This is using docstring for specification1.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        
    responses:
        200:
            description: The output values
    """
    
    df = pd.read_csv(request.files.get('file'))
    prediction = model.predict(df)
    return 'bank note classification is '+str(list(prediction))

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000)