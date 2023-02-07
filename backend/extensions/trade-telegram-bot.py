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
		  title = "ProfitSnipper BybitBot Api", 
		  description = "Admin panel",
          doc=False)

# adding the namespaces
api.add_namespace(userNS, path='/users')
api.add_namespace(authNS)

# Then we need a loop to work with
loop = asyncio.get_event_loop()
bot_token = "1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8"

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

# State definitions for top level conversation
SELECTING_ACTION, ADDING_MEMBER, ADDING_SELF, DESCRIBING_SELF = map(chr, range(4))
# State definitions for second level conversation
SELECTING_LEVEL, SELECTING_GENDER, SELECTING_TRADE = map(chr, range(4, 7))
# State definitions for descriptions conversation
SELECTING_FEATURE, SELECTING_FEATURE1, SELECTING_FEATURE2, SELECTING_FEATURE3, TYPING, TYPING1, TYPING2, TYPING3 = map(chr, range(7, 15))
# Meta states
STOPPING, SHOWING = map(chr, range(15, 17))
# Shortcut for ConversationHandler.END
END = ConversationHandler.END


# own settings 

ENDMANUAL =  map(chr, range(17, 18))
# Different constants for this example
(
    PARENTS,
    CHILDREN,
    NEIGHBORS,
    FOREIGNERS,
    SELF,
    GENDER,
    MALE,
    FEMALE,
    AUTOMATED,
    SETTINGS,
    SHOW_SETTINGS,
    WEBHOOK,
    AGE,
    NAME,
    BUYETH,
    BUYEOS,
    BUYXRP,
    SELLETH,
    SELLEOS,
    SELLXRP,
    LEVERAGE,
    CLOSE,
    POSITION,
    START_OVER,
    FEATURES,
    CURRENT_FEATURE,
    CURRENT_LEVEL,
    TAKEPROFIT, 
    STOPLOSS,
    AMOUNTSETTING,
    TRAILINGSTOP,
    NEWTRAILINGACTIVE,
    LEVERAGESETTING,
) = map(chr, range(18, 51))


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
    
    has_position = False
    textp =''
    print("Trade symbol...................", user_trade_data['symbol'])
    trade_symbol = user_trade_data['symbol']
    vvery12 = telegram_id
    with app.app_context():
            api_data = db.session.query(Telegram.api_key, Telegram.api_secret,Telegram.verified, Telegram.first_name,Telegram.second_name).filter(Telegram.telegramid==user_trade_data['TelegramID']).all()

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
   

@app.route('/webhook', methods=['POST'])
def webhook():
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

        y_dict = json.loads(datart)

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
            authenticated = bool(db.session.query(Telegram).filter_by(telegramid = int(y_dict['TelegramID'])).first())
            
        # if token in toList:
        if authenticated == True: 
            print('token found')
            #datart = datarc[1:-1]
            print('===================================================')
            print(datart)
            print('===================================================')
                
            bot_token = '1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8'
            bot_chatID =y_dict['TelegramID']
            print("bot chat id", bot_chatID)
            #datart = '{"type": "market", "side": "buy", "amount": "97", "leftAsset" : "BTC", "rightAsset" : "USDT","leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "TelegramID":"1093054762"}'
            if datart != None :     

                # bot_message = datart          
                # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                # #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                # response = requests.get(send_text)

                # bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                # bot_message1 = datart

                # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                # #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                # response = requests.get(send_text)

                # my code running perfectly
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

                    vvery12 = y_dict['TelegramID']
                    # if error_reta is not None: 
                    #     bot_message = ' *'+error_reta+'* ' + str(placedbtcvalue) + ' BTC contracts. *Filled entry* '''+ created_at +'' ' ''' + str(placedbtcvalue) +'' '@ $'+str(round(float(final_entry_price), 5))+''          
                    #     print("bot message ", bot_message)
                    #     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message
                    #     #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    #     response = requests.get(send_text)

                    #     bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                    #     bot_message1 = ''+ error_reta +'' 

                    #     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                    #     #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    #     response = requests.get(send_text)

                    # else: 
                    #     bot_message = error_reta
                    #     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                    #     #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    #     response = requests.get(send_text)

                    #     bot_message = '*Telegram ID* : ' ''+ str(bot_chatID) +'' ' \n ''  '
                    #     bot_message1 = ''+ error_reta +'' 

                    #     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1
                    #     #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    #     response = requests.get(send_text)
                    if ret_msg == 'OK' or ret_msg == 'ok':
                        # print(float(placed_btc_value))
                        # update1.message.reply_text(' *Manual Order Received: Buy* ' + str(round(float(placed_btc_value), 5)) + ' BTC contracts\n \n'
                        #         'Filled entry ' ''+ created_at +'' ' \n \n ' 
                        #         '' + str(round(float(placed_btc_value), 5)) +'' '@ $'+str(round(float(final_entry_price), 5))+'')
                        

                        
                        
                        bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                        bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                        bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                        bot_message3 = '*Automated Order Received: * ' + str(placedbtcvalue) + ' ' + y_dict['symbol'] + ' \n '' '
                        bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                        bot_message5 = '' + str(placedbtcvalue) +' BTC' '@ $'+str(round(float(final_entry_price), 5))+''


                        
                        # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        # #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        # response = requests.get(send_text)

                        # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                        # #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        # response = requests.get(send_text)

                        
                        textp = bot_message3 + bot_message4 + bot_message5

                    

                    if error_reta.startswith('TrailingStop:') or ret_msg.startswith('TrailingStop:'):
                        print(float(placed_btc_value))
                        # update1.message.reply_text(error_reta)
                        

                        # update1.message.reply_text(' *Manual Order Received: Buy* ' + str(round(float(placed_btc_value), 5)) + ' BTC contracts\n \n'
                        #         'Filled entry ' ''+ created_at +'' ' \n \n ' 
                        #         '' + str(round(float(placed_btc_value), 5)) +'' '@ $'+str(round(float(final_entry_price), 5))+'')

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
                        # update1.message.reply_text('Your buy Order Not successful')
                        # update1.message.reply_text('You have no funds in your Bybit Account')
                        # update1.message.reply_text('Top up to continue using the Bot')

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
                        # update1.message.reply_text('Your sell Order Not successful though leverage was set')
                        # update1.message.reply_text('Your quantity was not correct, you can reduce the percentage of amount. ')
                        # update1.message.reply_text('Or you can top up to continue using the Bot')

                        # update1.message.reply_text(' *Manual Order Received: Buy* ' + str(round(float(placed_btc_value), 5)) + ' BTC contracts\n \n'
                        #         'Filled entry ' ''+ created_at +'' ' \n \n ' 
                        #         '' + str(round(float(placed_btc_value), 5)) +'' '@ $'+str(round(float(final_entry_price), 5))+'')


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
                        # update1.message.reply_text('You have insuffient Balance to Place this Order. Check the percentage of Amount you are passing\n')
                        # update1.message.reply_text('Your quantity was not correct, you can reduce the percentage of amount. ')
                        # update1.message.reply_text('Or you can top up to continue using the Bot')
                        # update1.message.reply_text('Type /stop to restart the bot')
                        

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
            bot_message = 'you are not authenticated to use this bot\n Visit http://bybit.cm to create a Bybit account and get API keys.\n' 
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

@app.route('/close', methods=['GET','POST'])
def close():
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
        # y_dict = ast.literal_eval(datart)
        y_dict = json.loads(datart)
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
            authenticated = bool(db.session.query(Telegram).filter_by(telegramid = int(y_dict['TelegramID'])).first())
            
        # if token in toList:
        if authenticated == True: 
            print('token found')
            #datart = datarc[1:-1]
            print('===================================================')
            print(datart)
            print('===================================================')
                
            # y_dict = ast.literal_eval(datart)
            bot_token = '1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8'
            y_dict = json.loads(datart)
            bot_chatID = y_dict['TelegramID']
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
            bot_message = 'you are not authenticated to use this bot\n Visit http://bybit.cm to create a Bybit account and get API keys.\n' 
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
        

@app.route('/leverage', methods=['GET','POST'])
def leverage():
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
        y_dict = json.loads(datart)
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
            authenticated = bool(db.session.query(Telegram).filter_by(telegramid = int(y_dict['TelegramID'])).first())
            
        # if token in toList:
        if authenticated == True: 
            print('===================================================')
            print(datart)
            print('===================================================')
            # y_dict = ast.literal_eval(datart)
            y_dict = json.loads(datart)
            bot_token = '1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8'
            bot_chatID = y_dict['TelegramID']
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
            bot_message = 'you are not authenticated to use this bot\n Visit http://bybit.cm to create a Bybit account and get API keys.\n' 
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

# This function gets the wallet balances given an asset
def getAssetWalletBalance(bybit1,asset):
    wallet_balance = bybit1.get_wallet_balance(asset)
    print('Wallet Balance ----------------------------------------------------------')
    
    print(wallet_balance)
    print(wallet_balance['result'][asset]['available_balance'])
    wbalance = wallet_balance['result'][asset]['available_balance']
    intwalletbalance = wallet_balance['result'][asset]['available_balance']
    return wallet_balance, wbalance, intwalletbalance

# This function cleans the data ----- converts the "None" to None
def orderDataCleaner(data):
    for i in data:
        if data[i] == "None":
            data.update({i:None})
    return data

# This function gets the last price
def getLastPrice(bybit1, symbol):
    ticker = bybit1.get_tickers(symbol)
    print(json.dumps(ticker, indent=2))
    tickers = ticker["result"]
    print("Tickers ",tickers)
    tick = tickers[0]
    #print("Last Price", tick['last_price'])
    last_price = float(tick['bid_price'])
    return last_price

# This function calcutes the order quantity from the percentage passed on the data
def calcQuantity(bybit1,data):
    trade_symbol = data['symbol']
    last_price = getLastPrice(bybit1, trade_symbol)
    if 'BTC'  in trade_symbol:
        wallet_balance, wbalance, intwalletbalance = getAssetWalletBalance(bybit1,'BTC')
    if 'ETH' in trade_symbol:
        wallet_balance, wbalance, intwalletbalance = getAssetWalletBalance(bybit1,'ETH')
    if 'EOS' in trade_symbol:
        wallet_balance, wbalance, intwalletbalance = getAssetWalletBalance(bybit1,'EOS')
    if 'XRP' in trade_symbol:
        wallet_balance, wbalance, intwalletbalance = getAssetWalletBalance(bybit1,'XRP')
    
    amnt = wbalance

    print("Bid Price Value Two", last_price)
    print('WALLET BALANCE FOR THIS SYMBOL')

    leverage = bybit1.get_leverage()
    print('Leverage ----------------------------------------------------------')
    print(json.dumps(leverage, indent=2))
    leverages = leverage["result"][trade_symbol]['leverage']
    print("Leverage Value", leverages)
    
    trade_amount  = (amnt*leverages)*(float(data['amount'])/100)
    tr_amnt = trade_amount*last_price
    return tr_amnt

# This function gets the minimum parameter for placing an order
def intialOrderDataFilter(bybit1,data):
    data = orderDataCleaner(data)
    trade_symbol = data['symbol']
    orderData = {
        
        'side': data['side'],
        'symbol':data['symbol'],
        'order_type': data['type'],
        'qty': calcQuantity(bybit1,data),
        'price': None,
        'time_in_force': 'PostOnly',
        'take_profit': None,
        'stop_loss': None,
        'order_link_id': None
        }
        
    return orderData

# This function prepares the conditional parameters it recalculates the  actual parameters 
def conditionalOrderDataFilter(bybit1, data):
    data = orderDataCleaner(data)
    trade_symbol = data['symbol']
    conditionalData = {
        "symbol":data["symbol"],
        'take_profit': data["takeProfit"],
        'stop_loss': data["stopLoss"],
        'trailing_stop': data["trailingStop"],
        'new_trailing_active': data["new_trailing_active"]
    }
    for i in conditionalData:
        if conditionalData[i] != None:
            lastPrice = getLastPrice(bybit1,trade_symbol)
            if data["side"] == "Buy":
                if i == "take_profit":
                    take_profit = lastPrice + (float(conditionalData[i])/100) * lastPrice
                    conditionalData.update({i:round(take_profit,3)})

                if i == "stop_loss":
                    stop_loss = lastPrice - (float(conditionalData[i])/100) *lastPrice
                    conditionalData.update({i:round(stop_loss,3)})

                if i == "trailing_stop":
                    trailing_stop = lastPrice * (float(conditionalData[i])/100)
                    conditionalData.update({i:round(trailing_stop,3)})

                if i == "new_trailing_active":
                    new_trailing_active = lastPrice + (float(conditionalData[i])/100)*lastPrice
                    conditionalData.update({i:round(new_trailing_active,3)})

            if data["side"] == "Sell":
                if i == "take_profit":
                    take_profit = lastPrice - (float(conditionalData[i])/100) * lastPrice
                    conditionalData.update({i:round(take_profit,3)})

                if i == "stop_loss":
                    stop_loss = lastPrice + (float(conditionalData[i])/100) *lastPrice
                    conditionalData.update({i:round(stop_loss,3)})

                if i == "trailing_stop":
                    trailing_stop = lastPrice * (float(conditionalData[i])/100)
                    conditionalData.update({i:round(trailing_stop,3)}) 

                if i == "new_trailing_active":
                    new_trailing_active = lastPrice - (float(conditionalData[i])/100)*lastPrice
                    conditionalData.update({i:round(new_trailing_active,3)})

    return conditionalData

