from flask import Flask,jsonify
from config import DevelopmentConfig
from db import db
from backend.models import Telegram, TradeDataDefaults
from backend.models import Bybit as BybitModel

from flask_restx import Api,fields
from backend.controller.userAuth import api as userNS
from backend.controller.userAuth import api2 as authNS
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

CORS(app)


# manage file here

#!/usr/bin/env python
# -*- coding: utf-8 -*-ci
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

from enum import Enum
from operator import pos     # for enum34, or the stdlib version

import ccxt
from sqlalchemy.sql.sqltypes import DECIMAL
from sqlalchemy.sql import exists    
from backend.extensions import MarketData
from backend.extensions import WebsocketMarket
from backend.extensions import Client as FuturesClient
import random
import csv
import string
from csv import writer
from csv import reader
# from decimal import *
import math
import logging
from datetime import datetime
from time import sleep
import time
import json
import ast
# import bybit

import argparse
import os
import sys
import click
import time
import logging 


from flask import Flask, request, abort, session
from flask_session import Session
from loguru import logger
import threading, time
from telethon import TelegramClient, events, sync
import time
import json
from io import StringIO
import socket
import datetime
#import pyperclip
import os, ast
import subprocess
import re
import signal
import clipboard
#from jaraco import clipboard as clipboard2
# First we need the asyncio library
import asyncio
#from backend.extensions import db

from flask.cli import FlaskGroup, run_command
from flask_cors import CORS
# from backend.models import Bybit as BybitModel
# from backend.models import Telegram

from backend.extensions import Bybit 
# from backend.database import BaseModel
from multiprocessing import Process

from flask_alembic import Alembic
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from telethon import TelegramClient, events, sync
import time


alembic = Alembic()

# from backend.api import ModelResource
# from backend.extensions.api import api       # url_prefix='/api/v1'
# from backend.security.models import Asset
# from backend.extensions import db
from flask import Blueprint, url_for
# from backend.api import CREATE, DELETE, GET, LIST, PATCH, PUT
from flask import jsonify, Flask
from flask_wtf.csrf import CSRFProtect
import requests
security = Blueprint('security', __name__, url_prefix='/auth',
                     template_folder='templates')

# csrf = CSRFProtect()
# csrf.init_app(app)

api = Api(app, version = "1.0", 
		  title = "Crypttops BybitBot Api", 
		  description = "Admin panel",
          doc=False)

# adding the namespaces
api.add_namespace(userNS, path='/users')
api.add_namespace(authNS)

# Then we need a loop to work with
loop = asyncio.get_event_loop()
bot_token = "add toke here"

#curl http://127.0.0.1:5000/asset{"hello": "world"}
#curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:5000/asset
    #maybe this method have defined below will be useful
    #it will eliminate the aspect of receiving bot updates when you havent even started the bot
    #it is useful so that a user only received automated updates only when they have started 
    #the bot
import random
import csv
import string
from csv import writer
from csv import reader


"""
Import the send_order_v2 from trade-telegram-bot.py
"""
from tradetelegrambot import send_order_v2



global result_str
result_str = ''

