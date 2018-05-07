#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template, request
import logging

from model.SLR import SLR

# webapp
app = Flask(__name__)

# model global variable 
model = None

def load_model():
    global model

    model = SLR('./data')
    model.load()
    app.logger.info("* model loaded.")

def _predict(input):
    return model.predict(input)


@app.route('/api/predict', methods=['POST'])
def predict():
    app.logger.debug(request.json)
    
    tmp = {'appraisedValue': [int(request.json['appraisedValue'])], 'minValue': [int(request.json['minValue'])]}
    input = pd.DataFrame(data=tmp)
    
    output = _predict(input)
    #print(output)
    app.logger.debug(output)

    return jsonify(results={'predict':int(output), 'predictRate':0})


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':

    load_model()

    app.debug = True
    app.logger.info("* Loading starting server...")
    app.run(host='0.0.0.0', port=4444) 


