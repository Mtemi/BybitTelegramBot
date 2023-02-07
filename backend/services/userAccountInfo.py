from backend.extensions import Bybit
from backend.models import Telegram
from db import db

# check if user exists in the database
def checkUserExists(telegramid):
    exists = bool(db.session.query(Telegram).filter_by(telegramid = int(telegramid)).first())
    return exists


# get user single user api data given telegramid
def getUserApiData(telegramid):
    """
    This is a help function to get the api_key and api_secret from the database
    """
    exists = checkUserExists(telegramid)
    if exists==True:
        botUser = db.session.query(Telegram).filter(Telegram.telegramid==telegramid).first()
        apiData = {
            "api_key":botUser.api_key,
            "api_secret":botUser.api_secret
        }
        return apiData
    else:
        return None
# gets the pnl information for specific user given the telegram id



def getUsertradeInfo(api_key, api_secret, symbol):
    """
    This is a help function to get the pnl information
    """ 
    
    bybit1 = Bybit(api_key=api_key,
                    secret=api_secret, symbol=symbol, ws=True, test=False)

    tradeInfo = bybit1.get_user_trade_record(symbol=symbol)
    
    buyQuantity = []
    buyClosedPnl = []
    sellQuantity = []
    sellClosedPnl = []
    if tradeInfo["result"]["data"] != None:
        for info in tradeInfo["result"]["data"]:
            if info["side"] =="Buy":

                buyQuantity.append(info["qty"])
                buyClosedPnl.append(info["closed_pnl"])
                

            if info["side"] =="Sell":
                sellQuantity.append(info["qty"])
                sellClosedPnl.append(info["closed_pnl"])


        buyQtySum =  sum([e for e in buyQuantity])
        buyClosedPnlSum = sum(e for e in buyClosedPnl)
        sellQtySum =  sum([e for e in sellQuantity])
        sellClosedPnlSum = sum(e for e in sellClosedPnl)

        return {

                "symbol":symbol,
                "pnl_info":[
                {
                "side": "Buy",
                "total_trade_qty":buyQtySum,
                "total_closed_pnl":buyClosedPnlSum
                },
                {
                "side": "Sell",
                "total_trade_qty":sellQtySum,
                "total_closed_pnl":sellClosedPnlSum
                }
                ]}
    else:
        return {

                "symbol":symbol,
                "pnl_info":[
                {
                "side": "Buy",
                "total_trade_qty":0,
                "total_closed_pnl":0
                },
                {
                "side": "Sell",
                "total_trade_qty":0,
                "total_closed_pnl":0
                }
                ]}

    # return tradeInfo
def getWalletBalance(api_key,api_secret, symbol, asset):
    """
    This is a help function to get the wallet balance of a single asset
    """

    bybit1 = Bybit(api_key=api_key,
                    secret=api_secret, symbol=symbol, ws=True, test=False)
    wallet_balance = bybit1.get_wallet_balance(asset)
    
    wbalance = wallet_balance['result'][asset]['available_balance']
    return wbalance



"""
For more complexity on the server user the single user services to fetch the records

"""
# get all the user information from the database
def getAllBotUsers():
    usersRecords = {}
    userInfo = db.session.query(Telegram.telegramid, Telegram.first_name, Telegram.second_name, Telegram.api_key, Telegram.api_secret).all()
    if userInfo == []:
        return []
    else:
        for user in userInfo:
            usersRecords.update({user[0]:{
                "telegram_id":user[0], 
                "first_name": user[1],
                "second_name": user[2],
                "api_data":{
                    "api_key":user[3],
                    "api_secret":user[4]
                    },
                }})     
        return usersRecords


# get wallet balances given telegram id
def getOneAssetWalletBalances(telegramid):
    apiData = getUserApiData(telegramid)
    if apiData is None:
        return None
    else:
        api_key = apiData["api_key"]
        api_secret = apiData["api_secret"]

        wbBtc = getWalletBalance(api_key, api_secret, "BTCUSD","BTC")
        wbXrp = getWalletBalance(api_key, api_secret, "XRPUSD", "XRP")
        wbEos = getWalletBalance(api_key, api_secret,"EOSUSD", "EOS")
        wbEth = getWalletBalance(api_key, api_secret,"ETHUSD", "ETH")
        userwbal={      
                    "BTC": "%.6f"%float(wbBtc),
                    "ETH": "%.6f"%float(wbEth),
                    "EOS": "%.6f"%float(wbEos),
                    "XRP":  "%.6f"%float(wbXrp)
        }
        return userwbal
        
# get tradepnl given telegramid
def getOneTradePnl(telegramid):
    apiData = getUserApiData(telegramid)
    if apiData is None:
        return None
    else:
        api_key = apiData["api_key"]
        api_secret = apiData["api_secret"]

        btcUsd= getUsertradeInfo(api_key, api_secret, "BTCUSD")
        ethUsd= getUsertradeInfo(api_key, api_secret, "ETHUSD")
        xrpUsd= getUsertradeInfo(api_key, api_secret, "XRPUSD")
        eosUsd= getUsertradeInfo(api_key, api_secret, "EOSUSD")
        
        res = [btcUsd, ethUsd, xrpUsd, eosUsd]
        return res

    
# -------------------------------------------------end of single user data services --------------------------------------------------


"""
The looping functions returns all the records for every user in a single record but very resources intensive
"""

#loops for records wallet balances for every user 
def getAssetWalletBalances():
    userApiData = db.session.query(Telegram.telegramid,Telegram.api_key, Telegram.api_secret).all()
    userWalletBalances = {}
    for user in userApiData:
        telegram_id = user[0]
        api_key = user[1]
        api_secret = user[2]
        
        wbBtc = getWalletBalance(api_key, api_secret, "BTCUSD","BTC")
        wbXrp = getWalletBalance(api_key, api_secret, "XRPUSD", "XRP")
        wbEos = getWalletBalance(api_key, api_secret,"EOSUSD", "EOS")
        wbEth = getWalletBalance(api_key, api_secret,"ETHUSD", "ETH")
        userwbal={ 
                telegram_id:{
                     
                    "BTC": "%.6f"%float(wbBtc),
                    "ETH": "%.6f"%float(wbEth),
                    "EOS": "%.6f"%float(wbEos),
                    "XRP":  "%.6f"%float(wbXrp)
                }
        }
        userWalletBalances.update(userwbal)
        
    return userWalletBalances 



# loops for pnl records for every user records 
def getUserPnlInfo():
    userApiData = db.session.query(Telegram.telegramid,Telegram.api_key, Telegram.api_secret).all()
    if userApiData !=[]:
        pnl_store = {}
        for user in userApiData:
            telegramid = user[0]
            api_key = user[1]
            api_secret = user[2]
            
            btcUsd= getUsertradeInfo(api_key, api_secret, "BTCUSD")
            ethUsd= getUsertradeInfo(api_key, api_secret, "ETHUSD")
            xrpUsd= getUsertradeInfo(api_key, api_secret, "XRPUSD")
            eosUsd= getUsertradeInfo(api_key, api_secret, "EOSUSD")
            
            
            res = {telegramid:
                [btcUsd, ethUsd, xrpUsd, eosUsd]
            }
            pnl_store.update(res)
        return pnl_store
    else:
        return userApiData

# -----------------------------------------------End of all looping user data fetch services ---------------------------------------------------- 