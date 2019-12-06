# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:27:17 2019

@author: Chintan Maniyar
"""

import json
from sentinelsat import SentinelAPI


def initializeSentinelAPI():
    '''
    Sets up the Sentinel API
    '''
    creds = {}
    with open('./credentials.json') as temp:
        creds = json.load(temp)
    
    user = creds['uid']
    passw = creds['pass']
    api = SentinelAPI(user, passw, 'https://scihub.copernicus.eu/dhus')
    
    return api


    
    