#get the user api data from the database 
def getUserApiData(data):
    with app.app_context():
        apiData = db.session.query(Telegram).filter(Telegram.telegramid == data['TelegramID']).first()
    return apiData 
def send_order_v2(data):
    trade_symbol = data['symbol']
    apiData = getUserApiData(data)

    api_key = apiData.api_key
    api_secret = apiData.api_secret

    bybit1 = Bybit(api_key=api_key,
                secret=api_secret, symbol=trade_symbol, ws=True, test=False)
    # filter the data for initial order parameters 
    intialOrderData =intialOrderDataFilter(bybit1, data)
    # filter the data conditional data
    conditionalData =conditionalOrderDataFilter(bybit1,data)

    # print("Data 1", intialOrderData)
    # print("\n data 2", conditionalData)
     
    order_resp1 = bybit1.place_active_order_v2(intialOrderData)
    print("intial order Response", order_resp1)
    order_resp2 = bybit1.place_active_order_ts_v2(conditionalData)
    print("second orderRespose", order_resp2)

    # {'ret_code': 0, 'ret_msg': 'OK', 'ext_code': '', 'ext_info': '', 'result': {'user_id': 1795752, 'order_id': '174b28d7-0756-4bf0-aa19-aaf6ad396c4f', 'symbol': 'ETHUSD', 'side': 'Buy', 'order_type': 'Market', 'price': 2491.1, 'qty': 45, 'time_in_force': 'ImmediateOrCancel', 'order_status': 'Created', 'last_exec_time': 0, 'last_exec_price': 0, 'leaves_qty': 45, 'cum_exec_qty': 0, 'cum_exec_value': 0, 'cum_exec_fee': 0, 'reject_reason': 'EC_NoError', 'order_link_id': '', 'created_at': '2021-04-21T23:38:04.831Z', 'updated_at': '2021-04-21T23:38:04.831Z'}, 'time_now': '1619048284.831643', 'rate_limit_status': 99, 'rate_limit_reset_ms': 1619048284829, 'rate_limit': 100}

    # {'ret_code': 0, 'ret_msg': 'OK', 'ext_code': '', 'ext_info': '', 'result': {'id': 0, 'user_id': 1795752, 'symbol': 'ETHUSD', 'side': 'Buy', 'size': 45, 'position_value': 0.01896733, 'entry_price': 2372.50050482, 'risk_id': 11, 'auto_add_margin': 0, 'leverage': 10, 'position_margin': 0.00189674, 'liq_price': 2176.65, 'bust_price': 2156.85, 'occ_closing_fee': 1.565e-05, 'occ_funding_fee': 0, 'take_profit': 2374.35, 'stop_loss': 2367.7, 'trailing_stop': 0, 'position_status': 'Normal', 'deleverage_indicator': 2, 'oc_calc_data': '{"blq":0,"slq":0,"bmp":0,"smp":0,"fq":-45,"bv2c":0.101575,"sv2c":0.101425}', 'order_margin': 0, 'wallet_balance': 0.00951358, 'realised_pnl': -3.891e-05, 'cum_realised_pnl': -0.00411842, 'cum_commission': 0, 'cross_seq': 2996712666, 'position_seq': 1025853193, 'created_at': '2020-10-05T20:08:23Z', 'updated_at': '2021-04-21T23:38:05.504171572Z', 'ext_fields': {'trailing_active': '0', 'sl_trigger_by': 'LastPrice', 'tp_trigger_by': 'LastPrice', 'v': 61972, 'mm': 0}}, 'time_now': '1619048285.504621', 'rate_limit_status': 74, 'rate_limit_reset_ms': 1619048285503, 'rate_limit': 75}

    if order_resp2["ret_msg"] == 'OK' or order_resp2["ret_msg"]=='Ok':
        ret_msg =order_resp2["ret_msg"]
        error_reta = order_resp2["ret_msg"]
        placed_btc_value =order_resp2["result"]['size']/order_resp2["result"]["entry_price"]
        created_at = order_resp1["result"]['created_at']
        final_entry_price = order_resp2["result"]["entry_price"]
        created_at = dateFormater(created_at)
        return ret_msg, error_reta,  placed_btc_value, created_at, final_entry_price

    if order_resp2["ret_msg"] != "OK" and  order_resp1["ret_msg"]=="OK":
        ret_msg =order_resp2["ret_msg"]
        error_reta = order_resp2["ret_msg"]
        placed_btc_value =order_resp1["result"]['qty']/order_resp1["result"]["price"]
        created_at = order_resp1["result"]['created_at']
        final_entry_price = order_resp1["result"]["price"]
        created_at = dateFormater(created_at)
        return ret_msg, error_reta,  placed_btc_value, created_at, final_entry_price

    else:
        # return the error message only
        return order_resp1["ret_msg"], order_resp1["ret_msg"], '', '', ''

def dateFormater(date):
    date = date[:19]
    created_at = date.replace("T"," at"+" ")
    created_at = "on"+" " + created_at
    return created_at

# Helper
def _name_switcher(level):
    if level == PARENTS: #parents here is a branch for manual trading
        return 'Manual Trading', 'Automated Trading', 'Defaut Settings' 
    if level == CHILDREN: #children here is a branch for automated trading
        return 'Manual Trading', 'Automated Trading', 'Defaut Settings'
    if level == NEIGHBORS: #parents here is a branch for manual trading
        return 'Manual Trading', 'Automated Trading', 'Defaut Settings' 
    if level == FOREIGNERS: #children here is a branch for automated trading
        return 'Manual Trading', 'Automated Trading', 'Defaut Settings' 
    
update1 = {}
print("------------UPDATE 1- INIT----------------", update1)
callback1 = {}
print("------------CALLBACK 1---INIT--------------", callback1)


# return all the user details to avoid crushes in multisking
def getUserDetails(update: Update, context: CallbackContext) -> None:
    if update.callback_query == None:
        user = update.message.from_user
        print(user)
        global telegram_id, first_name
        telegram_id = user.id
        first_name = user.first_name
        second_name = user.last_name
    if update.callback_query != None:
        print("update---------------------------------------", update)
        user = update.callback_query.message.chat
        print('-------------------------------', user)
        telegram_id = user.id
        first_name = user.first_name
        second_name = user.last_name
        print('first name...............',first_name)

    if first_name == 'None' or first_name == None:
        first_name = ''
    if second_name == 'None' or second_name == None:
        second_name = ''
    return user, telegram_id, first_name, second_name


