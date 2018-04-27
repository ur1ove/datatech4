#!/usr/bin/python
# -*- coding: utf-8 -*-

from sshtunnel import SSHTunnelForwarder
import mysql.connector as db
import tensorflow as tf
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam, SGD

ssh_host = '210.114.91.91'
ssh_port = 19430

ssh_username='eduuser'
ssh_password='' # 암호

remote_bind_address = 'localhost'
remote_mysql_port = 3306

local_bind_address='localhost'

db_user='datatech4'
db_password = '' # 암호
db_name = 'auctionDB'

def query(q):
    with SSHTunnelForwarder(
         (ssh_host, ssh_port),
         ssh_username=ssh_username, 
         ssh_password=ssh_password, 
         remote_bind_address=(remote_bind_address, remote_mysql_port)) as server:
        
        conn = db.connect(host=local_bind_address, port=server.local_bind_port, 
                          user=db_user, 
                          passwd=db_password, 
                          database=db_name)
        
        return pd.read_sql_query(q, conn)

def query2(q):
    with SSHTunnelForwarder(
         (ssh_host, ssh_port),
         ssh_username=ssh_username, 
         ssh_password=ssh_password, 
         remote_bind_address=(remote_bind_address, remote_mysql_port)) as server:
        
        conn = db.connect(host=local_bind_address, port=server.local_bind_port, 
                          user=db_user, 
                          passwd=db_password, 
                          database=db_name)
        
        return pd.read_sql_query(q, conn)        


def train():
        
    df = query("select auctionDate, sum(appraisedValue) as appraisedValue, sum(minValue) as minValue, sum(saleValue) as saleValue from ctauInfo_out2 where saleValue > 0 and LENGTH(auctionDate) > 0 group by auctionDate")

    df['auctionDate'] = pd.to_datetime(df['auctionDate'],format='%Y-%m-%d')
    df = df.set_index('auctionDate')

    split_date = pd.Timestamp('2016-01-01')
    train = df.loc[:split_date, ['appraisedValue']]
    test = df.loc[split_date:, ['appraisedValue']]

    print(train.head())

    

    sc = MinMaxScaler()
    train_sc = sc.fit_transform(train)
    test_sc = sc.transform(test)

    train_sc_df = pd.DataFrame(train_sc, columns=['Scaled'], index=train.index)
    test_sc_df = pd.DataFrame(test_sc, columns=['Scaled'], index=test.index)

    print(train_sc_df.head())

    window_size = 7

    for s in range(1, window_size+1):
        train_sc_df['shift_{}'.format(s)] = train_sc_df['Scaled'].shift(s)
        test_sc_df['shift_{}'.format(s)] = test_sc_df['Scaled'].shift(s)

    train_sc_df.head(window_size+1)

    X_train = train_sc_df.dropna().drop('Scaled', axis=1)
    y_train = train_sc_df.dropna()[['Scaled']]

    X_test = test_sc_df.dropna().drop('Scaled', axis=1)
    y_test = test_sc_df.dropna()[['Scaled']]

    print(X_train.head())
    print(y_train.head())


    X_train = X_train.values
    X_test= X_test.values

    y_train = y_train.values
    y_test = y_test.values

    X_train_t = X_train.reshape(X_train.shape[0], window_size, 1)
    X_test_t = X_test.reshape(X_test.shape[0], window_size, 1)

    print("최종 DATA")
    print(X_train_t.shape)
    print(X_train_t)
    print(y_train)




    K.clear_session()
    model = Sequential() # Sequeatial Model
    model.add(LSTM(20, input_shape=(window_size, 1))) # (timestep, feature)
    model.add(Dense(1)) # output = 1
    #model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.0001, beta_1=0.9, beta_2=0.001, epsilon=1e-08), metrics=['accuracy'])
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    model.summary()


    early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)
    model.fit(X_train_t, y_train, epochs=1000, batch_size=10, verbose=1, callbacks=[early_stop])

    score = model.evaluate(X_test_t, y_test, verbose=0)
    print(model.metrics_names)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])


    model_json = model.to_json()
    with open("model.json", "w") as json_file : 
        json_file.write(model_json)

    model.save_weights("model.h5")
    print("Saved model to disk")


if __name__ == '__main__':
    train()

