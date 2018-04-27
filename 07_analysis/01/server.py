#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from flask import Flask, jsonify, render_template, request
import logging

from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam, SGD
from keras.models import model_from_json

# webapp
app = Flask(__name__)

# model global variable 
model = None

def load_model():
    global model

    json_file = open("model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    
    model = model_from_json(loaded_model_json)
    model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.0001, beta_1=0.9, beta_2=0.001, epsilon=1e-08), metrics=['accuracy'])


def _predict(input):
    return model.predict()


@app.route('/api/predict', methods=['POST'])
def predict():
    app.logger.debug(request.json)
    
    # input = (np.array(request.json, dtype=np.uint8)).reshape(1, 7, 1)
    #output1 = _predict(input)
    
    return jsonify(results={'predict':23000, 'predictRate':93.2})


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':

    load_model()

    app.debug = True
    app.logger.info("* Loading Keras model and Flask starting server...")
    app.run(host='0.0.0.0', port=4444) 


