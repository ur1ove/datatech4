#!/usr/bin/python
# -*- coding: utf-8 -*-

from model.SLR import SLR
import setting
import utils

def train():
    data = utils.query("select auctionDate, appraisedValue, minValue, saleValue from ctauInfo_out2 where saleValue > 0 and LENGTH(auctionDate) > 0", setting.CONF)
    
    col_names = ['appraisedValue', 'minValue']
    X = data[col_names].astype(float)
    y = data['saleValue'].astype(float)
    
    print(X.head())
    print(y.head())
    
    model = SLR('./data')
    model.train(X, y)
    print("training model...")

    model.save()
    print("Saved model to disk")

if __name__ == '__main__':
    train()

