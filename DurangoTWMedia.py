#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:21:51 2018

@author: jesus
"""

import tweepy,os


consumer_key = 'KEY'
consumer_secret = 'KEY'
access_token = 'KEY'
access_token_secret = 'KEY'
PATH=os.path.dirname(os.path.abspath(__file__))

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


api.update_with_media(PATH+"/figura.png","Grafica")
