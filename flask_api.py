# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)

pickle_in = open('classification.pkl','rb')
model = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'WELCOME ALL'


@app.route('/predict')
def prediction_ip():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    return 'bank note classification is '+str(prediction)

@app.route('/predict_file',methods = ['POST'])
def prediction_file():
    df = pd.read_csv(request.files.get('file'))
    prediction = model.predict(df)
    return 'bank note classification is '+str(list(prediction))

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000)
    