def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(16))
    print('value to write to file')
    print(result_str)
    result_str1 = [result_str, ]
    print('----------------------------')
    with open('tokens.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(result_str1)
    return result_str

def save_order_ids(order_Id):

    with open('orderId.csv', 'a+', newline='') as write_obj:

        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(order_Id)
    return order_Id

import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



global telegram_id
global first_name
global second_name

telegram_id = ''
first_name = ''
second_name  = ''


# http://a0902b3e4a41.ngrok.io/webhook/zulhfezpankgalke 

def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(16))
    print('value to write to file')
    print(result_str)
    result_str1 = [result_str, ]
    print('----------------------------')
    with open('tokens.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(result_str1)
    return result_str

def checkPositionExistsAutomated(user_trade_data):
    print("the user trade data", user_trade_data)
    has_position = False
    textp =''
    print("Trade symbol...................", user_trade_data['symbol'])
    trade_symbol = user_trade_data['symbol']
    vvery12 = telegram_id
    with app.app_context():
            api_data = db.session.query(Telegram.api_key, Telegram.api_secret,Telegram.verified, Telegram.first_name,Telegram.second_name).filter(Telegram.telegramid==user_trade_data['TelegramID']).all()
        
    api_key = api_data[0][0]
    api_secret = api_data[0][1]
    
    try:
        bybit1 = Bybit(api_key=api_key,
                    secret=api_secret, symbol=trade_symbol, ws=True, test=False)


        position1 = bybit1.get_position_http()
        print('---------------------------New Position DATA----------------------------------')
        position_result1  = position1['result']
        json.dumps(position_result1, indent=2)
        # update1.message.reply_text('Your Bybit Positions')
        botu_message = 'Your Bybit Positions\n\n'
        print('auto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_result')
        print(position_result1)
        # if position_result1['data'] is None : 
           
        # else: 
        print(len(position_result1))
        for x in range(len(position_result1)):
           
            if position_result1[x]['data']['symbol'] == trade_symbol and        position_result1[x]['data']['side'] == user_trade_data['side']:
                
                textp = "You are already in a trade:\n side | {0}| size | {1} \n Wait until the position is closed before opening another trade of the same asset.".format(position_result1[x]['data']['side'],position_result1[x]['data']['size'])
                print(textp)
                has_position = True
            if position_result1[x]['data']['symbol'] == trade_symbol and        position_result1[x]['data']['side'] == 'None':
                # update1.message.reply_text('You have no  open position')
                bot_message1 = 'You have no  open position'
                textp = bot_message1
                has_position = False


    except:
        textp = "There is something wrong, your current positions could not be fetched from Bybit." 

    return has_position, textp    
   

@app.route('/webhook/<user_auth_token>', methods=['POST'])
def webhook(user_auth_token):
    textp = ''
    print('Webhook REsource Started to manage Auto-TRading from TradingView')
    #generate api id and hash on https://my.telegram.org
    #name = 'Bybit_TradingView_Bot'
    list_of_rows = [[]]
    # read csv file as a list of lists
    with open('tokens.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        print('list_of_rows', list_of_rows)
    token = '111'
    print('token = ',  token)

    #generate api id and hash on https://my.telegram.org
    #name = 'Bybit_TradingView_Bot'
    list_of_rows_access = [[]]
    # read csv file as a list of lists
    with open('access.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows_access = list(csv_reader)
        print('list_of_rows_access', list_of_rows_access)
    print('token = ',  token)
    toList = []
    toListAccess = []
    if request.method == 'POST':
        datart = request.get_data(as_text=True)
        print(datart)
        # y_dict = ast.literal_eval(datart)

        
        for i in range(len(list_of_rows)):
            rt = str(list_of_rows[i])[1:]
            tr = rt[1:]
            re = tr[:-1]
            rew = re[:-1]
            toList.append(rew)
        for i in range(len(list_of_rows_access)):
            rt = str(list_of_rows_access[i])[1:]
            tr = rt[1:]
            re = tr[:-1]
            rew = re[:-1]
            toListAccess.append(rew)
            # print('toListAccess', toListAccess, 'passed token', y_dict['token'])
        with app.app_context():
            authenticated = bool(db.session.query(Telegram).filter_by(auth_token = user_auth_token).first())
            user = db.session.query(Telegram).filter_by(auth_token = user_auth_token).first()
            
        # if token in toList:
        if authenticated == True and user.verified=="Yes": 
            y_dict = json.loads(datart)
            y_dict.update({"TelegramID":int(user.telegramid)})
          
            print('token found')
            #datart = datarc[1:-1]
            print('===================================================')
            print(datart)
            print('===================================================')
                
            bot_token = 'add toke here'
            bot_chatID =str(user.telegramid)
            print("bot chat id", bot_chatID)
            #datart = '{"type": "market", "side": "buy", "amount": "97", "leftAsset" : "BTC", "rightAsset" : "USDT","leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "TelegramID":"1093054762"}'
            if datart != None :     

                
                print('Trade request received from TradingView.')
               
                has_positions, textresponse = checkPositionExistsAutomated(y_dict)

                print("\n\n\n\n\n******************++++++++++++++++++++++", has_positions, textresponse)
                if has_positions ==True:
                    textp = textresponse
                    bot_message = textp
                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message
                    
                    response = requests.get(send_text)

                    
                else:
                    ret_msg, error_reta, placed_btc_value, created_at, final_entry_price = send_order_v2(y_dict)
                    print('ret_msg', ret_msg)
                    print('error_reta', error_reta)
                    print('placed_btc_value', placed_btc_value)
                    print('final_entry_price', final_entry_price)
                    try:
                        placedbtcvalue = "%.6f"%float(placed_btc_value)
                    except:
                        placedbtcvalue = " "

                    vvery12 = user.telegramid
                    
                    if ret_msg == 'OK' or ret_msg == 'ok':
                        
                        print('dsdjsopijewipjdfksipdold', placedbtcvalue)
                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = '*Automated Order Received: * ' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                        bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                        bot_message5 = '' + str(placedbtcvalue) +' BTC' '@ $'+str(round(float(final_entry_price), 5))+''


                        textp = bot_message3 + bot_message4 + bot_message5

                    

                    if error_reta.startswith('TrailingStop:') or ret_msg.startswith('TrailingStop:'):
                        print(float(placed_btc_value))
                        
                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = '*' +y_dict['side'] + '*' + '*Automated Order Received: * ' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                        bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                        bot_message5 = '' + str(placedbtcvalue) +'' '@ $'+str(round(float(final_entry_price), 5))+''

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)
                        
                        textp = bot_message3 + bot_message4 + bot_message5

                    

                    if ret_msg == 'empty price':
                      
                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = 'Your buy Order Not successful' '\n '' '
                        bot_message4 = 'You have no funds in your Bybit Account ' ' \n ' 
                        bot_message5 = 'Top up to continue using the Bot'

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        textp = bot_message3 + bot_message4 + bot_message5
                        
                    if error_reta.startswith('error sign!'):
                        

                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = 'Your buy Order Not successful' '\n '' '
                        bot_message4 = 'You have no funds in your Bybit Account ' ' \n \n ' 
                        bot_message5 = 'Top up to continue using the Bot'

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        textp = bot_message3 + bot_message4 + bot_message5
                    
                        # Param validation for 
                    
                    if error_reta.startswith('Param validation') or ret_msg.startswith('Param validation'):
                        
                        

                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = 'Your buy Order Not successful' '\n '' '
                        bot_message4 = 'You have no funds in your Bybit Account ' ' \n \n ' 
                        bot_message5 = 'Top up to continue using the Bot'

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        botu_message = 'You have insuffient Balance to Place this Order. Check the percentage of Amount you are passing\n'
                        botu_message1 = 'Your quantity was not correct, you can reduce the percentage of amount. '
                        botu_message2 = 'Or you can top up to continue using the Bot'

                        textp = botu_message + botu_message1 + botu_message2
                    if error_reta.startswith('incorrect'):
                        textp = "something is wrong\n Check your default settings \n \n "

                    if error_reta.startswith('params stop_loss invalid') or ret_msg.startswith('params stop_loss invalid'):
                           
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Automated Order Received: ' + str(y_dict['side']) +'*' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(assetSymbolSplitter(y_dict["symbol"])) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: StopLoss is invalid"


                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                    if error_reta.startswith('params trailing_stop invalid') or ret_msg.startswith('params trailing_stop invalid'):
                        
                        
                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = '*Automated Order Received: ' + str(y_dict['side']) +'*' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                        bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                        bot_message5 = '' + str(placedbtcvalue) +' ' + str(assetSymbolSplitter(y_dict["symbol"])) + '@ $'+str(round(float(final_entry_price), 5))+''
                        bot_message6 = "\n Conditional parameters not activated: TrailingStop is invalid"

                        textp = bot_message3 + bot_message4 + bot_message5 + bot_message6
                    
                    if error_reta.startswith('params take_profit invalid') or ret_msg.startswith('params take_profit invalid'):
                        
                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = '*Automated Order Received: ' + str(y_dict['side']) +'*' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                        bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                        bot_message5 = '' + str(placedbtcvalue) +' ' + str(assetSymbolSplitter(y_dict["symbol"])) + '@ $'+str(round(float(final_entry_price), 5))+''
                        bot_message6 = "\n Conditional parameters not activated: TakeProfit is invalid"

                        textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                        



                        # y_dict.clear()
                    if error_reta.startswith('params new_trailing_active invalid') or ret_msg.startswith('params new_trailing_active invalid'):
                            
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Automated Order Received: ' + str(y_dict['side']) +'*' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(assetSymbolSplitter(y_dict["symbol"])) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: newTrailingStop is invalid"

                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 
                    if error_reta.startswith('params invalid') or ret_msg.startswith('params invalid'):
                            
                            
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Automated Order Received: ' + str(y_dict['side']) +'*' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(assetSymbolSplitter(y_dict["symbol"])) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: params invalid"

                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                    if error_reta.startswith('TakeProfit') or ret_msg.startswith('TakeProfit'):
                        textp = ret_msg

                    if error_reta.startswith('StopLoss') or ret_msg.startswith('StopLoss'):
                        textp = ret_msg

                    if error_reta.startswith('TrailingStop') or ret_msg.startswith('TrailingStop'):
                        textp = ret_msg

                    if error_reta.startswith('NewTrailingActive') or ret_msg.startswith('NewTrailingActive'):
                        textp = ret_msg
                        # y_dict.clear()
                    bot_message = textp
                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

            else: 
                bot_message = 'No valid message received from TradingView eligible of placing trade on your Bybit Account'
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)
                print('Automated Webhook Sent for processing')

                bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                bot_message1 = 'No valid message received from TradingView eligible of placing trade on your Bybit Account' 

                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)
                  

        else: 
            print('you not authenticated to use this bot')
            print('token not found')
            print('You have wrong settings for your url. Click Webhook button to get correct format')

            # bot_message = 'token not found. Ensure you have correct token to use the bot'
            bot_message = 'you are not authenticated to use this bot\n Visit https://www.bybit.com/en-US/invite?ref=J6WWOV to create a Bybit account and get API keys.\n' 
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)
            print('Automated Webhook Sent for processing')

            bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
            bot_message1 = 'You have wrong settings for your url. Click Webhook button to get correct format' 

            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)

            abort(400)
        print('_____________TESTING ASSET WITHOUT MODEL RESURCE______________________')
        return "WEBHOOK CALLED"

