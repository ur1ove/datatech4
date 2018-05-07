# -*- coding: utf-8 -*-

from sshtunnel import SSHTunnelForwarder
import mysql.connector as db
import pandas as pd
import numpy as np

def query(q, config):

    if config['tunnel']:
        with SSHTunnelForwarder(
            (config['ssh']['host'], config['ssh']['port']),
            ssh_username=config['ssh']['username'], 
            ssh_password=config['ssh']['password'], 
            remote_bind_address=(config['db']['host'], config['db']['port'])) as server:
            
            conn = db.connect(host=config['db']['host'], port=server.local_bind_port, 
                          user=config['db']['user'], 
                          passwd=config['db']['password'], 
                          database=config['db']['database'])
            return pd.read_sql_query(q, conn)
    else:
        conn = db.connect(host=config['db']['host'], port=config['db']['port'], 
                          user=config['db']['user'], 
                          passwd=config['db']['password'], 
                          database=config['db']['database'])
        return pd.read_sql_query(q, conn)
