import logging
from time import sleep
#from backend.extensions import Bybit 
from .pybybit import Bybit
#from mtemibybit import BybitMoneyBadger
import time
import json
import ccxt
import ast
import bybit
#from webhookbot import test

from backend.security.models import Bybit as BybitModel
from backend.security.models import Telegram
from backend.extensions import Bybit 
from backend.app import create_app
from flask_alembic import Alembic
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

app = create_app()

db = SQLAlchemy(metadata=MetaData(naming_convention={
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}))
alembic = Alembic()


class Actions():

    keyss = ''
    secretss = ''
    thisdict =	{
    "Uid": 0,
    "Key": 0,
    "Secret": 0
    }
    print(thisdict)

    thisdict1 =	{
    "uids": 0
    }
    print(thisdict1)

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

        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bybit_bot"
            )

        select_stmt = "SELECT api_key FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        re = cur.execute(select_stmt, { 'telegram_id': data["TelegramID"]})
        print('API Key from Telegram', re)
        bybit_ids = cur.fetchall()
        print('API Key Verification Data pulled from Database', bybit_ids)
        api_key = ''
        for x in bybit_ids:
            api_key = str(' '.join(map(str, (x))))
            print('api_key', api_key)
        cnx.commit()
        cur.close()

        select_stmtt = "SELECT api_secret FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        api_secrett = cur.execute(select_stmtt, { 'telegram_id': data["TelegramID"]})
        print('API Secret from Telegram', api_secrett)
        bybit_idst = cur.fetchall()
        print('Secret Verification Data pulled from Database', bybit_idst)
        api_secret = ''
        for x in bybit_idst:
            api_secret = str(' '.join(map(str, (x))))
            print('api_key', api_secret)

        cnx.commit()
        cur.close()

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

        bybit1.cancel_all_active_orders(symbol=data['symbol'])

        print('Cancel ALL Conditional Orders')

        bybit1.cancel_all_conditional_orders(symbol=data['symbol'])

        #bybit1.cancel_conditional_order(order_id = order_ids)


        if position_list is not None: 
            print('POSITION -------------------LIST---------------------------------------')
            pl = position_list['result']
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
        else: 
            print('Nothing to Close as no open positions')

            """
            {"type": "Null",
            "side": "Null",
            "amount": "Null",
            "symbol": "Null",
            "takeProfit": " Null",
            "stopLoss": "Null",
            "trailingStop": "Null",
            "leverage": "Null",
            "key": "Null"}
            """

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
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bybit_bot"
            )

        select_stmt = "SELECT api_key FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        re = cur.execute(select_stmt, { 'telegram_id': data["TelegramID"]})
        print('API Key from Telegram', re)
        bybit_ids = cur.fetchall()
        print('API Key Verification Data pulled from Database', bybit_ids)
        api_key = ''
        for x in bybit_ids:
            api_key = str(' '.join(map(str, (x))))
            print('api_key', api_key)
        cnx.commit()
        cur.close()

        select_stmtt = "SELECT api_secret FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        api_secrett = cur.execute(select_stmtt, { 'telegram_id': data["TelegramID"]})
        print('API Secret from Telegram', api_secrett)
        bybit_idst = cur.fetchall()
        print('Secret Verification Data pulled from Database', bybit_idst)
        api_secret = ''
        for x in bybit_idst:
            api_secret = str(' '.join(map(str, (x))))
            print('api_key', api_secret)

        cnx.commit()
        cur.close()

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
        save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
        leverage_data = save_leverage
        print(save_leverage)
        print("Leverage Saved")


    def close_webhook(webhook_data):
        data = webhook_data
        print('Trade Close Data as Literal', data)
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bybit_bot"
            )

        select_stmt = "SELECT api_key FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        re = cur.execute(select_stmt, { 'telegram_id': data["TelegramID"]})
        print('API Key from Telegram', re)
        bybit_ids = cur.fetchall()
        print('API Key Verification Data pulled from Database', bybit_ids)
        api_key = ''
        for x in bybit_ids:
            api_key = str(' '.join(map(str, (x))))
            print('api_key', api_key)
        cnx.commit()
        cur.close()

        select_stmtt = "SELECT api_secret FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        api_secrett = cur.execute(select_stmtt, { 'telegram_id': data["TelegramID"]})
        print('API Secret from Telegram', api_secrett)
        bybit_idst = cur.fetchall()
        print('Secret Verification Data pulled from Database', bybit_idst)
        api_secret = ''
        for x in bybit_idst:
            api_secret = str(' '.join(map(str, (x))))
            print('api_key', api_secret)

        cnx.commit()
        cur.close()

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

        position_list

        if position_list is not None: 
            print('POSITION -------------------LIST---------------------------------------')
            pl = position_list['result']
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
        else: 
            print('Nothing to Close as no open positions')

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
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bybit_bot"
            )

        select_stmt = "SELECT api_key FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        re = cur.execute(select_stmt, { 'telegram_id': data["TelegramID"]})
        print('API Key from Telegram', re)
        bybit_ids = cur.fetchall()
        print('API Key Verification Data pulled from Database', bybit_ids)
        api_key = ''
        for x in bybit_ids:
            api_key = str(' '.join(map(str, (x))))
            print('api_key', api_key)
        cnx.commit()
        cur.close()

        select_stmtt = "SELECT api_secret FROM telegram_bot WHERE telegram_id = %(telegram_id)s"
        cur = cnx.cursor()
        api_secrett = cur.execute(select_stmtt, { 'telegram_id': data["TelegramID"]})
        print('API Secret from Telegram', api_secrett)
        bybit_idst = cur.fetchall()
        print('Secret Verification Data pulled from Database', bybit_idst)
        api_secret = ''
        for x in bybit_idst:
            api_secret = str(' '.join(map(str, (x))))
            print('api_key', api_secret)

        cnx.commit()
        cur.close()

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
        save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
        manual_leverage = save_leverage['ret_msg']
        print(manual_leverage)
        print("Leverage Saved")    
        adjusted_manual_leverages = bybit1.get_leverage()
        adjusted_manual_leverage = adjusted_manual_leverages['result']
        print('current_manual_leverage -----------current_manual_leverage--------')
        print(adjusted_manual_leverage)

    def send_order(self, data):

        global nonebuy
        global nonesell 
        global oldqty
        global oldprice
        global oldqtysell
        global oldpricesell
        global ret_msg 
        global order_id000
        global leverage_data
        global wbalance
        global placed_usd_value
        global placed_btc_value
        global order_ids
        
        global error_reta 

        global  created_at

        global initial_symbol 
        global initial_side
        global initial_size
        global initial_entry_price
        global initial_leverage

        global final_symbol 
        global final_side
        global final_size
        global final_entry_price
        global final_leverage
        global tick_size

        def error_ret(error_rets):
            error_reta  = error_rets

        created_at = ''

        ret_msg = ''
        order_id000 = ''
        leverage_data = ''
        wbalance = 0
        placed_usd_value = 0
        placed_btc_value = 0
        leverage_value = 0

        initial_symbol = ''
        initial_side = ''
        initial_size = ''
        initial_entry_price = 0
        initial_leverage = 0

        final_symbol = ''
        final_side = ''
        final_size = ''
        final_entry_price = 0
        final_leverage = 0

        #data['side'] = 'Sell'
        #bybit1 = Bybit(api_key='JB76Njd3U64amNpkHF',
                    #secret='LblyOzDpw23uwxfKxPH5itad50MIsTlW6iyW', symbol=data['symbol'], ws=True, test=True)
        #Client API Keys
        """
        with open('keys.json', 'r+') as json_file:
            datasa = json.load(json_file)
            print('Data Read From File', datasa)
        #print('Data Read from JSON', data["symbol"])
        """
        print('dumped json data',data)
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
            print('api_key', api_key)


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
            print('api_secret', api_secret)

        print('---2222222---keyss--------secretss--------------')

        trade_symbol = data['symbol']

        bybit1 = Bybit(api_key=api_key,
                    secret=api_secret, symbol=data['symbol'], ws=True, test=False)

        print('api_key', api_key ,'api_secret', api_secret)
        # Send the order to the exchange, using the values from the tradingview alert.
        print('Sending:', trade_symbol, data['type'], data['side'], data['amount'])
        print('Trading Amount:', data['amount'])
        print('Side:', data['side'])
        print('Type:', data['type'])
        wallet_balance = bybit1.get_wallet_balance('BTC')
        print('Wallet Balance ----------------------------------------------------------')
        
        print(wallet_balance)
        print(wallet_balance['result']['BTC']['available_balance'])
        wbalance = wallet_balance['result']['BTC']['available_balance']
        print('Place Order Amount')
        intamountpercentage  = float(data['amount'])/100
        print('Int Amount Percentage', intamountpercentage)
        intwalletbalance = wallet_balance['result']['BTC']['available_balance']
        print('Wallet Balance', intwalletbalance)

        leverage = bybit1.get_leverage()
        print('Leverage ----------------------------------------------------------')
        print(json.dumps(leverage, indent=2))
        leverages = leverage["result"][trade_symbol]['leverage']
        print("Leverage Value", leverages)
        
        #time.sleep(5.0)

        position = bybit1.get_position_http()
        print('Position ----------------------------------------------------------')
        print('GENERAL POSITION', position)
        print('Position ----------------------------------------------------------')
        position_result  = position['result']
        print('SIZE OF THE POSITION RESULT ABOVE', len(position_result))
        print('Your Initial Position',position_result)
        json.dumps(position_result, indent=2)
        initial_symbol = position_result[0]['symbol']
        initial_side = position_result[0]['side']
        initial_size = position_result[0]['size']
        initial_entry_price = position_result[0]['entry_price']
        initial_leverage = position_result[0]['leverage']


        print('Position Result', position_result[0]['side'])
        position_side = position_result[0]['side']
        position_take_profit = position_result[0]['take_profit']
        print('Position Take Profit', position_take_profit)
        position_stop_loss = position_result[0]['stop_loss']
        print('Position Stop Loss', position_stop_loss)
        print('Order ID ----------------------------------------------------------')
        order_idss = position_result[0]['id']
        print('Example Order ID',order_idss)
        #print(position['entry_price'])

        ticker = bybit1.get_tickers(data['symbol'])
        print(json.dumps(ticker, indent=2))
        tickers = ticker["result"]
        print("Tickers ",tickers)
        tick = tickers[0]
        #print("Last Price", tick['last_price'])
        last_price = float(tick['bid_price'])
        print("Bid Price Value Two", last_price)

        ticker_symbols = bybit1.symbols()
        print('ticker_symbol sizes')
        #print(json.dumps(ticker_symbols, indent=2))
        ticker_symbols1 = ticker_symbols["result"]
        print("RESULT FOR ticker_symbol", ticker_symbols1)
        for x in range(len(ticker_symbols1)):
            #print(ticker_symbols1[0]['name'])
            if ticker_symbols1[x]['name']==data['symbol']:
                tick_size = ticker_symbols1[x]['price_filter']['tick_size']
                print(tick_size)
            else: 
                print('Symbol Not Found')

        #The Position Entry Price Irrespective of where position or not
        print("Position Entry Price", position_result[0]['entry_price']) 
        entry_price = float(position_result[0]['entry_price'])
        print("Bid Price Value Two", entry_price)

        orderamounts = intwalletbalance*last_price
        print("Order Amount", orderamounts)
        orderamount  = orderamounts*intamountpercentage
        print('Order Amount in USD', orderamount)
        placed_usd_value = orderamount
        placed_btc_value = orderamount/last_price

        #Get Active Order Real Time
        real_time_active_order = bybit1.get_active_order(trade_symbol)
        print('Active Order Real Time ----------------------------------------------------------')
        real_time_active_order_result  = real_time_active_order['result']
        print('Real time active order result',real_time_active_order_result)
        json.dumps(real_time_active_order_result, indent=2)
        print('Real time active order result Intented Results',real_time_active_order_result)

        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']=='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = (takeProfitby100*last_price)+last_price
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = last_price-(stopLossby100*last_price)
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)
                
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), stop_loss=stoploss)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')


            
        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']=='None':  
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = last_price - (takeProfitby100*last_price)
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = last_price + (stopLossby100*last_price)
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)
                
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), stop_loss=stoploss)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')

        if position_side == 'Buy'and data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']=='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            # if there is no order Position at All
            
            data['side'] = 'Sell'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')
            
            data['side'] = 'Buy'
            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount+position_value,
            stop_loss=stoploss,time_in_force='PostOnly')

            
            
            
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly')
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']=='None':  # if there is no order Position at All
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')
            
            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount+position_value,
            stop_loss=stoploss,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly')
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']

                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']=='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')

            
            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount,
            stop_loss=stoploss,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly')
            
        
            
            ret_msgd = order_resp['ret_msg']

            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']=='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')
            
            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount,
            stop_loss=stoploss,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            

            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
            #-----------------------------------------------------------------------------------------------------------------
            
        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']=='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit

                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = last_price-(stopLossby100*last_price)
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)

                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], stop_loss=stoploss)
                error_reta  = 'Order Received'
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = 'You need pass a trailing_active value whose modulus' +str(tick_size)+' is true.\n \n'
                'Order Not Received'
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = stoploss
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')

        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']=='None':  
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit

                print('Stop Loss by 100 ----------------------------------------------------------')
                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = (stopLossby100*last_price) + last_price
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)

                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], stop_loss=stoploss)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd
                'Order Not Received'
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = stoploss
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')


        if position_side == 'Buy'==data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']=='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  
            
            # if there is no order Position at All
            
            data['side'] = 'Sell'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')
            
            data['side'] = 'Buy'
            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
        

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount+position_value,
            stop_loss=stoploss,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly')

            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']

                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']=='None':  # if there is no order Position at All
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')
            
            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount+position_value,
            stop_loss=stoploss,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']=='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  


            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')

            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount,
            stop_loss=stoploss,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly')
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            
            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']=='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly')
            
            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount,
            stop_loss=stoploss,time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, time_in_force='PostOnly')
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
            #-----------------------------------------------------------------------------------------------------------

        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']=='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            # and we have a new Buy Order
            print("None  Buy order being executed")
            # Since a Buy Position has been Opened, First Thing we set data type to Limit
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = (takeProfitby100*last_price)+last_price
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit))
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta  = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta  = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = 'No Order Placed'
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')

        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']=='None':  

            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            # and we have a new Buy Order
            print("None  Buy order being executed")
            # Since a Buy Position has been Opened, First Thing we set data type to Limit
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = last_price - (takeProfitby100*last_price)
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit))
                error_reta  = 'Order placed as below'
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = 'No Order Placed'
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')
        if position_side == 'Buy'==data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']=='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            
            data['side'] = 'Sell'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly', reduce_only=False)
            
            data['side'] = 'Buy'
            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount+position_value,
            time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 

            #order_rep = bybit1.replace_active_order(order_id = real_time_active_order_result['order_id'], symbol=data['symbol'],
            #                     p_r_qty=orderamount+position_value, p_r_price=int(takeprofit))
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
                        qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']=='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly', reduce_only=False)
            
            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount+position_value,
            time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']=='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly', reduce_only=False)

            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount,
            time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            
            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']=='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  


            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly', reduce_only=False)
            
            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=orderamount,
            time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            ret_msgd = order_resp['ret_msg']
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
            #---------------------------------------------------------------------------------------------------------------
            
        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']=='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")   

            print('Sending Order in ', data['side'],'position')
            print('Sending Order in ', trade_symbol,'symbol')
            print('Order Amount ', orderamount,'USD')
            
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print(order_resp)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
        
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
                print(pl)
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
                
            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
        """
        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']=='None':  
        

            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], order_type=data['type'], qty=orderamount,
            time_in_force='PostOnly', reduce_only=False)
            
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            data['type'] = 'Limit'
            data['side'] = 'Buy'
            #We want to Add TP to the Market Order
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], order_type=data['type'],
            qty = tr_amnt, time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonesell = order_resp['result']['order_id'] if order_resp['result'] else None
            oldqtysell = orderamount
            nonesell = nonesell

            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  
    

            position1 = bybit1.get_position_http()
            print('---------------------------New Position DATA----------------------------------')
            position_result1  = position1['result']
            print('Your New Position',position_result1)
            json.dumps(position_result1, indent=2)
            final_symbol = position_result1[0]['symbol']
            final_side = position_result1[0]['side']
            final_size = position_result1[0]['size']
            final_entry_price = pl['entry_price']
            final_leverage = position_result1[0]['leverage']
            created_at = position_result1[0]['created_at'] 
            
            data['side']='Sell'
        """

        if position_side == 'Buy'and data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']=='None':  # if there is no order Position at All
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            data['side'] = 'Buy'
            # and we have a new Buy Order
            
            print('Sending Order in ', data['side'],'position')
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])


            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            
            #
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            #
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            
            print('order_resporder_resporder_resporder_resporder_resporder_resporder_resporder_resporder_resporder_resp')
            print('order_resporder_resporder_resporder_resporder_resporder_resporder_resporder_resporder_resporder_resp')
            print(order_resp)

            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']=='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']=='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  


            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)

            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            

            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']=='None':
            
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)

            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', entry_price,'Position Entry price Value')

            ticker = bybit1.get_tickers(data['symbol'])
            print(json.dumps(ticker, indent=2))
            tickers = ticker["result"]
            print("Tickers ",tickers)
            tick = tickers[0]
            print("Last Price", tick['last_price'])
            last_price = float(tick['bid_price'])

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']!='None' and data['new_trailing_active']!='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = (takeProfitby100*last_price)+last_price
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = last_price-(stopLossby100*last_price)
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)
                
                print('new_trailing_active Stop by 100 ----------------------------------------------------------')
                new_trailing_active1 = float(data['new_trailing_active'])
                print(new_trailing_active1/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                new_trailing_active100 = new_trailing_active1/100
                print(new_trailing_active100*last_price)
                new_trailing_active = (new_trailing_active100*last_price)+last_price
                print('new_trailing_active Margin ----------------------------------------------------------')
                print(new_trailing_active)
                print('Sending Order in ', data['side'],'position')

                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), stop_loss=stoploss, trailing_stop = tstoploss, new_trailing_active = new_trailing_active)
                error_reta  = 'Your trailing_active value is' +str(new_trailing_active)+''
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = 'You need pass a trailing_active value whose modulus' +str(tick_size)+' is true.\n \n'
                'Your trailing_active value is' +str(new_trailing_active)+''
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')

        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']!='None'  and data['stopLoss']!='None' and data['trailingStop']!='None' and data['new_trailing_active']=='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = (takeProfitby100*last_price)+last_price
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = last_price-(stopLossby100*last_price)
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)

                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), stop_loss=stoploss, trailing_stop = tstoploss)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta  = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta  = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')


            
        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']!='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = (takeProfitby100*last_price)+last_price
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = last_price-(stopLossby100*last_price)
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)
            

                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), stop_loss=stoploss, trailing_stop = tstoploss)
                
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    
                    error_reta  = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta  = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')


        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']!='None':  

            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = last_price - (takeProfitby100*last_price)
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('Stop Loss by 100 ----------------------------------------------------------')
                sLoss = float(data['stopLoss'])
                print(sLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                stopLossby100 = sLoss/100
                print(stopLossby100*last_price)
                stoploss = last_price+(stopLossby100*last_price)
                print('Stop Loss Margin----------------------------------------------------------')
                print(stoploss)
                
                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), stop_loss=stoploss, trailing_stop = tstoploss)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd

            print('_________________________________________________________________________________________________')

            nonesell = order_ids
            oldqtysell = orderamount
            oldpricesell = stoploss
            nonesell = nonesell

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')

        if position_side == 'Buy'==data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']!='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved") 

            # if there is no order Position at All
            # and we have a new Sell Order
            print("None   Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)


            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)

            # if there is no order Position at All
            
            data['side'] = 'Sell'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']

                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
        
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = final_size, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']!='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
        
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = final_size, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']!='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            
            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']!='None' and data['trailingStop']!='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  


            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)

            ret_msgd = order_resp['ret_msg']
            
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
            #-----------------------------------------------------------------------------------------------------------------
            
        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']!='None'and data['trailingStop']!='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  
            
            # if there is no order Position at All
            # and we have a new Buy Order
            print("None  Buy order being executed")
            # Since a Buy Position has been Opened, First Thing we set data type to Limit
            """
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            """
            """
            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            """
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)

            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            ret_msgd = order_resp['ret_msg']

            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
    

            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = tr_amnt, time_in_force='PostOnly', reduce_only=False)

            ret_msgd = order_resp['ret_msg']

            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            oldqty = tr_amnt
            #oldprice = takeprofit
            nonebuy = nonebuy
            
            print('Order ID for this Sale', nonebuy)

            """
            order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol,
            p_r_qty = position_value, p_r_price = takeprofit)
            """

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']!='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            # and we have a new Sell Order
            print("None   Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            """
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            """

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd


            data['type'] = 'Limit'
            data['side'] = 'Buy'
            #We want to Add TP to the Market Order
            print('Sending Order in ', data['side'],'position')
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = tr_amnt, time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonesell = order_resp['result']['order_id'] if order_resp['result'] else None
            oldqtysell = orderamount
            oldpricesell = stoploss
            nonesell = nonesell
    

            position1 = bybit1.get_position_http()
            print('---------------------------New Position DATA----------------------------------')
            position_result1  = position1['result']
            print('Your New Position',position_result1)
            json.dumps(position_result1, indent=2)
            final_symbol = position_result1[0]['symbol']
            final_side = position_result1[0]['side']
            final_size = position_result1[0]['size']
            final_entry_price = pl['entry_price']
            final_leverage = position_result1[0]['leverage']
            created_at = position_result1[0]['created_at'] 
            
            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']!='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            
            data['side'] = 'Sell'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price


            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Buy'
            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly', reduce_only=False)
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None
            

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']!='None':  # if there is no order Position at All
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly', reduce_only=False)
            
            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            """
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            """

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            """
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            """
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """

            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']!='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price


            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = last_price-(stopLossby100*last_price)
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly', reduce_only=False)
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']!='None' and data['trailingStop']!='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)

            print('Stop Loss by 100 ----------------------------------------------------------')
            sLoss = float(data['stopLoss'])
            print(sLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            stopLossby100 = sLoss/100
            print(stopLossby100*last_price)
            stoploss = (stopLossby100*last_price) + last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(stoploss)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, time_in_force='PostOnly', reduce_only=False)

            ret_msgd = order_resp['ret_msg']

            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            #-----------------------------------------------------------------------------------------------------------

        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']!='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = (takeProfitby100*last_price)+last_price
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)


                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('new_trailing_active Stop by 100 ----------------------------------------------------------')
                new_trailing_active1 = float(data['new_trailing_active'])
                print(new_trailing_active1/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                new_trailing_active100 = new_trailing_active1/100
                print(new_trailing_active100*last_price)
                new_trailing_active = (new_trailing_active100*last_price)+last_price
                print('new_trailing_active Margin ----------------------------------------------------------')
                print(new_trailing_active)
                print('Sending Order in ', data['side'],'position')

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), trailing_stop = tstoploss)
                error_reta  = 'Your trailing_active value is' +str(new_trailing_active)+''
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')




        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']!='None':  

            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = (takeProfitby100*last_price)+last_price
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit = int(takeprofit), trailing_stop = tstoploss)
                error_reta  = 'Your trailing_active value is' +str(new_trailing_active)+''
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = takeprofit
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')




        if position_side == 'Buy' and data['side']=='Buy' and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']!='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")         
        
            # if there is no order Position at All
            
            data['side'] = 'Sell'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Buy'
            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Stop Loss Margin----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 

            #order_rep = bybit1.replace_active_order(order_id = real_time_active_order_result['order_id'], symbol=data['symbol'],
            #                     p_r_qty=orderamount+position_value, p_r_price=int(takeprofit))
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
                        qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']!='None': 
            # if there is no order Position at All
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']!='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            # and we have a new Buy Order
            print("Buy  Buy order being executed" )
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = (takeProfitby100*last_price)+last_price
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']

                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = (takeProfitby100*entry_price)+entry_price
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']!='None' and data['stopLoss']=='None' and data['trailingStop']!='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  


            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Sell'
            print("None Sell order being executed")
            print('Take Profit by 100 ----------------------------------------------------------')
            tprofit = float(data['takeProfit'])
            print(tprofit/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            takeProfitby100 = tprofit/100
            print(takeProfitby100*last_price)
            takeprofit = last_price - (takeProfitby100*last_price)
            print('Take Profit Margin----------------------------------------------------------')
            print(takeprofit)
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']

                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd


            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None

            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            tprofit = float(data['takeProfit'])
            takeProfitby100 = tprofit/100
            takeprofit = entry_price-(takeProfitby100*entry_price)
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', takeprofit,'Take profit Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, price=int(takeprofit),time_in_force='PostOnly', reduce_only=True)
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
            #---------------------------------------------------------------------------------------------------------------
            
        if position_side == 'None' and data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']!='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit

                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd

            print('_________________________________________________________________________________________________')

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')
            
        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']!='None':
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit

                print('Trailing Stop by 100 ----------------------------------------------------------')
                tsLoss = float(data['trailingStop'])
                print(tsLoss/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                tstopLossby100 = tsLoss/100
                print(tstopLossby100*last_price)
                tstoploss = tstopLossby100*last_price
                print('Trailing Stop  Margin ----------------------------------------------------------')
                print(tstoploss)

                print('Activating Trailing Stop')
                print('ACTIVATING TRAILING STOP VALUE BELOW')
                print(tstoploss)
                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta = 'Order Placed Successfully'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd

            print('_________________________________________________________________________________________________')

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')

            
        if position_side == 'None' and data['side']=='Sell' and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']=='None':  
            
            print('I SERIOUSLY WANT TO TRACK THIS ENTRY FROM START TO THE END. THIS IS POSITION_SIDDE == NONE AND SIDE==BUY')
            
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,time_in_force='PostOnly', reduce_only=False)
            print(order_resp)
            ret_msgd = order_resp['ret_msg']
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids
                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']
                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                print('final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price final_entry_price')
                print(final_entry_price)
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd

            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)

            """
            print('_________________________________________________________________________________________________')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], new_trailing_active = new_trailing_active)
            print(order_resp)
            """
            if float(final_entry_price) % float(tick_size): 
                #last_price  = float(final_entry_price)
                # if there is no order Position at All
                # and we have a new Buy Order
                print("None  Buy order being executed")
                # Since a Buy Position has been Opened, First Thing we set data type to Limit
                print('Take Profit by 100 ----------------------------------------------------------')
                tprofit = float(data['takeProfit'])
                print(tprofit/100)
                print('Multiply By Entry Price ----------------------------------------------------------')
                takeProfitby100 = tprofit/100
                print(takeProfitby100*last_price)
                takeprofit = last_price - (takeProfitby100*last_price)
                print('Take Profit Margin----------------------------------------------------------')
                print(takeprofit)

                print('_________________________________________________________________________________________________')
                order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], take_profit=takeprofit)
                #error_ret(ret_error)
                print('RESPONSE FROM ACTIVATING TRAILING_STOP')
                print(order_resp)
                print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
                print(order_resp['ret_msg'])
                ret_msgd = order_resp['ret_msg']
                print(ret_msg)
                if ret_msgd == 'ok':
                    print('Order Placed Successfully')
                    ret_msg = 'OK'
                    order_id000 = order_ids
                    position_list = bybit1.get_position_list(symbol = data['symbol'])
                    pl = position_list['result']
                    print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                    position_size  = pl['size']
                    position_side  = pl['side']
                    final_entry_price = pl['entry_price']
                    created_at = pl['created_at']
                    error_reta  = 'Order Received'
                else : 
                    print('Order Not Placed Successfully, Error Below')
                    ret_msg = ret_msgd
                    error_reta  = ret_msgd
            else :
                print('Modulus Failed for this symbol')
                error_reta  = ret_msgd
                #error_ret(ret_error)

            print('_________________________________________________________________________________________________')

            nonebuy = order_ids
            oldqty = tr_amnt
            oldprice = stoploss
            nonebuy = nonebuy

            print('Order ID for this Sale', nonebuy)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

            print('I WANT TO TRACK RET VAKUE BEFORE EXIT')
            print(ret_msgd)
            print('END OF BUY WITH ALL PARAMETERS IN PLACE, WHERE NEXT DOES IT EXECUTE JUST TO TRACK THE ISSUE')


        if position_side == 'Buy'and data['side']=='Buy' and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']!='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")          
            
            # if there is no order Position at All
            
            data['side'] = 'Sell'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)

            data['side'] = 'Buy'
            # and we have a new Buy Order
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt+position_value,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']

                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly', reduce_only=False)
            
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Sell' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']!='None':  
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  
            
            # if there is no order Position at All
            # and we have a new Sell Order
            data['side'] = 'Buy'
            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price

            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            stop_loss=stoploss,time_in_force='PostOnly', reduce_only=False)
            data['side'] = 'Sell'
            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            print('Sending Order in ', data['side'],'position')

            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt+position_value,
            time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']

            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)

            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', entry_price,'Position Entry price Value')
            
            
            """
            order_resp = bybit1.replace_active_order(order_id = nonesell, symbol = trade_symbol, 
            p_r_qty = position_value, p_r_price = int(takeprofit)) 
            """
            
            """"""
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, time_in_force='PostOnly', reduce_only=False)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'
            
        if position_side == 'Sell' and data['side']=='Buy'and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']!='None': 
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  


            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price

            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly', reduce_only=False)

            
            print('Trailing Stop by 100 ----------------------------------------------------------')
            tsLoss = float(data['trailingStop'])
            print(tsLoss/100)
            print('Multiply By Entry Price ----------------------------------------------------------')
            tstopLossby100 = tsLoss/100
            print(tstopLossby100*last_price)
            tstoploss = tstopLossby100*last_price
            print('Trailing Stop  Margin ----------------------------------------------------------')
            print(tstoploss)
            
            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            time_in_force='PostOnly', reduce_only=False)
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Sell'
            #We want to Add TP to the Market Order
                    #We want to Add TP to the Market Order
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position')
            #,p_r_qty = int(orderamount), p_r_price = int(entry_price)
            #order_resp = bybit1.replace_active_order(order_id = nonebuy, symbol = trade_symbol, 
            #p_r_qty = position_value, p_r_price = int(takeprofit)) 
            
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value, time_in_force='PostOnly', reduce_only=False)
            
            
            ret_msgd = order_resp['ret_msg']
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            nonebuy = order_resp['result']['order_id'] if order_resp['result'] else None


            data['side']='None'
            position_side == 'None'
            data['takeProfit']!='None'
            data['stopLoss']!='None'
            data['stopLoss']!='None' 
            data['trailingStop']!='None'

        if position_side == 'Buy' and data['side']=='Sell'and data['takeProfit']=='None' and data['stopLoss']=='None' and data['trailingStop']!='None':
            leverage = bybit1.get_leverage()
            print('Leverage ----------------------------------------------------------')
            print(leverage)
            trade_symbol = data['symbol']
            print("Change Leverage")
            save_leverage = bybit1.change_leverage(trade_symbol, data['leverage'])
            leverage_data = save_leverage
            print(save_leverage)
            print("Leverage Saved")  

            position_value = position_result[0]['size']
            position_valueS = position_value*entry_price
            print('position Value in USD', position_valueS)
            bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=position_value,time_in_force='PostOnly', reduce_only=False)
            
            data['side'] = 'Sell'
            
            
            print('Sending Order in ', data['side'],'position')
            trade_symbol = data['symbol']
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            trade_symbol = trade_symbol[:-1]
            amnts = bybit1.get_wallet_balance(trade_symbol)
            print('WALLET BALANCE FOR THIS SYMBOL')
            print(amnts['result'][trade_symbol]['available_balance'])
            amnt = amnts['result'][trade_symbol]['available_balance']
            trade_amount  = amnt*(float(data['amount'])/100)
            print('AMOUNT REQUESTED FOR TRADE IN THIS SYMBOL')
            print(trade_amount)
            tr_amnt = last_price*trade_amount
            print('AMOUNT TO PLACE ON TRADE')
            print(tr_amnt)
            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'], qty=tr_amnt,
            time_in_force='PostOnly', reduce_only=False)
            
            
            ret_msgd = order_resp['ret_msg']
            
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            
            ret_msgd = order_resp['ret_msg']
            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                ret_msg = ret_msgd
            order_ids = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_ids)
            
            print('Activating Trailing Stop')
            order_resp = bybit1.place_active_order_ts(symbol=data['symbol'], trailing_stop = tstoploss)
            
            ret_msgd = order_resp['ret_msg']

            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            
            pos_take_profit = position_result[0]['take_profit']
            
            bybit1.cancel_all_active_orders(symbol=data['symbol'])
            
            data['type'] = 'Limit'
            data['side'] = 'Buy'
            
            position = bybit1.get_position_http()
            position_result  = position['result']
            entry_price = position_result[0]['entry_price']
            position_value = position_result[0]['size']
            print('Sending Order in ', data['side'],'position and ',position_value,'Position Value')
            print('And ', entry_price,'Position Entry price Value')

            order_resp = bybit1.place_active_order(side=data['side'], symbol=data['symbol'], order_type=data['type'],
            qty = position_value,time_in_force='PostOnly', reduce_only=False)

            ret_msgd = order_resp['ret_msg']

            if ret_msgd == 'OK':
                print('Order Placed Successfully')
                ret_msg = ret_msgd
                order_id000 = order_ids

                position_list = bybit1.get_position_list(symbol = data['symbol'])
                pl = position_list['result']
                print('bybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_listbybit1.get_position_list')
                position_size  = pl['size']
                position_side  = pl['side']


                position1 = bybit1.get_position_http()
                print('---------------------------New Position DATA----------------------------------')
                position_result1  = position1['result']
                print('Your New Position',position_result1)
                json.dumps(position_result1, indent=2)
                final_symbol = position_result1[0]['symbol']
                final_side = position_result1[0]['side']
                final_size = position_result1[0]['size']
                final_entry_price = pl['entry_price']
                final_leverage = position_result1[0]['leverage']
                created_at = pl['created_at']
            else : 
                print('Order Not Placed Successfully, Error Below')
                #ret_msg = ret_msgd
            order_resp = order_resp['result']['order_id'] if order_resp['result'] else None
            print(order_resp)

            data['side']='Sell'

        return 'Trade Successful'

        