@app.route('/close/<user_auth_token>', methods=['GET','POST'])
def close(user_auth_token):
    print('Webhook REsource Started to manage Auto-TRading from TradingView')
    #generate api id and hash on https://my.telegram.org
    #name = 'Bybit_TradingView_Bot'
    list_of_rows = [[]]
    # read csv file as a list of lists
    with open('tokens.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

    #generate api id and hash on https://my.telegram.org
    #name = 'Bybit_TradingView_Bot'
    list_of_rows_access = [[]]
    # read csv file as a list of lists
    with open('access.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows_access = list(csv_reader)
        print('list_of_rows_access', list_of_rows_access)
    token = '11111'
    print('token = ',  token)
    toList = []
    toListAccess = []
    if request.method == 'POST':
        datart = request.get_data(as_text=True)
        
        for i in range(len(list_of_rows)):
            rt = str(list_of_rows[i])[1:]
            tr = rt[1:]
            re = tr[:-1]
            rew = re[:-1]
            toList.append(rew)
        for i in range(len(list_of_rows_access)):
            rt = str(list_of_rows_access[i])[1:]
            tr = rt[1:]
            re = tr[:-1]
            rew = re[:-1]
            toListAccess.append(rew)
            # print('toListAccess', toListAccess, 'passed token', y_dict['token'])
        # if token in toList and y_dict['token'] in toListAccess: 
        with app.app_context():
            authenticated = bool(db.session.query(Telegram).filter_by(auth_token = user_auth_token).first())
            user = bool(db.session.query(Telegram).filter_by(auth_token = user_auth_token).first())
            
            
        # if token in toList:
        if authenticated == True: 
            y_dict = json.loads(datart)
            y_dict.update({"TelegramID":int(user.telegramid)})
            print('token found')
            #datart = datarc[1:-1]
            print('===================================================')
            print(datart)
            print('===================================================')
                
            # y_dict = ast.literal_eval(datart)
            bot_token = 'add toke here'
            y_dict_raw = json.loads(datart)
            y_dict = y_dict_raw.update({"TelegramID":int(user.telegramid)})
            bot_chatID = str(user.telegramid)
            #datart = '{"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "TelegramID":"1093054762"}'
            if datart != None :                
                # my code running perfectly
                print('Trade request received from TradingView.')
                closes = close_webhook(y_dict)
                print("Printing closes------------", closes)
                if closes !='None' or None: 
                    bot_message = closes       
                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                    bot_message1 = closes

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)
                    
                else: 
                    bot_message = 'Positions already closed'
                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                    bot_message1 = 'Positions already closed'

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

            else: 
                bot_message = 'No valid message received from TradingView eligible of closing trade on your Bybit Account'
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)
                print('Automated Webhook Sent for processing')

                bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                bot_message1 = 'No valid message received from TradingView eligible of closing trade on your Bybit Account'

                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)

        else: 
            print('you not authenticated to use this bot')
            print('token not found')
            print('You have wrong settings for your url. Click Webhook button to get correct format')

            # bot_message = 'token not found. Ensure you have correct token to use the bot'
            bot_message = 'you are not authenticated to use this bot\n Visit https://www.bybit.com/en-US/invite?ref=J6WWOV to create a Bybit account and get API keys.\n' 
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)
            print('Automated Webhook Sent for processing')

            bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
            bot_message1 = 'token not found. Ensure you have correct token to use the bot'

            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)

            abort(400)
        print('_____________TESTING ASSET WITHOUT MODEL RESURCE______________________')
        return "WEBHOOK CALLED"
        