# Top level contversation callbacks
def start(update: Update, context: CallbackContext) -> None:
    global update1
    global callback1
   
    update1 = update
    callback1 = CallbackContext

    print('update1',update1)
    print('callback1', callback1)
    
    user, telegram_id, first_name, second_name = getUserDetails(update, context)

    logger.info("User %s started the conversation.", first_name)
    print('telegram id------ ', telegram_id)
    """Select an action: Adding parent/child or show data."""
    text = (
        'Ensure you have been validated using your Bybit API Key and Secret'
        
    )
    buttons = [
        [
            InlineKeyboardButton(text='Begin Trading', callback_data=str(ADDING_MEMBER)),
            InlineKeyboardButton(text='Verify Bybit keys', callback_data=str(ADDING_SELF)),
        ],
        [
            # InlineKeyboardButton(text='Show data', callback_data=str(SHOWING)),
            InlineKeyboardButton(text='Done', callback_data=str(END)),
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we're starting over we don't need do send a new message
    if context.user_data.get(START_OVER):

        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
        # update1.message.reply_text(text=text, reply_markup=keyboard)
    else:
       
        update.message.reply_text(
            'Hello, Welcome to ProfitSniper Bybit Trading Referral Bot.\n Click this link http://bybit.cm to create a Bybit account and get your Bybit API keys. \n Click Start Trading to Proceed'
        )
        update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_ACTION


def adding_self(update: Update, context: CallbackContext) -> None:
    
    context.user_data[CURRENT_LEVEL] = SELF
    text = 'By verifying your API keys you accept you are using this bot at your own risk!'
    button = InlineKeyboardButton(text='API DATA', callback_data=str(MALE))
    keyboard = InlineKeyboardMarkup.from_button(button)

    update.callback_query.answer()
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return DESCRIBING_SELF


def displayDefaultSettings(update: Update, context: CallbackContext, levelinput, user_data):
    user, telegram_id, first_name, second_name = getUserDetails(update, context)
    text = ''
    textp = 'Invalid selection'
    ret_msg, error_reta, placed_btc_value, created_at, final_entry_price = '', '', '','',''
    key = ''
    secret = ''
    text_except = ''
    text_if1 = ''
    text_if2 = ''
    buy = ''
    sell = ''
    text = 'Null'
    textp ='Done'
    # first_name = ''
    # second_name = ''
    vvery12 = ''

    text2 = ""
    text_c =''

    text_if1 = '' 
    text_if2 = '' 
    text_except = '' 
    text_c = '' 
    buy_c = '' 
    sell_c = '' 
    key_c = '' 
    secret_c = '' 
    text_if1_c = '' 
    text_if2_c = '' 
    text_except_c = ''

    text_cN = '' 
    buy_cN = ''
    sell_cN = '' 
    key_cN = '' 
    secret_cN = '' 
    text_if1_cN = '' 
    text_if2_cN = '' 
    text_except_cN = '' 

    text_cF = '' 
    buy_cF = '' 
    sell_cF = '' 
    key_cF = '' 
    secret_cF = '' 
    text_if1_cF = '' 
    text_if2_cF = '' 
    text_except_c = ''
    # user_data_buy = {}
    # user_data_sell = {}
    # user_data_take_profit = {}
    # user_data_stop_loss = {}
    # user_data_amount_setting = {}                
    # user_data_trailing_stop = {}
    # user_data_trailing_active = {}
    # user_data_leverage_setting = {}
    user_data = context.user_data
    
    print(user_data, "USER DATA")
    
    level = context.user_data[CURRENT_LEVEL]

    if level == levelinput:
        # AND INSIDE HERE, WE HAVE MANY OTHER OPTIONS LIKE Manual Trading, Automated Trading, Default Settings, Show Settings
        # and these will be repeated for variety of symbols. 
        # under this level for example there are SELECT[GENDER] which are options availed to process 
        # Manual Trading, Automated Trading, Default Settings, Show Settings
        # Manual Trading (FEMALE), Automated Trading(AUTOMATED), Default Settings(), Show Settings(SHOW_SETTINGS) 
        print('------------------------LEVEL -----------------------------------------------------------------', level)

        # user_data_take_profit = None
        # user_data_stop_loss = None
        # user_data_amount_setting = None                 
        # user_data_trailing_stop = None
        # user_data_trailing_active = None
        # user_data_leverage_setting = None
    
        male, female, automated = _name_switcher(level)
        print(user_data[level])
        print('gender below')
        print(GENDER)
        print('either male or female below')
        print(FEMALE)
        for person in user_data[level]:
            #the below code doesn't execute settings, just bad naming. It executes BTC Orders
            if person[GENDER] == SETTINGS: #Executes Bybit Trading. I suppose this has changed to TRADE BTC
                gender = female 
                # BUYETH,BUYEOS,BUYXRP,SELLETH,SELLEOS,SELLXRP,
                text += f"\n{gender}: Buy BTC: {person.get(NAME, '-')}, Buy ETH: {person.get(BUYETH, '-')}, Buy EOS: {person.get(BUYEOS, '-')}, Buy XRP: {person.get(BUYXRP, '-')}, Sell BTC: {person.get(AGE, '-')}, Sell ETH: {person.get(SELLETH, '-')}, Sell EOS: {person.get(SELLEOS, '-')}, Sell XRP: {person.get(SELLXRP, '-')}"

                
                # user_data_buy_eth, user_data_buy_eos, user_data_buy_xrp, user_data_buy_eth, user_data_buy_eos, user_data_buy_xrp
                user_data_buy =f"{person.get(NAME)}" #BUY BTC USD
                user_data_buy_eth =f"{person.get(BUYETH, '-')}" #BUY ETH USD
                user_data_buy_eos =f"{person.get(BUYEOS, '-')}" #BUY EOS USD
                user_data_buy_xrp =f"{person.get(BUYXRP, '-')}" #BUY XRP USD
                user_data_sell =f"{person.get(AGE)}" #SELL BTC USD
                user_data_sell_eth =f"{person.get(SELLETH, '-')}" #BUY ETH USD
                user_data_sell_eos =f"{person.get(SELLEOS, '-')}" #BUY EOS USD
                user_data_sell_xrp =f"{person.get(SELLXRP, '-')}" #BUY XRP USD
                user_data_close = f"{person.get(CLOSE)}"
                user_data_position = f"{person.get(POSITION)}"
                user_data_leverage = f"{person.get(LEVERAGE)}"
                user_data_take_profit =f"{person.get(TAKEPROFIT)}"
                user_data_stop_loss =f"{person.get(STOPLOSS)}"
                user_data_amount_setting = f"{person.get(AMOUNTSETTING)}"
                user_data_trailing_stop = f"{person.get(TRAILINGSTOP)}"
                user_data_trailing_active = f"{person.get(NEWTRAILINGACTIVE)}"
                user_data_leverage_setting = f"{person.get(LEVERAGESETTING)}"

                # if user_data_take_profit is None :
                #     user_data_take_profit = 'None'
                # if user_data_stop_loss is None :
                #     user_data_stop_loss = 'None'
                # if user_data_amount_setting is None :
                #     user_data_amount_setting = 'None'
                # if user_data_trailing_stop is None :
                #     user_data_trailing_stop = 'None'
                # if user_data_trailing_active is None :
                #     user_data_trailing_active = 'None'
                # if user_data_leverage_setting is None :
                #     user_data_leverage_setting = 'None'

                print("user data close", user_data_close)
                print('user_data_leverage', user_data_leverage)
                print('user_data_position', user_data_position)
                print("user data user_data_take_profit", user_data_take_profit)
                print('user_data_stop_loss', user_data_stop_loss)
                print('user_data_amount_setting', user_data_amount_setting)                    
                print("user data user_data_trailing_stop", user_data_trailing_stop)
                print('user_data_trailing_active', user_data_trailing_active)
                print('user_data_leverage_setting', user_data_leverage_setting)
                #ret_msg, error_reta, placed_btc_value, created_at, final_entry_price = send_order(order)
                secret = f"{person.get(AGE, '-')}"
                vvery12 = telegram_id
                print('telegram_id', vvery12)

                datasa = checkTradedatadb(level)

                 # Data to be written 
                passed_dictionary ={ 
                    "takeProfit" : user_data_take_profit, 
                    "stopLoss" : user_data_stop_loss, 
                    "amount" : user_data_amount_setting, 
                    "trailingStop" : user_data_trailing_stop,
                    "new_trailing_active" : user_data_trailing_active, 
                    "Leverage" : user_data_leverage_setting,
                    "type":'Market',
                    "TelegramID" : telegram_id
                } 
                print("\n\n\n printing datasa",datasa)
                print("The passed data", passed_dictionary)
                # write to the database instead


                # compare the data passed with the data previously recorded to properly change the altered values only.

                

                for i in passed_dictionary:
                    if i != 'TelegramID':
                        
                        if passed_dictionary[i] != datasa[i] and passed_dictionary[i]=='None':
                            passed_dictionary.update({i:datasa[i]})

                        if passed_dictionary[i] != datasa[i] and passed_dictionary[i]!='None':
                            if passed_dictionary[i] == '0':
                                passed_dictionary.update({i:'None'})
                            else:
                                passed_dictionary.update({i:passed_dictionary[i]})
                        
                        if passed_dictionary[i] == datasa[i] and passed_dictionary[i]!='None':
                            if passed_dictionary[i] == '0':
                                passed_dictionary.update({i:'None'})
                        # check if the the passed is not integer if the user enters any non int convert to None
                        try:
                            float(passed_dictionary[i])
                        except:
                            passed_dictionary.update({i:'None'})

                
                print("*******************Printing the latest update of passed dictionary")
                print(passed_dictionary)


               
                
                vvery12 = telegram_id

        # access the database

        with app.app_context():
            api_data = db.session.query(Telegram.api_key, Telegram.api_secret,Telegram.verified, Telegram.first_name,Telegram.second_name).filter(Telegram.telegramid==vvery12).all()

        #and thhis is API KEY AND SECRET of the Leder
        yes  = 'Yes'
        print("API data -----------", api_data)
        try:
            api_key = api_data[0][0]
            api_secret = api_data[0][1]
            res = api_data[0][2]
            first_name = api_data[0][3]
            second_name = api_data[0][4]
            if first_name == None:
                first_name = ''
            if second_name == None:
                second_name == ''
        except:
            api_key = ''
            api_secret = ''
            res = ''
            first_name = ''
            second_name = ''


        print('firstname', 'secondname')
        print(first_name, second_name)
        second_name = ''

        print("printing response", second_name)

        # leverage = 'Leverage'
        vvery12 = telegram_id
        # user_data and user_data_sell 
        # if user_data != 'None': 
        print("user data user_data_take_profit", user_data_take_profit)
        print('user_data_stop_loss', user_data_stop_loss)
        print('user_data_amount_setting', user_data_amount_setting)                    
        print("user data user_data_trailing_stop", user_data_trailing_stop)
        print('user_data_trailing_active', user_data_trailing_active)
        print('user_data_leverage_setting', user_data_leverage_setting)

        
        print('user_datauser_datauser_datauser_datauser_data', user_data)
        print('user_data_sell user_data_sell user_data_sell user_data_sell user_data_sell user_data_sell', user_data_sell)

        print('Telegram ID',vvery12)
        
       
        if yes == res: 
            print('Started working on Leverage Operations')
            # update1.message.reply_text('Settings Data Passed To Database')
            #update.message.reply_text('Manual Order sent: Sell' + float(placed_btc_value) + ' BTC contracts\n \n')
            #uids13 = user_data['Leverage']
            print('passed_dictionary',passed_dictionary)

            if level == PARENTS:
                 
                asset = 'BTCUSD'
              
                
            if level == CHILDREN:

                asset = 'ETHUSD'

                
            if level == NEIGHBORS:
                asset = 'EOSUSD' 
               
            if level == FOREIGNERS:
                asset = 'XRPUSD'
            
            print('Printing the asset',asset)


            with app.app_context():
               
                asset_exists = bool(db.session.query(TradeDataDefaults).filter_by(telegramid = vvery12, asset = asset).first())
            
                if asset_exists == True:
                    try:
                        db.session.query(TradeDataDefaults).filter_by(telegramid =int(passed_dictionary['TelegramID']), asset=asset).update({
                        TradeDataDefaults.mtype:'Market',
                        TradeDataDefaults.amount:passed_dictionary['amount'],
                        TradeDataDefaults.takeprofit:passed_dictionary['takeProfit'],
                        TradeDataDefaults.stoploss:passed_dictionary['stopLoss'],
                        TradeDataDefaults.trailingstop:passed_dictionary['trailingStop'],
                        TradeDataDefaults.newtrailingactive:passed_dictionary['new_trailing_active'],
                        TradeDataDefaults.leverage:passed_dictionary['Leverage']

                        })
                        db.session.commit()
                        
                    except:
                        text = "Default setting not updated\n Please register your API data and try again"

                else:
                     todo = TradeDataDefaults.create( asset = asset, mtype = 'Market', amount= passed_dictionary['amount'], telegramid = int(passed_dictionary['TelegramID']),takeprofit= passed_dictionary['takeProfit'], stoploss = passed_dictionary['stopLoss'] , trailingstop =passed_dictionary['trailingStop'], newtrailingactive = passed_dictionary['new_trailing_active'], leverage= passed_dictionary['Leverage'])


                # Data will be processed here
                datasa1 = checkTradedatadb(level)
                text = str(datasa1)
                textp = text
        
        else : 
            
            # update1.message.reply_text(
            # 'You must have valid Bybit API key and Secret \n \n'
            # '\n \n '
            # 'Type /start to enter your Capture your details afresh \n \n'.format(text.lower()))
            
            textp = "You must have valid Bybit API key and Secret \n \n"
            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
            bot_message3 = 'User tried set leverage but doesn\'t have valid Bybit API Key and Secret'

            text_except = 'You must have valid Bybit API key and Secret'

            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)

            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
            response = requests.get(send_text)
        user_data_buy = {}
        user_data_sell = {}
        user_data_take_profit = {}
        user_data_stop_loss = {}
        user_data_amount_setting = {}                
        user_data_trailing_stop = {}
        user_data_trailing_active = {}
        user_data_leverage_setting = {}

       
        return textp
        
def verifyApiData(update: Update, context: CallbackContext, level, user_data):
    key = ''
    text = 'Null'
    text_except = ''
    text_if1 = ''
    text_if2 = ''
    buy = ''
    sell = ''
    secret = ''
    bot_token = '1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8'
    user, telegram_id, first_name, second_name = getUserDetails(update, context)
    vvery12 = telegram_id
    for person in user_data[level]:
        # people = user_data.get(level)
        #the below code doesn't execute settings, just bad naming. It executes BTC Orders
        if person[GENDER] == MALE: #Executes Bybit Trading. I suppose this has changed to TRADE BTC
            # gender = female 
            text += f"\nName: {person.get(NAME, '-')}, Age: {person.get(AGE, '-')}"

            key =f"{person.get(NAME, '-')}"
            secret = f"{person.get(AGE, '-')}"
            
            print('Key', key, 'Secret', secret)
            
            #if secretsa and key in user_data: 
            key1 = secret
            key2 = key
            print('Secret',key1)
            print('API key',key2)
            bybit1 = Bybit(api_key=key2,
                    secret=key1, symbol="BTCUSD", ws=True, test=False)
            print("bybit1", bybit1)
            
            api_data = bybit1.get_api_data()
            print('api_data', api_data)
            inviter_id = api_data['result']
            print('inviter_id',inviter_id)
            if api_data['ret_msg'].startswith('invalid request') and api_data['ret_code'] == 10002:
                textp = "There is a problem verifying your keys at the moment\n Please correct your date and time and try again"

            else:
                if api_data['ret_msg']!='ok':
                    
                    text1 = ' Your Bybit API Data is incorrect. Confirm they are correct. \n'

                    text2 = 'Visit https://www.bybit.com/app/user/api-management to get keys \n'
                    
                    text3 = 'please verify your Bybit keys before proceeding to trade.\n'
                    
                    
                    textp = text1 + text2 + text3
                    
                    
                    print(textp)
                    

                else: 
                    main_invitor_id = '506788'
                    inviter_idt = ''
                    res = ''
                    bybit_ids = ''
                    for x in range(len(inviter_id)):
                        print('inviter_id unique specification', inviter_id[x]['inviter_id'])
                        inviter_idt = str(inviter_id[x]['inviter_id'])
                        print('inviter_idt', inviter_idt)
                        # shida inatokea hapa
                        with app.app_context():
                            asset_to_ids = db.session.query(BybitModel.bybitid).all()
                        print(asset_to_ids)
                        asset_to_idss = str(asset_to_ids)[1:-1]
                        print(asset_to_idss)
                        asset_to_idsss = str(asset_to_idss)[1:-1]
                        print(asset_to_idsss)
                        bybit_ids = asset_to_idsss.replace(",", "")
                        print('asset_to_id', bybit_ids)

                    print('Secret Verification Data pulled from Database', bybit_ids)
                    for x in bybit_ids:
                        res = bybit_ids
                    print('result that we need to compare with inviter_id data below', res)
                    telegram_dict = []
                    # if inviter_idt == res:
                    # I have hard coded the inviter ID below, but this can be dynamically pulled fromm DB as was setup in the above code 
                    # that's returning variable, "res"
                    
                    if inviter_idt == main_invitor_id:
                        inv = len(inviter_id)
                        #if these two values are equal we proceed to update the the table verified field to Yes
                        #Thos code line below will tell us if that UID is really available
                        #that is if really size of inv variable below is greater than 1
                        print('size of inviter result data is', inv)
                        with app.app_context():
                            size_f = Telegram.query.all()
                        print('Size of Assets Model Schema',len(size_f))
                        
                        for j in range(0, len(size_f)):
                            sm = size_f[j].api_secret
                            telegram_dict.append(sm)

                        print('Data from Telegram Data Table')
                        print(telegram_dict)

                        if key1 in telegram_dict:

                            print('Starting Telegram Bot Data Update')
                            print('telegram_id   ',telegram_id)
                            print('firstname', first_name)

                            # db.session.query(Telegram).filter(Telegram.api_secret == key1).update({Telegram.inviter_id: 10000, Telegram.verified: 'Yes', Telegram.telegramid: telegram_id, Telegram.api_key: key2, Telegram.api_secret: key1, Telegram.first_name: first_name})

                            # db.session.commit()
                            with app.app_context():
                                db.session.query(Telegram).filter(Telegram.telegramid == telegram_id).delete()

                                db.session.commit()

                                todo = Telegram.create(inviter_id = inviter_idt, verified = 'Yes', telegramid = telegram_id, api_key = key2, api_secret = key1, first_name = first_name, second_name = second_name)
                                
                            print('Telegram Data Updated')

                            text1 =' Your New Data has been updated \n '
                            

                            text2 = ' Your Bybit data has been Verified too. You can proceed and start trading \n'
                            
                            
                            text3 ='Bybit ID is valid \n \n'
                            'You can proceed to manual trading via  this bot, or setup automated trading with TradingView'
                            
                            # update.callback_query.edit_message_text(text=(text1 + text2 + text3))

                            # update.callback_query.edit_message_text(text='Type /stop to restart bot and start Trading')

                            textp = text1 + text2 + text3
                            
                            vvery12 = telegram_id
                            bot_message = 'Telegram ID ' ''+ str(vvery12) +'' ' \n \n '
                            ' Name ' + first_name + ' ' + second_name + '\n \n'
                            'Sir Name ' ''+ second_name +'' ' \n \n '
                            ' *User has updated their API key and Secret* '  '\n \n'

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)
                
                            
                        
                            # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(telegram_id) + '&parse_mode=Markdown&text=' + bot_message
                            # response = requests.get(send_text)

                            # select_level(update, context)   
                            # text_if1  = text1 + text2 + text3
                            

                        if not (key1 in telegram_dict):

                            # db.session.query(Telegram).filter(Telegram.telegramid == telegram_id).delete()

                            # todo = Telegram.create(commit = True, inviter_id = 10000, verified = 'Yes', telegramid = telegram_id, api_key = key2, api_secret = key1, first_name = first_name)
                            with app.app_context():
                    
                                db.session.query(Telegram).filter(Telegram.telegramid == telegram_id).delete()

                                db.session.commit()

                                todo = Telegram.create(inviter_id = inviter_idt, verified = 'Yes', telegramid = telegram_id, api_key = key2, api_secret = key1, first_name = first_name, second_name = second_name)
                
                            print('Telegram Table Create Result')
                            print(todo)
                            print('__________________________________________________________')

                            text1 = 'Your data has been captured \n'

                            text2 = 'Your Bybit data has been Verified. You can proceed and start trading \n'
                                                        
                            text3 = 'Bybit ID is valid, you can proceed to manual trading via  this bot, or setup automated trading with TradingView \n'
                            
                            # update.callback_query.edit_message_text(text=(text1 + text2 + text3))

                            # update.callback_query.edit_message_text(text='Type /stop to restart bot and Verify your keys afresh')

                            textp = text1 + text2 + text3

                            bot_message = 'Telegram ID ' ''+ str(vvery12) +'' ' \n \n '
                            ' Name ' + first_name + ' ' + second_name + '\n \n'
                            'Sir Name ' ''+ second_name +'' ' \n \n '
                            ' *User has Captured and Validated their API key and Secret for the first time* '  '\n \n'

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)
                            

                            
                            
                    else:
                        text1 = ' Your Api data could not be authenticated for use by this bot.\n'

                        text2 = 'Visit http://bybit.cm to create a Bybit account and get API keys.\n'

                        bot_message = text1 + text2 
                        
                        textp = bot_message
            

            return textp  
            
