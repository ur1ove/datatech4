# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
import os

class SLR:
    model_filename = 'SLR.model'

    def __init__(self, path):
        self.model = LinearRegression(fit_intercept=False)
        
        if not os.path.exists(path):
            os.makedirs(path)

        self.fullpath = '{}/{}'.format(path,self.model_filename)

    def save(self):
        joblib.dump(self.model, self.fullpath)

    def load(self):
        self.model = joblib.load(self.fullpath)

    def train(self, x_train, y_train):
        return self.model.fit(x_train, y_train)
    

    def predict(self, x):
        return self.model.predict(x)