@app.route('/leverage<user_auth_token>', methods=['GET','POST'])
def leverage(user_auth_token):
    print('CLOSE Webhook REsource Started to manage Auto-TRading from TradingView')
    list_of_rows = [[]]
    # read csv file as a list of lists
    with open('tokens.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
    
    token = '1111'

    print('token = ',  token)

    #generate api id and hash on https://my.telegram.org
    #name = 'Bybit_TradingView_Bot'
    list_of_rows_access = [[]]
    # read csv file as a list of lists
    with open('access.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows_access = list(csv_reader)
        print('list_of_rows_access', list_of_rows_access)
        
    print('token = ',  token)
    toList = []
    toListAccess = []
    if request.method == 'POST':
        datart = request.get_data(as_text=True)
        # y_dict = ast.literal_eval(datart)
       
        for i in range(len(list_of_rows)):
            rt = str(list_of_rows[i])[1:]
            tr = rt[1:]
            re = tr[:-1]
            rew = re[:-1]
            toList.append(rew)
        for i in range(len(list_of_rows_access)):
            rt = str(list_of_rows_access[i])[1:]
            tr = rt[1:]
            re = tr[:-1]
            rew = re[:-1]
            toListAccess.append(rew)
            # print('toListAccess', toListAccess, 'passed token', y_dict['token'])
        # if token in toList and y_dict['token'] in toListAccess:  
        print('token found')
        #datart = datarc[1:-1]
        with app.app_context():
            authenticated = bool(db.session.query(Telegram).filter_by(auth_token = user_auth_token).first())
            user = bool(db.session.query(Telegram).filter_by(auth_token = user_auth_token).first())
        # if token in toList:
        if authenticated == True and user.verified=="Yes": 
            print('===================================================')
            print(datart)
            print('===================================================')
            y_dict = json.loads(datart)
            y_dict.update({"TelegramID":int(user.telegramid)})

            bot_token = 'add toke here'
            bot_chatID = str(user.telegramid)
            #datart = '{"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "TelegramID":"1093054762"}'
            if datart != None :                
                # my code running perfectly
                print('Trade request received from TradingView.')
                current_manual_leverage, adjusted_manual_leverage, manual_leverage= set_manual_leverage(y_dict)
                bot_message2 = 'Leverage Adjusted to:'
                send_text2 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message2
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response2 = requests.get(send_text2)

                
                bot_message = current_manual_leverage
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + str(bot_message)
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)

                bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                bot_message1 = current_manual_leverage

                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + str(bot_message) + str(bot_message1)
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)
                """
                bot_message3 = 'New Set Leverage'
                send_text3 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + str(bot_message3)
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response3 = requests.get(send_text2)

                bot_message1 = adjusted_manual_leverage
                send_text1 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + str(bot_message1)
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response1 = requests.get(send_text1)

                bot_message4 = 'You can click the Positions/Balances button to confirm your positions. Remember to start the bot for this to work'
                send_text4 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + str(bot_message4)
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response4 = requests.get(send_text1)
                """

            else: 
                bot_message = 'No valid message received from TradingView eligible of changing leverage on your Bybit Account'
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + str(bot_message)
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)
                print('Automated Webhook Sent for processing')

                bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                bot_message1 = 'No valid message received from TradingView eligible of changing leverage on your Bybit Account'

                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                response = requests.get(send_text)
        else: 
            print('you not authenticated to use this bot')
            print('token not found')
            print('You have wrong settings for your url. Click Webhook button to get correct format')

            # bot_message = 'token not found. Ensure you have correct token to use the bot'
            bot_message = 'you are not authenticated to use this bot\n Visit https://www.bybit.com/en-US/invite?ref=J6WWOV to create a Bybit account and get API keys.\n' 
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)
            print('Automated Webhook Sent for processing')
            
            bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
            bot_message1 = 'You have wrong settings for your url. Click Webhook button to get correct format'

            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)


            abort(400)
        print('_____________TESTING ASSET WITHOUT MODEL RESURCE______________________')
        return "WEBHOOK CALLED"    