def show_data(update: Update, context: CallbackContext) -> str:
    """Pretty print gathered data."""
    """Pretty print gathered data."""
    print("The execution is still on show data")
   
   
    bot_token = '1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8'
    user, telegram_id, first_name, second_name = getUserDetails(update, context)
    user_data = context.user_data
    bot_chatID = str(telegram_id)
   
    user_data = context.user_data
    
    print(user_data, "USER DATA")
    #text = 'Yourself:' + prettyprint(user_data, SELF)
    # print(' prettyprint(user_data, PARENTS)' ,prettyprint(user_data, PARENTS))
    print('PARENTS DATA')
    print(PARENTS)
    level = context.user_data[CURRENT_LEVEL]

    if level == SELF:
        textp = verifyApiData(update, context, level, user_data)

    else:
        textp = displayDefaultSettings(update, context, level, user_data)
    

    
    user_data.clear()
    user_data[START_OVER] = True
    print("------------CALLBACK 1---END START--------------", callback1)
    print("------------UPDATE 1- END START----------------", update1)
    buttons = [[InlineKeyboardButton(text='Back', callback_data=str(END))]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.answer()
    update.callback_query.edit_message_text(text=textp, reply_markup=keyboard)  
    return SHOWING
    

def get_api_data(update: Update, context: CallbackContext) -> None:
    """Pretty print gathered data."""

    key = ''
    secret = ''
    def prettyprint(user_data, level):
        people = user_data.get(level)
        if not people:
            return '\nNo information yet.'

        text = ''
        
        if level == SELF:
            for person in user_data[level]:
                text += f"\nName: {person.get(NAME, '-')}, Age: {person.get(AGE, '-')}"
        else:
            male, female, automated = _name_switcher(level)

            for person in user_data[level]:
                gender = female if person[GENDER] == FEMALE else male
                text += f"\n{gender}: Key: {person.get(NAME, '-')}, Secret: {person.get(AGE, '-')}"
                key =f"{person.get(NAME, '-')}"
                secret = f"{person.get(AGE, '-')}"

        return text, key, secret

    user_data = context.user_data
    #text = 'Yourself:' + prettyprint(user_data, SELF)
    text, key, secret, text_if1, text_if2, text_except = prettyprint(user_data, PARENTS)
    #text += '\n\nChildren:' + prettyprint(user_data, CHILDREN)


    update.message.reply_text('Okay, bye.')
    update.message.reply_text('Type, /start to restart bot.')
    # buttons = [[InlineKeyboardButton(text='Back', callback_data=str(END))]]
    # keyboard = InlineKeyboardMarkup(buttons)

    # update.callback_query.answer()
    # update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    context.user_data[START_OVER] = True

    return key, secret



def stop(update: Update, context: CallbackContext) -> None:
    """End Conversation by command."""
    update.message.reply_text('Okay, bye.')
    update.message.reply_text('Type, /start to restart bot.')
    
    context.user_data[START_OVER] = False
    return END


def end(update: Update, context: CallbackContext) -> None:
    """End conversation from InlineKeyboardButton."""
    update.callback_query.answer()

    text = 'See you around!'
    update.callback_query.edit_message_text(text=text)
    update.callback_query.edit_message_text(text = 'Type, /start to restart bot.')
    # update.message.reply_text('Type, /start to restart bot.')

    return END


# Second level conversation callbacks
def select_level(update: Update, context: CallbackContext) -> None:
    """Choose to add a parent or a child."""
    text = 'You can perform sell, buy operations or automated trades. To proceed select an option. Type /stop to restart bot'
    buttons = [
        # [
        #     InlineKeyboardButton(text= 'API DATA', callback_data=str(MALE)),
        # ],
        [
            InlineKeyboardButton(text='Trade BTC', callback_data=str(PARENTS)),
            InlineKeyboardButton(text='Trade ETH', callback_data=str(CHILDREN)),
        ],
        [
            InlineKeyboardButton(text='Trade EOS', callback_data=str(NEIGHBORS)),
            InlineKeyboardButton(text='Trade XRP', callback_data=str(FOREIGNERS)),
        ],
        
        [
            InlineKeyboardButton(text= 'Back', callback_data=str(END)),
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    update.callback_query.answer()
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return SELECTING_LEVEL


def select_gender(update: Update, context: CallbackContext) -> None:
    update1 = update
    callback1 = CallbackContext
    """Choose to add mother or father."""
    level = update.callback_query.data
    context.user_data[CURRENT_LEVEL] = level

    text = 'Please select a option to continue'

    if level == PARENTS or level == CHILDREN or level == SELF or level == NEIGHBORS or level == FOREIGNERS: 

        female, automated, settings = _name_switcher(level)

        buttons = [
            # [
            #     InlineKeyboardButton(text= male, callback_data=str(MALE)),
            # ],
            [
                InlineKeyboardButton(text= female, callback_data=str(FEMALE)),
                InlineKeyboardButton(text= automated, callback_data=str(AUTOMATED)),

            ],
            [
                InlineKeyboardButton(text= settings, callback_data=str(SETTINGS)),
                # InlineKeyboardButton(text= show_settings, callback_data=str(SHOW_SETTINGS)),
            ],
            [
                # InlineKeyboardButton(text='Show data', callback_data=str(SHOWING)),
                InlineKeyboardButton(text='Back', callback_data=str(END)),
            ],
        ]
        keyboard = InlineKeyboardMarkup(buttons)
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    
    return SELECTING_GENDER

def select_trade(update: Update, context: CallbackContext) -> None:
    """Choose to add mother or father."""
    level = update.callback_query.data
    context.user_data[CURRENT_LEVEL] = level

    text = 'Please choose, whom to add.'

    male, female, automated = _name_switcher(level)

    buttons = [
        [
            InlineKeyboardButton(text=male, callback_data=str(MALE)),
            InlineKeyboardButton(text=female, callback_data=str(FEMALE)),
            InlineKeyboardButton(text=automated, callback_data=str(AUTOMATED)),

        ],
        [
            # InlineKeyboardButton(text='Show data', callback_data=str(SHOWING)),
            InlineKeyboardButton(text='Back', callback_data=str(END)),
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    update.callback_query.answer()
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return SELECTING_TRADE

def end_second_level(update: Update, context: CallbackContext) -> None:
    """Return to top level conversation."""
    context.user_data[START_OVER] = True
    print('update1',update1)
    print('callback1', callback1)
    start(update, context)
    

    return END
 

# Third level callbacks
def select_feature1(update: Update, context: CallbackContext) -> None:

    update1 = update
    callback1 = CallbackContext

    """Select a feature to update for the person."""
    buttons = [
        [
            InlineKeyboardButton(text='Buy', callback_data=str(NAME)),
            InlineKeyboardButton(text='Sell', callback_data=str(AGE)),
            # InlineKeyboardButton(text='Buy ETH', callback_data=str(BUYETH)),
            # InlineKeyboardButton(text='Buy EOS', callback_data=str(BUYEOS)),
            # InlineKeyboardButton(text='Buy XRP', callback_data=str(BUYXRP)),
        ], 
        # [
        #     InlineKeyboardButton(text='Sell', callback_data=str(AGE)),
        #     # InlineKeyboardButton(text='Sell ETH', callback_data=str(SELLETH)),
        #     # InlineKeyboardButton(text='Sell EOS', callback_data=str(SELLEOS)),
        #     # InlineKeyboardButton(text='Sell XRP', callback_data=str(SELLXRP)),
        # ],
        [
            InlineKeyboardButton(text='Leverage', callback_data=str(LEVERAGE)),
            InlineKeyboardButton(text='Close', callback_data=str(CLOSE)),
        ],
        [
            InlineKeyboardButton(text='Position', callback_data=str(POSITION)),
            InlineKeyboardButton(text='Done', callback_data=str(END)),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we collect features for a new person, clear the cache and save the gender
    if not context.user_data.get(START_OVER):
        context.user_data[FEATURES] = {GENDER: update.callback_query.data}
        text = 'Please select a operation to perform.'

        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    # But after we do that, we need to send a new message
    else:
        text = 'Got it! Please select a operation to perform.'
        update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_FEATURE1

#automation 
def select_feature2(update: Update, context: CallbackContext) -> None:
    update1 = update
    callback1 = CallbackContext

    """Select a feature to update for the person."""
    buttons = [
        [
            InlineKeyboardButton(text='Webhook', callback_data=str(WEBHOOK)),
        ],
        [
            InlineKeyboardButton(text='Buy', callback_data=str(NAME)),
            InlineKeyboardButton(text='Sell', callback_data=str(AGE)),
            # InlineKeyboardButton(text='Buy ETH', callback_data=str(BUYETH)),
            # InlineKeyboardButton(text='Buy EOS', callback_data=str(BUYEOS)),
            # InlineKeyboardButton(text='Buy XRP', callback_data=str(BUYXRP)),
        ], 
        # [
        #     InlineKeyboardButton(text='Sell', callback_data=str(AGE)),
        #     # InlineKeyboardButton(text='Sell ETH', callback_data=str(SELLETH)),
        #     # InlineKeyboardButton(text='Sell EOS', callback_data=str(SELLEOS)),
        #     # InlineKeyboardButton(text='Sell XRP', callback_data=str(SELLXRP)),
        # ],
        [
            InlineKeyboardButton(text='Leverage', callback_data=str(LEVERAGE)),
            InlineKeyboardButton(text='Close', callback_data=str(CLOSE)),
        ],
        [
            InlineKeyboardButton(text='Position', callback_data=str(POSITION)),
            InlineKeyboardButton(text='Done', callback_data=str(END)),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we collect features for a new person, clear the cache and save the gender
    if not context.user_data.get(START_OVER):
        context.user_data[FEATURES] = {GENDER: update.callback_query.data}
        text = 'Please select a feature to update.'

        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    # But after we do that, we need to send a new message
    else:
        text = 'Got it! Please select a feature to update.'
        update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_FEATURE2

# Third level callbacks
def select_feature1(update: Update, context: CallbackContext) -> None:
    update1 = update
    callback1 = CallbackContext

    """Select a feature to update for the person."""
    buttons = [
        [
            InlineKeyboardButton(text='Buy', callback_data=str(NAME)),
            InlineKeyboardButton(text='Sell', callback_data=str(AGE)),
            # InlineKeyboardButton(text='Buy ETH', callback_data=str(BUYETH)),
            # InlineKeyboardButton(text='Buy EOS', callback_data=str(BUYEOS)),
            # InlineKeyboardButton(text='Buy XRP', callback_data=str(BUYXRP)),
        ], 
        # [
        #     InlineKeyboardButton(text='Sell', callback_data=str(AGE)),
        #     # InlineKeyboardButton(text='Sell ETH', callback_data=str(SELLETH)),
        #     # InlineKeyboardButton(text='Sell EOS', callback_data=str(SELLEOS)),
        #     # InlineKeyboardButton(text='Sell XRP', callback_data=str(SELLXRP)),
        # ], 
        [
            InlineKeyboardButton(text='Leverage', callback_data=str(LEVERAGE)),
            InlineKeyboardButton(text='Close', callback_data=str(CLOSE)),
        ],
        [
            InlineKeyboardButton(text='Position', callback_data=str(POSITION)),
            InlineKeyboardButton(text='Done', callback_data=str(END)),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we collect features for a new person, clear the cache and save the gender
    if not context.user_data.get(START_OVER):
        context.user_data[FEATURES] = {GENDER: update.callback_query.data}
        text = 'Please select a operation to perform.'

        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    # But after we do that, we need to send a new message
    else:
        text = 'Got it! Please select a operation to perform.'
        update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_FEATURE1

#automation 
def select_feature3(update: Update, context: CallbackContext) -> None:

    update1 = update
    callback1 = CallbackContext

    """Select a feature to update for the person."""
    buttons = [
        [
            InlineKeyboardButton(text='Amount', callback_data=str(AMOUNTSETTING)),
            InlineKeyboardButton(text='Take Profit', callback_data=str(TAKEPROFIT)),
        ],
        [
            InlineKeyboardButton(text='Stop Loss', callback_data=str(STOPLOSS)),
            InlineKeyboardButton(text='Trailing Stop', callback_data=str(TRAILINGSTOP)),
        ], 
        [
            InlineKeyboardButton(text='New Trailing Active', callback_data=str(NEWTRAILINGACTIVE)),
            InlineKeyboardButton(text='Leverage', callback_data=str(LEVERAGESETTING)),
        ],
        [
            InlineKeyboardButton(text='Done', callback_data=str(END)),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we collect features for a new person, clear the cache and save the gender
    if not context.user_data.get(START_OVER):
        context.user_data[FEATURES] = {GENDER: update.callback_query.data}
        text = 'Please select a feature to update.'

        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    # But after we do that, we need to send a new message
    else:
        text = 'Got it! Please select a feature to update.'
        update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_FEATURE3


# Third level callbacks
def select_feature(update: Update, context: CallbackContext) -> None:
    """Select a feature to update for the person."""
    update1 = update
    callback1 = CallbackContext

    buttons = [
        [
            InlineKeyboardButton(text='Api Key', callback_data=str(NAME)),
            InlineKeyboardButton(text='Api Secret', callback_data=str(AGE)),
            InlineKeyboardButton(text='Done', callback_data=str(END)),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we collect features for a new person, clear the cache and save the gender
    if not context.user_data.get(START_OVER):
        context.user_data[FEATURES] = {GENDER: update.callback_query.data}
        text = 'Please select a feature to update.'

        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    # But after we do that, we need to send a new message
    else:
        text = 'Got it! Please select a feature to update.'
        update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_FEATURE






def ask_for_input(update: Update, context: CallbackContext) -> None:
    update1 = update
    callback1 = CallbackContext
    """Prompt user to input data for selected feature."""
    context.user_data[CURRENT_FEATURE] = update.callback_query.data
    text = 'Okay, tell me.'

    update.callback_query.answer()
    update.callback_query.edit_message_text(text=text)

    return TYPING

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
            
            
            if position_result1[x]['data']['symbol'] == trade_symbol and  position_result1[x]['data']['side'] == user_trade_data['side']:
                
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
   

def checkTradedatadb(level):
    with app.app_context():
        vvery12 = telegram_id
        if level == PARENTS:
                 
            asset = 'BTCUSD'
            
            
        if level == CHILDREN:

            asset = 'ETHUSD' 

            
        if level == NEIGHBORS:
            asset = 'EOSUSD'
            
        if level == FOREIGNERS:
            asset = 'XRPUSD'
    
        try:
            trade_data = db.session.query(TradeDataDefaults.mtype, TradeDataDefaults.amount,TradeDataDefaults.takeprofit,TradeDataDefaults.stoploss,TradeDataDefaults.trailingstop, TradeDataDefaults.newtrailingactive,TradeDataDefaults.leverage).filter_by(telegramid=vvery12, asset=asset).all()

            datasa1 ={

                "type" :trade_data[0][0],
                "amount" :trade_data[0][1],
                "takeProfit" : trade_data[0][2], 
                "stopLoss" : trade_data[0][3], 
                "trailingStop" : trade_data[0][4],
                "new_trailing_active" : trade_data[0][5], 
                "Leverage" : trade_data[0][6],
                "TelegramID" : int(telegram_id)

                }
        except:
            datasa1 ={
            "type": 'Market',
            "amount": 'None', 
            "takeProfit" :'None', 
            "stopLoss" : 'None', 
            "trailingStop" : 'None',
            "new_trailing_active" : 'None', 
            "Leverage" : 'None',
            "TelegramID" : telegram_id  
            }       
    return datasa1

    print("\n\n\n\n\n\n\n^^^^^^^^^^^^^^^^^^^^^^^^^$#$@#$#$##$*********************************printing tradedata")
    print(trade_data)

def assetSymbolSplitter(trade_symbol):
    if 'BTC'  in trade_symbol:
        return 'BTC'
    if 'ETH' in trade_symbol:
        return 'ETH'
    if 'EOS' in trade_symbol:
        return 'EOS'
    if 'XRP' in trade_symbol:
        return 'XRP'

def orderProcessor(update: Update, context: CallbackContext,levelinput, user_data):
    user, telegram_id, first_name, second_name = getUserDetails(update, context)
    textp = "Invalid Selection"
    user_data_buy = {}
    user_data_sell = {}
    user_data_close = {}
    user_data_position = {}
    user_data_leverage = {}
    yes  = 'Yes'
    buttons = [[InlineKeyboardButton(text='Back', callback_data=str(END))]]
    keyboard = InlineKeyboardMarkup(buttons)

    level = context.user_data[CURRENT_LEVEL]
    # check if users time is ok before placing any order
    timestatus = CheckTimestamp()

    if level == levelinput:
        # AND INSIDE HERE, WE HAVE MANY OTHER OPTIONS LIKE Manual Trading, Automated Trading, Default Settings, Show Settings
        # and these will be repeated for variety of symbols. 
        # under this level for example there are SELECT[GENDER] which are options availed to process 
        # Manual Trading, Automated Trading, Default Settings, Show Settings
        # Manual Trading (FEMALE), Automated Trading(AUTOMATED), Default Settings(), Show Settings(SHOW_SETTINGS) 
        print('------------------------LEVEL PARENT-----------------------------------------------------------------')

        vvery12 = telegram_id

        # access the database

        with app.app_context():
            api_data = db.session.query(Telegram.api_key, Telegram.api_secret,Telegram.verified, Telegram.first_name,Telegram.second_name).filter(Telegram.telegramid==vvery12).all()

            #and thhis is API KEY AND SECRET of the Leder
        print("API data -----------", api_data)
        try:
            api_key = api_data[0][0]
            api_secret = api_data[0][1]
            res = api_data[0][2]
            first_name = api_data[0][3]
            second_name = api_data[0][4]
            if first_name == None:
                first_name = ''
            if second_name == None:
                second_name == ''
        except:
            api_key = ''
            api_secret = ''
            res = ''
            first_name = ''
            second_name = ''

        print('firstname', 'secondname')
        print(first_name, second_name)
        second_name = ''

        print("printing response", second_name)

        if context.user_data[CURRENT_FEATURE] == str(NAME): 
                #     # text = ''+'{"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","Leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            # Data to be written
            
            if level == PARENTS:
                passed_dictionary ={ 
                    "side" : 'Buy', 
                    "symbol" : 'BTCUSD', 
                    "TelegramID": str(telegram_id)
                } 
            if level == CHILDREN:
                passed_dictionary ={ 
                    "side" : 'Buy', 
                    "symbol" :'ETHUSD', 
                    "TelegramID": str(telegram_id)
                }
            if level == NEIGHBORS:
                passed_dictionary ={ 
                    "side" : 'Buy', 
                    "symbol" :'EOSUSD', 
                    "TelegramID": str(telegram_id)
                } 
            if level == FOREIGNERS:
                passed_dictionary ={ 
                    "side" : 'Buy', 
                    "symbol" :'XRPUSD', 
                    "TelegramID": str(telegram_id)
                } 
            datasa1 = {}
            datasaa = checkTradedatadb(level) 
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            print('Updated Data For Insertion', datasa1)
            text = datasa1   
            user_data_buy = text 
            # update to the user
            
            
            vvery12 = telegram_id
            # if buy in user_data: 
            
            if user_data_buy['amount'] !='None':
                if res == yes: 
                    update.callback_query.edit_message_text(text='Sending Buy Request to Bybit\n\n'+ str(user_data_buy))

                    print('Started working on Buy Operations')
                    print("User data buy", user_data_buy)
                    #update.message.reply_text('Manual Order sent: Buy' + float(placed_btc_value) + ' BTC contracts\n \n')
                    # update.callback_query.edit_message_text('Manual Buy Order sent to Bybit')
                    # user_data[START_OVER] = True
                    # update.callback_query.edit_message_text(text="done",reply_markup = keyboard)
                    #uids13 = user_data['Buy']
                    print('Buy',user_data_buy)
                    print('Started working on Buy Operations')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(user_data_buy)
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    user_data_buy = json.dumps(user_data_buy)
                    

                    buy_dump = json.loads(user_data_buy)
                    print('buy-------------------dump', buy_dump["symbol"])
                    #buy_dump['TelegramID'] = vvery12
                    print('Want to Check JSON on Buy',buy_dump)
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(buy_dump)
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

                    list_of_rows_access = [[]]
                    # read csv file as a list of lists
                    with open('access.csv', 'r') as read_obj:
                        # pass the file object to reader() to get the reader object
                        csv_reader = reader(read_obj)
                        # Pass reader object to list() to get a list of lists
                        list_of_rows_access = list(csv_reader)
                        print('list_of_rows_access', list_of_rows_access)
                    toListAccess = []
                    for i in range(len(list_of_rows_access)):
                        rt = str(list_of_rows_access[i])[1:]
                        tr = rt[1:]
                        re = tr[:-1]
                        rew = re[:-1]
                        toListAccess.append(rew)
                        # print('toListAccess', toListAccess, 'passed token', buy_dump['token'])
                    # if buy_dump['token'] in toListAccess: 
                    print('User Can access the Bot. Token Valid')
                    ret_msg = ''
                    error_reta = ''
                    placed_btc_value = ''
                    created_at = ''
                    final_entry_price = ''
                    
                    has_positions, textresponse = checkPositionExists(buy_dump)

                    print("\n\n\n\n\n******************++++++++++++++++++++++", has_positions, textresponse)
                    if has_positions ==True:
                        textp = textresponse
                    else:
                        # ret_msg, error_reta,  placed_btc_value, created_at, final_entry_price = send_order(buy_dump)
                        ret_msg, error_reta,  placed_btc_value, created_at, final_entry_price = send_order_v2(buy_dump)
                        print('return value after sending_order request')
                                 
                        print('ret_msg')
                        print(ret_msg)
                        print('error_reta')
                        print(error_reta)
                        print('placed_btc_value')
                        print(placed_btc_value)
                        print('created_at')
                        print(created_at)
                        print('final_entry_price')
                        print(final_entry_price)
                        print('Buy Done')
                        print('first name', first_name)
                        print("second name",second_name)
                        try:
                            placedbtcvalue = "%.6f"%float(placed_btc_value)
                        except:
                            placedbtcvalue = " "
                        trade_asset = assetSymbolSplitter(buy_dump['symbol'])
                        if ret_msg == 'OK' or ret_msg == 'ok':
                           
                            
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: buy* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''



                           
                            textp = bot_message3 + bot_message4 + bot_message5

                            

                        if error_reta.startswith('TrailingStop:') or ret_msg.startswith('TrailingStop:'):
                            print(float(placed_btc_value))
                          
            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: buy* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''

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
                            bot_message3 = '*Manual Order Received: buy* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: StopLoss is invalid"


                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                        if error_reta.startswith('params trailing_stop invalid') or ret_msg.startswith('params trailing_stop invalid'):
                            
                            
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: buy* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: TrailingStop is invalid"


                            
                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6
                        
                        if error_reta.startswith('params take_profit invalid') or ret_msg.startswith('params take_profit invalid'):
                           
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: buy* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: TakeProfit is invalid"


                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                        



                        # buy_dump.clear()
                    if error_reta.startswith('params new_trailing_active invalid') or ret_msg.startswith('params new_trailing_active invalid'):
                           
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: buy* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: newTrailingStop is invalid"


                            

                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 
                    if error_reta.startswith('params invalid') or ret_msg.startswith('params invalid'):
                           
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: buy* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
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
                        # buy_dump.clear()


                

                else : 
                    # update1.message.reply_text(
                    # 'You must have valid Bybit API key and Secret \n \n')          
            
                    bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                    bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                    bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                    bot_message3 = 'Buy not possible. User has no valid API Key and Secret' '\n '' '
                    
                    errer_response = bot_message + bot_message1 + bot_message2 + bot_message3 
                    messages_store = {
                    'side':'buy',
                    'ret_msg':'',
                    'error_reta':'',
                    'placed_btc_value':'',
                    'created_at':'',
                    'final_entry_price':'',
                    'error_response': errer_response
                    }

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    botu_message = 'You must have valid Bybit API key and Secret \n \n'
                    textp = botu_message
                    # buy_dump.clear()
                    
            else:
                textp = "Trade amount cannot be None\n Check your {0} default setting and try again".format(user_data_buy['symbol'])
        if context.user_data[CURRENT_FEATURE] == str(AGE):
            

            datasa1 = checkTradedatadb(level)
            if level == PARENTS:
                passed_dictionary ={ 
                    "side" :'Sell', 
                    "symbol" : 'BTCUSD', 
                    "TelegramID": str(telegram_id)
                } 
            if level == CHILDREN:
                passed_dictionary ={ 
                    "side" : 'Sell', 
                    "symbol" :'ETHUSD', 
                    "TelegramID": str(telegram_id)
                }
            if level == NEIGHBORS:
                passed_dictionary ={ 
                    "side" : 'Sell', 
                    "symbol" :'EOSUSD', 
                    "TelegramID": str(telegram_id)
                } 
            if level == FOREIGNERS:
                passed_dictionary ={ 
                    "side" : 'Sell', 
                    "symbol" :'XRPUSD', 
                    "TelegramID": str(telegram_id)
                }    
           
            datasa1 = {}
            datasaa = checkTradedatadb(level) 
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            print('Updated Data For Insertion', datasa1)
            
            user_data_sell = datasa1

           
            # user_data_sell = json.dumps(user_data_sell)
            vvery12 = telegram_id
            if user_data_sell['amount'] != 'None': 
                user_data_sell = json.dumps(user_data_sell)
                update.callback_query.edit_message_text(text='Sending Sell Request to Bybit\n\n'+ str(user_data_sell))

                if yes == res: 
                    print('Started working on Sell Operations')
                    print('Sell data',user_data_sell)
                    # update1.message.reply_text('Manual Sell order sent to  Bybit')
                    botu_message = 'Manual Sell order sent to  Bybit'
                    #uids13 = user_data_sell['Sell']
                
                    print('Sell data',user_data_sell)
                    buy_dump = json.loads(user_data_sell)
                    print('Sell--------------dump', buy_dump["symbol"])
                    #buy_dump['TelegramID'] = vvery123
                    print('Want to Check JSON on Sell',buy_dump)
                    list_of_rows_access = [[]]
                    # read csv file as a list of lists
                    with open('access.csv', 'r') as read_obj:
                        # pass the file object to reader() to get the reader object
                        csv_reader = reader(read_obj)
                        # Pass reader object to list() to get a list of lists
                        list_of_rows_access = list(csv_reader)
                        print('list_of_rows_access', list_of_rows_access)
                    toListAccess = []
                    for i in range(len(list_of_rows_access)):
                        rt = str(list_of_rows_access[i])[1:]
                        tr = rt[1:]
                        re = tr[:-1]
                        rew = re[:-1]
                        toListAccess.append(rew)
                        # print('toListAccess', toListAccess, 'passed token', buy_dump['token'])
                    # if buy_dump['token'] in toListAccess:
                    has_positions,textresponse = checkPositionExists(buy_dump)
                    if has_positions == True:
                        textp =textresponse
                    else:
                        ret_msg, error_reta,  placed_btc_value, created_at, final_entry_price = send_order_v2(buy_dump)
                        
                        
                        #price_data = send_order(buy_dump)
                       
                        print('ret_msg')
                        print(ret_msg)
                        print('error_reta')
                        print(error_reta)
                        print('placed_btc_value')
                        print(placed_btc_value)
                        print('created_at')
                        print(created_at)
                        print('final_entry_price')
                        print(final_entry_price)
                        print('Buy Done')
                        print('first name', first_name)
                        print("second name",second_name)
                        try:
                            placedbtcvalue = "%.6f"%float(placed_btc_value)
                        except:
                            placedbtcvalue = " "

                        trade_asset = assetSymbolSplitter(buy_dump['symbol'])
                        
                        # update1.message.reply_text(error_reta)
                        if ret_msg == 'OK' or ret_msg == 'ok':

                           

                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: sell* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' '+str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''

                            
                            textp = bot_message3 + bot_message4 + bot_message5
                            
                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            
                            print('textp', textp)
                            

                        if error_reta.startswith('TrailingStop:') or ret_msg.startswith('TrailingStop:'):
                            
            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: sell* ' + str(round(float(placed_btc_value), 5)) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(round(float(placed_btc_value), 5)) +' '+ str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            textp = botu_message + bot_message3 + bot_message4 + bot_message5

                        if ret_msg == 'empty price':
                            

                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = 'Your sell Order Not successful' '\n '' '
                            bot_message4 = 'You have no funds in your Bybit Account ' ' \n ' 
                            bot_message5 = 'Top up to continue using the Bot'

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            textp = botu_message + bot_message3 + bot_message4 + bot_message5
                            
                        if error_reta.startswith('error sign!'):
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = 'Your sell Order Not successful' '\n '' '
                            bot_message4 = 'You have no funds in your Bybit Account ' ' \n \n ' 
                            bot_message5 = 'Top up to continue using the Bot'

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            textp =botu_message +  bot_message3 + bot_message4 + bot_message5

                            # Param validation for 
                        
                        if error_reta.startswith('Param validation') or ret_msg.startswith('Param validation'):
                            

                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = 'Your sell Order Not successful' '\n '' '
                            bot_message4 = 'You have no funds in your Bybit Account ' ' \n \n ' 
                            bot_message5 = 'Top up to continue using the Bot'

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3 +bot_message4 + bot_message5
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            textp =botu_message + bot_message3 + bot_message4 + bot_message5
                        if error_reta.startswith('incorrect'):
                            print("Hello---------------")
                            textp = "something is wrong\n Check default settings and try again."
                            # buy_dump.clear()
                        if error_reta.startswith('params stop_loss invalid') or ret_msg.startswith('params stop_loss invalid'):
                
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: sell* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: StopLoss is invalid"


                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                        if error_reta.startswith('params trailing_stop invalid') or ret_msg.startswith('params trailing_stop invalid'):
                           
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: sell* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: TrailingStop is invalid"


                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6
                        
                        if error_reta.startswith('params take_profit invalid') or ret_msg.startswith('params take_profit invalid'):
                           
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: sell* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: TakeProfit is invalid"

                           
                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                        



                    if error_reta.startswith('params new_trailing_active invalid') or ret_msg.startswith('params new_trailing_active invalid'):
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: sell* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
                            bot_message6 = "\n Conditional parameters not activated: newTrailingStop is invalid"


                            textp = bot_message3 + bot_message4 + bot_message5 + bot_message6 

                    if error_reta.startswith('params invalid') or ret_msg.startswith('params invalid'):
                           
                            
                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = '*Manual Order Received: sell* ' + str(placedbtcvalue) + ' ' + buy_dump['symbol'] + ' \n '' '
                            bot_message4 = '*Filled entry*' ''+ str(created_at) +'\n '' '
                            bot_message5 = '' + str(placedbtcvalue) +' ' + str(trade_asset) + '@ $'+str(round(float(final_entry_price), 5))+''
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

                

                else : 
                    

                    bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                    bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                    bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                    bot_message3 = 'User doesn\'t have valid Bybit API key and Secret \n'
                    error_response = bot_message + bot_message1 + bot_message2 +bot_message3 
                    messages_store = {
                    'side':'sell',
                    'ret_msg':'',
                    'error_reta':'',
                    'placed_btc_value':'',
                    'created_at':'',
                    'final_entry_price':'',
                    'error_response': ''
                    }

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    textp = 'You must have valid Bybit API key and Secret \n \n'

                    
        
            else:
                 
                textp = "Trade amount cannot be None\n Check your {0} default setting and try again".format(user_data_sell['symbol'])
        

        if context.user_data[CURRENT_FEATURE] == str(LEVERAGE):
            datasa1 = checkTradedatadb(level)

            if level == PARENTS:
                text = '{"symbol": "BTCUSD", "Leverage": "'+datasa1['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'
            if level == CHILDREN:
                text = '{"symbol": "ETHUSD", "Leverage": "'+datasa1['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'
            if level == NEIGHBORS:
                text = '{"symbol": "EOSUSD", "Leverage": "'+datasa1['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'
            if level == FOREIGNERS:
                text = '{"symbol": "XRPUSD", "Leverage": "'+datasa1['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'

            user_data_leverage = text
            update.callback_query.edit_message_text(text='Sending Change Leverage Request to Bybit\n\n'+ str(user_data_leverage))
            vvery12 = telegram_id
            
            # if leverage in user_data_leverage: 
            if user_data_leverage != 'None': 
                
                if yes == res: 
                    print('Started working on Leverage Operations')
                    botu_message = 'Leverage Change Requested'
                    #update.message.reply_text('Manual Order sent: Sell' + float(placed_btc_value) + ' BTC contracts\n \n')
                    #uids13 = user_data['Leverage']
                    print('Leverage data',user_data_leverage)
                    
                    
                    try:
                        buy_dump = json.loads(user_data_leverage)
                        print('Leverage--------------dump', buy_dump["Leverage"])
                        #buy_dump['TelegramID'] = vvery123
                        print('Want to Check JSON on Leverage',buy_dump)
                        current_manual_leverage, adjusted_manual_leverage, manual_leverage= set_manual_leverage(buy_dump)
                        print('Leverage Send')
                        print(manual_leverage)
                        print("Printing the manual leverage data")
                        
                        
                        if manual_leverage =='OK':
                            
                            bot_message1 = ' Previous Leverage Data' + str(current_manual_leverage) + ' \n \n'
                            bot_message2 = ' Leverage Updated Successfully \n \n'
                            bot_message3 = ' Updated Leverage Data ' + str(adjusted_manual_leverage) + ' \n \n'
                            textp = bot_message1 + bot_message2 + bot_message3
                            # update1.message.reply_text('Leverage set successfully')

                            bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                            bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                            bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                            bot_message3 = 'User Updated their Leverage' '\n '' '

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                            #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                            response = requests.get(send_text)

                            
                            buy_dump.clear()
                            
                            
                            
                        
                            
                            
                        else: 
                            textp = 'Leverage not modified\nYou cannot set leverage which is same as the old leverage'
                    except:
                        textp = "The Leverage request data is invalid\n Check your default setting and try again"  
                            
                    
                else : 
                   
                    
                    bot_message = '*Telegram ID* : ' ''+ str(vvery12) +'' ' \n ''  '
                    bot_message1 = '*Name* : ' + first_name + ' ' + second_name + ' \n '' '
                    bot_message2 = '*Sir Name* : ' ''+ second_name +' \n '' '
                    bot_message3 = 'User tried set leverage but doesn\'t have valid Bybit API Key and Secret'

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 +bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    textp = 'You must have valid Bybit API key and Secret \n \n'

                

        if context.user_data[CURRENT_FEATURE] == str(CLOSE):
            if level == PARENTS:
                text = '{"symbol": "BTCUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'
            if level == CHILDREN:
                text = '{"symbol": "ETHUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'
            if level == NEIGHBORS:
                text = '{"symbol": "EOSUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'
            if level == FOREIGNERS:
                text = '{"symbol": "XRPUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'
            
            user_data_close = text
            
            update.callback_query.edit_message_text(text='Sending Close Request to Bybit\n\n' + str(user_data_close))

            vvery1235 = telegram_id
            uids19  = 'None'
            if user_data_close != 'None':
                if yes == res: 
                    #uids19 = user_data_close['Close']
                    print('Close String',user_data_close)
                    print('Started working on Close Operations')
                    try:
                        close_dump = json.loads(user_data_close)
                        close_dump['TelegramID'] = vvery1235
                        print('Want to Check JSON on Buy',close_dump)
                        price_data = parse__price_webhook(close_dump)
                        print('Close Operations Done')
                        # update1.message.reply_text('Order Closed')
                        botu_message = 'Order Closed'

                        bot_message = 'Telegram ID ' ''+ str(vvery12) +'' ' \n \n '
                        bot_message1 = ' Name ' + first_name + ' ' + second_name + '\n \n'
                        bot_message2 = 'Sir Name ' ''+ second_name +'' ' \n \n '
                        bot_message3 = ' *User has Closed their Orders and Posistions* '  '\n \n'

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 + bot_message3
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)

                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 + bot_message3
                        #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                        response = requests.get(send_text)
                        textp = botu_message
                        close_dump.clear()
                    except:
                        textp = "The request data is invalid\n Check your default settings and try again..."
                    
                    
                    
                else : 
                    

                    bot_message = 'Telegram ID ' ''+ str(vvery12) +'' ' \n \n '
                    bot_message1 = ' Name ' + first_name + ' ' + second_name + '\n \n'
                    bot_message2 = 'Sir Name ' ''+ second_name +'' ' \n \n '
                    bot_message3 = ' *User has failed to validate their Bybit API key and Secret* '  '\n \n'

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 + bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 + bot_message3
                    #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                    response = requests.get(send_text)

                    textp = 'You must have valid Bybit API key and Secret \n \n'
                    # close_dump.clear()
        if context.user_data[CURRENT_FEATURE] == str(POSITION):
            if level == PARENTS:
                text = ''+'{"symbol": "BTCUSD", "Position" : "Position", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            if level == CHILDREN:
                text = ''+'{"symbol": "ETHUSD", "Position" : "Position", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            if level == NEIGHBORS:
                text = ''+'{"symbol": "EOSUSD", "Position" : "Position", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            if level == FOREIGNERS:
                text = ''+'{"symbol": "XRPUSD", "Position" : "Position", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            
            user_data_position = text
            update.callback_query.edit_message_text(text='Sending Check Position Request to Bybit\n\n' + str(user_data_position))
            vvery1235 = telegram_id
            uids19  = 'None'
            print('user data position---------', user_data_position)
            # if  position in user_data_position: 
            if user_data_position != 'None':
                
                print('vvery vvery',vvery1235)
                Binance_ids = ''
                try:
                    udp = json.loads(user_data_position)
                    print("Trade symbol...................", udp['symbol'])
                    trade_symbol = udp['symbol']

                    if yes == res: 
                        trade_symbol = udp['symbol']

                        print('printing the trade symbol', trade_symbol)
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
                            if position_result1 is None : 
                                # update1.message.reply_text('You have no  open position')
                                bot_message1 = 'You have no  open position'
                                textp = botu_message + bot_message1
                            else: 
                                print(len(position_result1))
                                for x in range(len(position_result1)):
                                
                                    walletbalance = "%.6f"%float(position_result1[x]['data']['wallet_balance'])

                                    if position_result1[x]['data']['symbol'] == trade_symbol:
                                        botu_message1=(
                                            'Market: ' +position_result1[x]['data']['symbol']+' |'+'Size'+': '+str(position_result1[x]['data']['size'])+' |'+'Side'+': '+position_result1[x]['data']['side']+' |'+'Entry price'+': '+str(round(float(position_result1[x]['data']['entry_price']), 5))+'\n \n'
                                            ' |'+'Leverage: '+str(position_result1[x]['data']['leverage'])+' |'+'Wallet Balance: '+str(walletbalance) +'\n \n'
                                            ' |'+'Take Profit: '+str(position_result1[x]['data']['take_profit'])+' |'+'Stop Loss: '+str(round(float(position_result1[x]['data']['stop_loss']), 5))+' '+' |'+'Trailing Stop: '+str(round(float(position_result1[x]['data']['trailing_stop']), 5))+' '+'')
                                
                                bot_message = 'Telegram ID ' ''+ str(vvery12) +'' ' \n \n '
                                bot_message1 = ' Name ' + first_name + ' ' + second_name + '\n \n'
                                bot_message2 = 'Sir Name ' ''+ second_name +'' ' \n \n '
                                bot_message3 = ' *User has queried their Bybit Positions* '  '\n \n'

                                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '1093054762' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 + bot_message3
                                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                                response = requests.get(send_text)

                                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + '146943702' + '&parse_mode=Markdown&text=' + bot_message + bot_message1 + bot_message2 + bot_message3
                                #https://api.telegram.org/botAAEXuaj6a029wmrNBnOCSFpPadIWga7KOBk/sendMessage?chat_id=1093054762&parse_mode=Markdown&text=atomatedtradingview
                                response = requests.get(send_text)

                                textp = botu_message + botu_message1
                        except:
                            textp = "There was an error fetching your positions from Bybit\n Verify your Api key and secret and try again" 
                    
                    else:  
                       
                        textp = 'You must have valid Bybit API key and Secret \n \n'
                        '\n \n '.format(text.lower())
                except:
                    textp = "Error in checking position\n Make sure the data in default setting is in correct format."
   
    
    # update.callback_query
    buttons = [[InlineKeyboardButton(text='Back', callback_data=str(ENDMANUAL))]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.answer()
    update.callback_query.edit_message_text(text=textp, reply_markup=keyboard)


    return SHOWING

# check if the bot user has the correct time stamp
def CheckTimestamp():
    
    vvery12 = telegram_id

    # access the database

    with app.app_context():
        api_data = db.session.query(Telegram.api_key, Telegram.api_secret,Telegram.verified, Telegram.first_name,Telegram.second_name).filter(Telegram.telegramid==vvery12).all()

        #and thhis is API KEY AND SECRET of the Leder
    print("API data -----------", api_data)
    try:
        api_key = api_data[0][0]
        api_secret = api_data[0][1]
        res = api_data[0][2]
        first_name = api_data[0][3]
        second_name = api_data[0][4]
        if first_name == None:
            first_name = ''
        if second_name == None:
            second_name == ''
    except:
        api_key = ''
        api_secret = ''
        res = ''
        first_name = ''
        second_name = ''

    bybit1 = Bybit(api_key=api_key,
                    secret=api_secret, symbol="BTCUSD", ws=True, test=False)
    print("bybit1", bybit1)
    
    api_data = bybit1.get_api_data()
    print('api_data', api_data)
    inviter_id = api_data['result']
    print('inviter_id',inviter_id)
    if api_data['ret_msg'].startswith('invalid request') and api_data['ret_code'] == 10002:
        return False
    else:
        return True

def ask_for_input1(update: Update, context: CallbackContext) -> None:
    """
    features 
    NAME ----- Buy
    AGE  ----- Sell
    LEVERAGE
    POSITION
    CLOSE
    """
    update1 = update
    callback1 = CallbackContext
    """Prompt user to input data for selected feature."""

    context.user_data[CURRENT_FEATURE] = update.callback_query.data
    user_data = context.user_data
    
    level = context.user_data[CURRENT_LEVEL]
        
    text = 'No Creteria Met'

    
    #intialize variables

    # calling the order processing function
    orderProcessor(update, context,level, user_data)
    
    
  

# Process Futures data
def ask_for_input2(update: Update, context: CallbackContext) -> None:

    user, telegram_id, first_name, second_name = getUserDetails(update, context)
    
    update1 = update
    callback1 = CallbackContext
    textp = "Invalid selection."
    """Prompt user to input data for selected feature."""

    bot_token = '1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8'
    
    bot_chatID = str(telegram_id)
    #text = 'Null'
    context.user_data[CURRENT_FEATURE] = update.callback_query.data
    
    level = context.user_data[CURRENT_LEVEL]

    # datasa1 = {}
    datasaa = checkTradedatadb(level)

    print('Data Read From SETITNGS File', datasaa)


     
    

    
    if context.user_data[CURRENT_FEATURE] == str(WEBHOOK):
        text3 = 'Login to your https://www.tradingview.com/ account, create an alert and paste the link below under Webhook URL checkbox option\n \n'
        text4  =  ' To open a trade (Buy / Sell) https://profitsniperrapidfire.com/webhook'+' \n \n'
        text5 = ' To close any trade https://profitsniperrapidfire.com/close'+'\n \n'
        text = text3 + text4 + text5

        textp = text3 + text4 + text5
        # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(telegram_id) + '&parse_mode=Markdown&text=' + textp
        # response = requests.get(send_text)

    if context.user_data[CURRENT_FEATURE] == str(POSITION):
        text = 'Check your position on the manual trading button \n \n'

       
        textp = 'Check your position on the manual trading button \n \n'

     
    if level == PARENTS:

        if context.user_data[CURRENT_FEATURE] == str(NAME):
            # text = ''+'{"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","Leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            # Data to be written 
            passed_dictionary ={ 
                "side" : "Buy", 
                "symbol" : "BTCUSD", 
                
            } 

            datasa1 = {}
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)
            print('Updated Data For Insertion', datasa1)
            # text = datasa1
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)

            textp =  text3 + text4 + str(datasa1)

        if context.user_data[CURRENT_FEATURE] == str(AGE):
            passed_dictionary ={ 
                "side" : "Sell", 
                "symbol" : "BTCUSD", 
                
            } 

           
            datasa1 = {}
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)
            print('Updated Data For Insertion', datasa1)
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)
            
            textp =  text3 + text4 + str(datasa1)
        if context.user_data[CURRENT_FEATURE] == str(LEVERAGE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/leverage on the webhook section and paste a message similar to this one below on the message section \n \n'     
            text5 = ''+'{"option":"spot", "symbol" : "BTCUSD", "Leverage": "'+datasaa['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text =  text3 + text4 + text5

        
            textp =  text3 + text4 + text5

        if context.user_data[CURRENT_FEATURE] == str(CLOSE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/close on the webhook section and paste a message similar to this one below on the message section \n \n'
            text5 = ''+'{"option":"spot", "symbol" : "BTCUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text = text3 + text4 + text5

            textp = text3 + text4 + text5
    
    if level == CHILDREN:
        if context.user_data[CURRENT_FEATURE] == str(NAME):
            # text = ''+'{"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","Leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            # Data to be written 
            passed_dictionary ={ 
                "side" : "Buy", 
                "symbol" : "ETHUSD"
                
            } 

            datasa1 = {}
           
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)
            print('Updated Data For Insertion', datasa1)
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)

            
            textp =  text3 + text4 + str(datasa1)

        if context.user_data[CURRENT_FEATURE] == str(AGE):
            passed_dictionary ={ 
                "side" : "Sell", 
                "symbol" : "ETHUSD"
                
            } 

            datasa1 = {}
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)

            print('Updated Data For Insertion', datasa1)
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)

        
            textp =  text3 + text4 + str(datasa1)
        if context.user_data[CURRENT_FEATURE] == str(LEVERAGE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/leverage on the webhook section and paste a message similar to this one below on the message section \n \n'     
            text5 = ''+'{"option":"spot", "symbol" : "ETHUSD", "Leverage": "'+datasaa['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text =  text3 + text4 + text5

        
            textp =  text3 + text4 + text5

        if context.user_data[CURRENT_FEATURE] == str(CLOSE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/close on the webhook section and paste a message similar to this one below on the message section \n \n'
            text5 = ''+'{"option":"spot", "symbol" : "ETHUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text = text3 + text4 + text5

            textp = text3 + text4 + text5

    if level == NEIGHBORS:
        if context.user_data[CURRENT_FEATURE] == str(NAME):
            # text = ''+'{"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","Leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            # Data to be written 
            passed_dictionary ={ 
                "side" : "Buy", 
                "symbol" :"EOSUSD"
                
            } 

            datasa1 = {}
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)

           
            print('Updated Data For Insertion', datasa1)
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)

        
            textp =  text3 + text4 + str(datasa1)

        if context.user_data[CURRENT_FEATURE] == str(AGE):
            passed_dictionary ={ 
                "side" : "Sell", 
                "symbol" : "EOSUSD"
                
            } 

            datasa1 = {}
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)

            print('Updated Data For Insertion', datasa1)
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)


            textp =  text3 + text4 + str(datasa1)

        if context.user_data[CURRENT_FEATURE] == str(LEVERAGE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/leverage on the webhook section and paste a message similar to this one below on the message section \n \n'     
            text5 = ''+'{"option":"spot", "symbol" : "EOSUSD", "Leverage": "'+datasaa['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text =  text3 + text4 + text5

        
            textp =  text3 + text4 + text5

        if context.user_data[CURRENT_FEATURE] == str(CLOSE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/close on the webhook section and paste a message similar to this one below on the message section \n \n'
            text5 = ''+'{"option":"spot", "symbol" : "EOSUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text = text3 + text4 + text5

            textp = text3 + text4 + text5
    if level == FOREIGNERS:
        if context.user_data[CURRENT_FEATURE] == str(NAME):
            # text = ''+'{"type": "Market", "side": "Buy", "amount": "97", "symbol": "BTCUSD","Leverage":"10", "takeProfit" : "None","stopLoss":"None","trailingStop":"None", "new_trailing_active":"None", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            # Data to be written 
            passed_dictionary ={ 
                "side" : "Buy", 
                "symbol" : "XRPUSD"
                
            } 

            datasa1 = {}
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)

            print('Updated Data For Insertion', datasa1)
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)

        
            textp =  text3 + text4 + str(datasa1)

        if context.user_data[CURRENT_FEATURE] == str(AGE):
            passed_dictionary ={ 
                "side" : "Sell", 
                "symbol" : "XRPUSD"
                
            } 

            datasa1 = {}
            datasa1 = {}
            datasa1.update(passed_dictionary)
            datasa1.update(datasaa)
            datasa1 = json.dumps(datasa1)

            print('Updated Data For Insertion', datasa1)
            text3  = 'While Logged into TradingView, Paste the message similar to the one below on the Message TextArea \n \n'
            text4 = 'You can edit the parameters as you may wish, e.g. change amount percentage, leverage, takeProfit value, etc.\n \n'
            text =  text3 + text4 + str(datasa1)


            textp =  text3 + text4 + str(datasa1)

        if context.user_data[CURRENT_FEATURE] == str(LEVERAGE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/leverage on the webhook section and paste a message similar to this one below on the message section \n \n'     
            text5 = ''+'{"option":"spot", "symbol" : "XRPUSD", "Leverage": "'+datasaa['Leverage']+'", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text =  text3 + text4 + text5

        
            textp =  text3 + text4 + text5

        if context.user_data[CURRENT_FEATURE] == str(CLOSE):
            text3 = 'You need set an automated process. Open your http://www.tradingview.com/ account, create an alert \n \n'
            text4 = 'Add https://profitsniperrapidfire.com/close  on the webhook section and paste a message similar to this one below on the message section \n \n'
            text5 = ''+'{"option":"spot", "symbol" : "XRPUSD", "Close" : "Close", "token":"None", "TelegramID":"'+str(telegram_id)+'"}'+'\n \n'
            text = text3 + text4 + text5

            textp = text3 + text4 + text5

    

    print('context.user_data[CURRENT_FEATURE] ', update)
    
    buttons = [[InlineKeyboardButton(text='Back', callback_data=str(ENDMANUAL))]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=textp, reply_markup=keyboard)
  
    return SHOWING
   
# Process Trade Settings Data data
def ask_for_input3(update: Update, context: CallbackContext) -> None:
    text='please select a feature to update'
    update1 = update
    callback1 = CallbackContext

    context.user_data[CURRENT_FEATURE] = update.callback_query.data
    if context.user_data[CURRENT_FEATURE] == str(TAKEPROFIT):
        text = 'Enter your Take Profit Data. A number between zero(0) and 100. It will be passed as a percentage'
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text)

    if context.user_data[CURRENT_FEATURE] == str(STOPLOSS) :
        text = 'Enter your Stop Loss Data. A number between zero(0) and 100. It will be passed as a percentage'
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text)

    if context.user_data[CURRENT_FEATURE] == str(AMOUNTSETTING) :
        text = 'Enter your Amount Data. A number between zero(0) and 100. It will be passed as a percentage of your asset balance'
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text)
    if context.user_data[CURRENT_FEATURE] == str(TRAILINGSTOP):
        text = 'Enter your Trailing Stop Data. A number between zero(0) and 100. It will be passed as a percentage'
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text)

    if context.user_data[CURRENT_FEATURE] == str(NEWTRAILINGACTIVE):
        text = 'Enter your New Trailing Active Data. A number between zero(0) and 100. It will be passed as a percentage'
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text)
    if context.user_data[CURRENT_FEATURE] == str(LEVERAGESETTING):
        text = 'Enter your Leverage Data a number between zero(0) and 100. It will be passed as a percentage'
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text)
    print('|||||||||||||||||||||||||||||||||||||')

    print('context.user_data[CURRENT_FEATURE] ', update1)

    # update1.message.reply_text(text=text)

    
   
    return TYPING3


def save_input(update: Update, context: CallbackContext) -> None:
    """Save input for feature and return to feature selection."""
    user_data = context.user_data
    user_data[FEATURES][user_data[CURRENT_FEATURE]] = update.message.text

    user_data[START_OVER] = True

    return select_feature(update, context)


def save_input1(update: Update, context: CallbackContext) -> None:
    """Save input for feature and return to feature selection."""
    user_data = context.user_data
    user_data[FEATURES][user_data[CURRENT_FEATURE]] = update.message.text

    user_data[START_OVER] = True

    return select_feature1(update, context)

def save_input2(update: Update, context: CallbackContext) -> None:
    update.message.text = 'Data'
    """Save input for feature and return to feature selection."""
    user_data = context.user_data
    print('save input 2 user_data ', update.message.text)
    #user_data[FEATURES][user_data[CURRENT_FEATURE]] = update.message.text
    user_data[FEATURES][user_data[CURRENT_FEATURE]] = update.message.text
    user_data[START_OVER] = True

    return select_feature2(update, context)

def save_input3(update: Update, context: CallbackContext) -> None:
    """Save input for feature and return to feature selection."""
    user_data = context.user_data
    user_data[FEATURES][user_data[CURRENT_FEATURE]] = update.message.text

    user_data[START_OVER] = True

    return select_feature3(update, context)

def end_describing_manual(update: Update, context: CallbackContext) -> None:
    """End gathering of features and return to parent conversation."""
    user_data = context.user_data
    level = user_data[CURRENT_LEVEL]
    if not user_data.get(level):
        user_data[level] = []
    user_data[level].append(user_data[FEATURES])

    # Print upper level menu
    if level == SELF:
        user_data[START_OVER] = True

        start(update, context)
    else:
        select_level(update, context)

    return END

def end_describing(update: Update, context: CallbackContext) -> None:
    """End gathering of features and return to parent conversation."""
    user_data = context.user_data
    level = user_data[CURRENT_LEVEL]
    if not user_data.get(level):
        user_data[level] = []
    user_data[level].append(user_data[FEATURES])
    if level == 'SELF':
        pass
       
    else:
        # select_level(update, context)
        show_data(update, context)
        
    return END

def stop_nested(update: Update, context: CallbackContext) -> None:
    """Completely end conversation from within nested conversation."""
    user_data = context.user_data
    update.message.reply_text('Okay, bye.')
    update.message.reply_text('Type, /start to restart bot.')
    user_data[START_OVER] = False
    return STOPPING


def production_warning(env, args):
    if len(args):
        env = 'PRODUCTION' if env == 'prod' else 'STAGING'
        cmd = ' '.join(args)
        # allow some time to cancel commands
        for i in [4, 3, 2, 1]:
            click.echo(f'!! {env} !!: Running "{cmd}" in {i} seconds')
            time.sleep(1)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1514326396:AAGaTRWcGgSBAItsLeCZKadI9qPbf44Byg8", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Set up third level ConversationHandler (collecting features)
    description_conv_self = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(
                select_feature, pattern='^' + str(MALE) + '$' #API data
            ), 
        ],
        states={
            SELECTING_FEATURE: [
                CallbackQueryHandler(ask_for_input, pattern='^(?!' + str(END) + ').*$')
            ],
            TYPING: [MessageHandler(Filters.text & ~Filters.command, save_input)],      
        },
        fallbacks=[
            CallbackQueryHandler(end_describing, pattern='^' + str(END) + '$'),
            CommandHandler('stop', stop_nested),
        ],
        map_to_parent={
            # Return to second level menu
            END: SELECTING_LEVEL,
            # End conversation alltogether
            STOPPING: STOPPING,
        },
    )

    # Set up third level ConversationHandler (collecting features)
    description_conv = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(
                select_feature, pattern='^' + str(MALE) + '$' #API data
            ), 
            CallbackQueryHandler(
                select_feature1, pattern='^' + str(FEMALE) + '$' #Manual Trading
            ),
            CallbackQueryHandler(
                select_feature2, pattern='^' + str(AUTOMATED) + '$' #Automatic Trading
            ),
            CallbackQueryHandler(
                select_feature3, pattern='^' + str(SETTINGS) + '$' #Execute Settings Trading
            )
        ],
        states={
            SELECTING_FEATURE: [
                # this ask for input is used by verify keys level   SELF.
                CallbackQueryHandler(ask_for_input, pattern='^(?!' + str(END) + ').*$')
            ],
            TYPING: [MessageHandler(Filters.text & ~Filters.command, save_input)],

            #handling all the manual trading
            SELECTING_FEATURE1: [
                CallbackQueryHandler(ask_for_input1, pattern='^(?!' + str(ENDMANUAL) + ').*$'),
            ],

            

            # Handling all the automated trading
            SELECTING_FEATURE2: [

                CallbackQueryHandler(ask_for_input2, pattern='^(?!' + str(ENDMANUAL) + ').*$'),

            ],
            # TYPING2: [MessageHandler(Filters.text & ~Filters.command, save_input2)],

            #Processing all the trade setting data
            SELECTING_FEATURE3: [
                CallbackQueryHandler(ask_for_input3, pattern='^(?!' + str(END) + ').*$'),

            ],
            TYPING3: [MessageHandler(Filters.text & ~Filters.command, save_input3)]
            
        },
        fallbacks=[
            CallbackQueryHandler(end_describing_manual, pattern='^' + str(ENDMANUAL) + '$'),
            CallbackQueryHandler(end_describing, pattern='^' + str(END) + '$'),
            CommandHandler('stop', stop_nested),
        ],
        map_to_parent={
            
            # Return to second level menu
            END: SELECTING_LEVEL,
           
            # End conversation alltogether
            STOPPING: STOPPING,
        },
    )

    # Set up second level ConversationHandler (adding a person)
    add_member_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(select_level, pattern='^' + str(ADDING_MEMBER) + '$')],
        states={
            # SELECTING_LEVEL: [
            #     CallbackQueryHandler(select_feature, pattern=f'^{MALE}$|')
            # ],
            SELECTING_LEVEL: [
                CallbackQueryHandler(select_gender, pattern=f'^{PARENTS}$|^{CHILDREN}$|^{NEIGHBORS}$|^{FOREIGNERS}$')
            ],
            SELECTING_GENDER: [description_conv],
        },
        fallbacks=[
            CallbackQueryHandler(show_data, pattern='^' + str(SHOWING) + '$'),
            CallbackQueryHandler(end_second_level, pattern='^' + str(END) + '$'),
            CommandHandler('stop', stop_nested),
        ],
        map_to_parent={
            # After showing data return to top level menu
            SHOWING: SHOWING,
            # Return to top level menu
            END: SELECTING_ACTION,
            # End conversation alltogether
            STOPPING: END,
        },
    )

    add_self_conv = ConversationHandler(
        entry_points=[ CallbackQueryHandler(adding_self, pattern='^' + str(ADDING_SELF) + '$')],
        states={
            DESCRIBING_SELF: [description_conv],
           
        },
        fallbacks=[
            CallbackQueryHandler(show_data, pattern='^' + str(SHOWING) + '$'),
            CallbackQueryHandler(end_second_level, pattern='^' + str(END) + '$'),
            CommandHandler('stop', stop_nested),
        ],
        map_to_parent={
            # After showing data return to top level menu
            SHOWING: SHOWING,
            # Return to top level menu
            END: SELECTING_ACTION,
            # End conversation alltogether
            STOPPING: END,
        },
    )

    # Set up top level ConversationHandler (selecting action)
    # Because the states of the third level conversation map to the ones of the econd level
    # conversation, we need to make sure the top level conversation can also handle them
    selection_handlers = [
        add_member_conv,
        add_self_conv,
        CallbackQueryHandler(show_data, pattern='^' + str(SHOWING) + '$'),
        # CallbackQueryHandler(adding_self, pattern='^' + str(ADDING_SELF) + '$'),
        CallbackQueryHandler(end, pattern='^' + str(END) + '$'),
    ]
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SHOWING: [CallbackQueryHandler(start, pattern='^' + str(END) + '$')],
            SELECTING_ACTION: selection_handlers,
            SELECTING_LEVEL: selection_handlers,
            # DESCRIBING_SELF: [description_conv],
            STOPPING: [CommandHandler('start', start)],
        },
        fallbacks=[CommandHandler('stop', stop)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    # Then, we need to run the loop with a task
    #loop.run_until_complete(main())

    #loop.create_task(main())
    p4 = Process(target = main)
    p4.start()
    # with app.app_context():
    # app.run(debug = False, host="0.0.0.0",port=85)
    # app.run(debug = False, host="0.0.0.0",port=5000)
    # app.run(host="0.0.0.0",port=80)

    #app.run(host="212.49.95.112:5055")
    #main()