def error_ret(error_rets):
    error_reta  = error_rets
def keysf(*args):
    saved_args = locals()
    keys = args
    print('------keyss--------secretss--------------')
    print(str(keys)[1:-1])
    #print(saved_args)
    global uid
    global keyss
    global secretss
    uid = keys[0]
    keyss = keys[1]
    secretss = keys[2]
    print('-------uids-------00000000---keyss--------secretss-------000000000-------')
    thisdict["Uid"] = uid
    thisdict["Key"] = keyss
    thisdict["Secret"] = secretss
    print(thisdict)

    with open('keys.json','w') as student_dumped :
        json.dump(thisdict,student_dumped)

    with open('keys.json', 'r+') as json_file:
        datasa = json.load(json_file)
        print('Data Read From File', datasa)
        datasa.update(thisdict)
        print('Updated Data', datasa)
        json_file.seek(0)
        json.dump(datasa,json_file)

    return datasa

def uids(*args):

    saved_args = locals()
    keys = args
    print('------keyss--------secretss--------------')
    print(str(keys)[1:-1])
    #print(saved_args)
    global keyss
    keyss = keys[0]
    print('---00000000---keyss--------secretss-------000000000-------')
    thisdict1["uids"] = keyss
    print(thisdict1)

    with open('uids.json', 'r+') as json_file:
        datasas = json.load(json_file)
        print('Data Read From File', datasas)
        datasas.update(thisdict1)
        print('Updated Data', datasas)
        json_file.seek(0)
        json.dump(datasas,json_file)

    with open('uids.json','w') as student_dumped :
        json.dump(thisdict1,student_dumped)

    return datasas

def buidtuid(*args):
    saved_args = locals()
    keysa = args
    print('------keyss--------secretss--------------')
    print(str(keys)[1:-1])
    #print(saved_args)
    global tuid
    global buidtuid
    uid = keysa[0]
    keyss = keysa[1]
        
    thisdicta =	{
    ""+uid+"": 0,
    ""+keyss+"": 0
    }

    print('-------uids-------00000000---keyss--------secretss-------000000000-------')
    thisdicta[""+uid+""] = uid
    thisdicta[""+keyss+""] = keyss
    print(thisdicta)

    with open('keys.json','w') as student_dumped :
        json.dump(thisdicta,student_dumped)

    with open('keys.json', 'r+') as json_file:
        datasa = json.load(json_file)
        print('Data Read From File', datasa)
        datasa.update(thisdict)
        print('Updated Data', datasa)
        json_file.seek(0)
        json.dump(datasa,json_file)

    return datasa

def parse__price_webhook(data):

    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_key).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_key
    for x in bybit_ids:
        api_key = bybit_ids
        #print('api_key', api_key)


    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_secret).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_secret
    for x in bybit_ids:
        api_secret = bybit_ids
        #print('api_secret', api_secret)

    print('---2222222---keyss--------secretss--------------')

    print('---2222222---keyss--------secretss--------------')
    trade_symbol = data['symbol']
    bybit1 = Bybit(api_key=api_key,
                secret=api_secret, symbol=data['symbol'], ws=True, test=False)

    print('api_key', api_key ,'api_secret', api_secret)
    #bybit1 = Bybit(api_key='JB76Njd3U64amNpkHF',
                #secret='LblyOzDpw23uwxfKxPH5itad50MIsTlW6iyW', symbol=data['symbol'], ws=True, test=True)
    
    print('------------API DATA------------------')

    api_data = bybit1.get_api_data()
    inviter_id = api_data['result']
    print(inviter_id)
    
    if inviter_id is not None : 
        inv = len(inviter_id)
        print('size of inviter result data is', inv)
        f=open("uids.txt", "a+")
        for x in range(len(inviter_id)):
            print('inviter_id', inviter_id[x]['inviter_id'])
            value_to_write = str(inviter_id[x]['inviter_id'])
            print('InviterID')
    else: 
        inv = 0
        print('size of inviter result data is None', inv )
    """
    print('Pulling SAVED ORDER ID')
    print(order_ids)
    print('=====================PRINT cancelled active order RRESULTS=====================================')
    cancelled_order_id  = bybit1.cancel_active_order(symbol = data['symbol'], order_id = order_ids)
    print(cancelled_order_id)

    print('-----------END OF GETTING-API DATA------------------')
    """
    position = bybit1.get_position_http()
    print('Position ----------------------------------------------------------')
    position_list = bybit1.get_position_list(symbol = data['symbol'])

    print('Cancel ALL Conditional Orders')

    bybit1.cancel_all_active_orders(symbol=data['symbol'])
    bybit1.cancel_all_conditional_orders(symbol=data['symbol'])
    if position_list is not None: 
        print('------------------------POSITION------LIST---------------------------------------')
        pl = position_list['result']
        if pl is not None: 
            print(pl)
            print('-------------------POSITION SIZE SIZE SIZE---------------------------------------')
            print(pl['size'])
            position_size  = pl['size']
            position_side  = pl['side']
            print('POSITION SIDE IS', position_side)
            if position_side == 'Sell':
                print('POSITION SIDE IS SELL')
                order_resp = bybit1.place_active_order(side='Buy', symbol=data['symbol'], order_type='Market', qty=position_size,time_in_force='PostOnly', reduce_only=False)
                position_side = 'Sell'
            if position_side == 'Buy':
                print('POSITION SIDE IS BUY')
                order_resp = bybit1.place_active_order(side='Sell', symbol=data['symbol'], order_type='Market', qty=position_size,time_in_force='PostOnly', reduce_only=False)
                position_side == 'Buy' 
            else: 
                print('End of Cancel of All Active, Conditional Orders and Positions')
        else : 
            print('no open positions')
    else: 
        print('Nothing to Close as no open positions')
    





def parse_webhook(webhook_data):

    data = ast.literal_eval(webhook_data)
    print('Data as Literal', data)
    with open('data.json', 'r+') as json_file:
        datasa = json.load(json_file)
        print('Data Read From File', datasa)
        datasa.update(data)
        print('Updated Data', datasa)
        #json_file.seek(0)
        #json.dump(datasa,data)
    return datasa


def set_leverage(webhook_data):
    data = ast.literal_eval(webhook_data)
    print('leverage Set data as Literal', data)
    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_key).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_key
    for x in bybit_ids:
        api_key = bybit_ids
        #print('api_key', api_key)


    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_secret).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_secret
    for x in bybit_ids:
        api_secret = bybit_ids
        #print('api_secret', api_secret)

    print('---2222222---keyss--------secretss--------------')

    print('---2222222---keyss--------secretss--------------')
    trade_symbol = data['symbol']
    bybit1 = Bybit(api_key=api_key,
                secret=api_secret, symbol=data['symbol'], ws=True, test=False)

    print('api_key', api_key ,'api_secret', api_secret)
    
    print('------------API DATA------------------')

    api_data = bybit1.get_api_data()
    inviter_id = api_data['result']
    print(inviter_id)
    
    if inviter_id is not None : 
        inv = len(inviter_id)
        print('size of inviter result data is', inv)
        f=open("uids.txt", "a+")
        for x in range(len(inviter_id)):
            print('inviter_id', inviter_id[x]['inviter_id'])
            value_to_write = str(inviter_id[x]['inviter_id'])
            print('InviterID')
    else: 
        inv = 0
        print('size of inviter result data is None', inv )

    print('-----------END OF GETTING-API DATA------------------')

    leverage = bybit1.get_leverage()
    print('Leverage ----------------------------------------------------------')
    print(leverage)
    print("Change Leverage")
    save_leverage = bybit1.change_leverage(trade_symbol, data['Leverage'])
    leverage_data = save_leverage
    print(save_leverage)
    print("Leverage Saved")



def close_webhook(webhook_data):
    data = webhook_data
    print('Trade Close Data as Literal', data)
    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_key).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_key
    for x in bybit_ids:
        api_key = bybit_ids
        #print('api_key', api_key)


    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_secret).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_secret
    for x in bybit_ids:
        api_secret = bybit_ids
        #print('api_secret', api_secret)

    print('---2222222---keyss--------secretss--------------')

    print('---2222222---keyss--------secretss--------------')
    trade_symbol = data['symbol']
    bybit1 = Bybit(api_key=api_key,
                secret=api_secret, symbol=data['symbol'], ws=True, test=False)

    print('api_key', api_key ,'api_secret', api_secret)
    
    print('------------API DATA------------------')

    api_data = bybit1.get_api_data()
    inviter_id = api_data['result']
    print(inviter_id)
    
    if inviter_id is not None : 
        inv = len(inviter_id)
        print('size of inviter result data is', inv)
        f=open("uids.txt", "a+")
        for x in range(len(inviter_id)):
            print('inviter_id', inviter_id[x]['inviter_id'])
            value_to_write = str(inviter_id[x]['inviter_id'])
            print('InviterID')
    else: 
        inv = 0
        print('size of inviter result data is None', inv )

    print('-----------END OF GETTING-API DATA------------------')
    
    position = bybit1.get_position_http()
    print('Position ----------------------------------------------------------')
    position_list = bybit1.get_position_list(symbol = data['symbol'])

    bybit1.cancel_all_active_orders(symbol=data['symbol'])

    #print('Order ID Passed to Cancel Conditional Order', order_ids)

    bybit1.cancel_all_conditional_orders(symbol=data['symbol'])

    #bybit1.cancel_conditional_order(order_id = order_ids)
    close = 'None'

    if position_list is not None: 
        print('POSITION -------------------LIST---------------------------------------')
        pl = position_list['result']
        if pl is None: 
            print('You have no open positions')
            close  = 'You have no open positions'
        else: 
            print(pl)
            print('-------------------POSITION SIZE SIZE SIZE---------------------------------------')
            print(pl['size'])
            position_size  = pl['size']
            position_side  = pl['side']
            print('POSITION SIDE IS', position_side)

            if position_side == 'Sell':
                print('POSITION SIDE IS SELL')
                order_resp = bybit1.place_active_order(side='Buy', symbol=data['symbol'], order_type='Market', qty=position_size,time_in_force='PostOnly', reduce_only=False)
                position_side = 'Sell'
                close  = 'Sell positions closed'   

            if position_side == 'Buy':
                print('POSITION SIDE IS BUY')
                order_resp = bybit1.place_active_order(side='Sell', symbol=data['symbol'], order_type='Market', qty=position_size,time_in_force='PostOnly', reduce_only=False)
                position_side == 'Buy'
                close  = 'Buy positions closed'   

    return close

def set_manual_leverage(manual_leverage_data):

    global manual_leverage
    global current_manual_leverage
    global adjusted_manual_leverage

    manual_leverage = 0
    current_manual_leverage = 0
    adjusted_manual_leverage = 0
    #data = ast.literal_eval(manual_leverage_data)
    data = manual_leverage_data

    print('leverage Set data as Literal', data)
    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_key).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_key
    for x in bybit_ids:
        api_key = bybit_ids
        #print('api_key', api_key)


    bybit_ids = ''
    with app.app_context():
        recordss = db.session.query(Telegram.api_secret).filter(Telegram.telegramid == data['TelegramID']).all()
        print(recordss)
        asset_to_idss = str(recordss)[1:-1]
        asset_to_idsss = str(asset_to_idss)[1:-1]
        asset_to_idssss = str(asset_to_idsss)[1:-1]
        bybit_ids = asset_to_idssss.replace("'", "")
        print('asset_to_id', bybit_ids)
    print('API Key Verification Data pulled from Database', bybit_ids)
    global api_secret
    for x in bybit_ids:
        api_secret = bybit_ids
        #print('api_secret', api_secret)

    print('---2222222---keyss--------secretss--------------')

    print('---2222222---keyss--------secretss--------------')
    trade_symbol = data['symbol']
    bybit1 = Bybit(api_key=api_key,
                secret=api_secret, symbol=data['symbol'], ws=True, test=False)

    print('api_key', api_key ,'api_secret', api_secret)
    
    print('------------API DATA------------------')

    api_data = bybit1.get_api_data()
    inviter_id = api_data['result']
    print(inviter_id)
    
    if inviter_id is not None : 
        inv = len(inviter_id)
        print('size of inviter result data is', inv)
        f=open("uids.txt", "a+")
        for x in range(len(inviter_id)):
            print('inviter_id', inviter_id[x]['inviter_id'])
            value_to_write = str(inviter_id[x]['inviter_id'])
            print('InviterID')
    else: 
        inv = 0
        print('size of inviter result data is None', inv )

    print('-----------END OF GETTING-API DATA------------------')

    current_manual_leverages = bybit1.get_leverage()
    current_manual_leverage = current_manual_leverages['result']
    print('current_manual_leverage -----------current_manual_leverage--------')
    print(current_manual_leverage)
    print("Change Leverage")
    save_leverage = bybit1.change_leverage(trade_symbol, data['Leverage'])
    print("\n\n\n***************************save leverage",save_leverage)
    manual_leverage = save_leverage['ret_msg']
    print(manual_leverage)
    print("Leverage Saved")    
    adjusted_manual_leverages = bybit1.get_leverage()
    adjusted_manual_leverage = adjusted_manual_leverages['result']
    print('current_manual_leverage -----------current_manual_leverage--------')
    print(adjusted_manual_leverage)

    return current_manual_leverage, adjusted_manual_leverage, manual_leverage

  

def checkPositionExists(user_trade_data):
    
    has_position = False
    textp =''
    print("Trade symbol...................", user_trade_data['symbol'])
    trade_symbol = user_trade_data['symbol']
    vvery12 = telegram_id
    with app.app_context():
            api_data = db.session.query(Telegram.api_key, Telegram.api_secret,Telegram.verified, Telegram.first_name,Telegram.second_name).filter(Telegram.telegramid==vvery12).all()

            #and thhis is API KEY AND SECRET of the Leder
        
    api_key = api_data[0][0]
    api_secret = api_data[0][1]
    
    try:
        bybit1 = Bybit(api_key=api_key,
                    secret=api_secret, symbol=trade_symbol, ws=True, test=False)


        position1 = bybit1.get_position_http()
        print('---------------------------New Position DATA----------------------------------')
        position_result1  = position1['result']
        json.dumps(position_result1, indent=2)
        # update1.message.reply_text('Your Bybit Positions')
        botu_message = 'Your Bybit Positions\n\n'
        print('auto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_resultauto_result')
        print(position_result1)
        # if position_result1['data'] is None : 
           
        # else: 
        print(len(position_result1))
        for x in range(len(position_result1)):
            # print("\n\n\n\n\n\n\n\n\n----------------------------&&&&&&&&&&&&&&&&&&&&&",position_result1[x]['symbol'], trade_symbol, user_trade_data['side'], position_result1[x]['side'] )
            
            if position_result1[x]['data']['symbol'] == trade_symbol and        position_result1[x]['data']['side'] == user_trade_data['side']:
                
                textp = "You are already in a trade:\n side | {0}| size | {1} \n Wait until the position is closed before opening another trade of the same asset.".format(position_result1[x]['data']['side'],position_result1[x]['data']['size'])
                print(textp)
                has_position = True
            if position_result1[x]['data']['symbol'] == trade_symbol and        position_result1[x]['data']['side'] == 'None':
                # update1.message.reply_text('You have no  open position')
                bot_message1 = 'You have no  open position'
                textp = bot_message1
                has_position = False


    except:
        textp = "There is something wrong, your current positions could not be fetched from Bybit." 

    return has_position, textp    
   

def assetSymbolSplitter(trade_symbol):
    if 'BTC'  in trade_symbol:
        return 'BTC'
    if 'ETH' in trade_symbol:
        return 'ETH'
    if 'EOS' in trade_symbol:
        return 'EOS'
    if 'XRP' in trade_symbol:
        return 'XRP'




def production_warning(env, args):
    if len(args):
        env = 'PRODUCTION' if env == 'prod' else 'STAGING'
        cmd = ' '.join(args)
        # allow some time to cancel commands
        for i in [4, 3, 2, 1]:
            click.echo(f'!! {env} !!: Running "{cmd}" in {i} seconds')
            time.sleep(1)





if __name__ == '__main__':
    
    app.run(debug = False, host="0.0.0.0",port=5002)
  
