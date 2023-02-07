from pybybit import Bybit
import json
api_key = "a3mxwletKMbd7pNVVZ"
api_secret = "epzYwlzw12ZMaViJuUi7dmiTCa7RO4ALlyZq"

bybit1 = Bybit(api_key=api_key,
                secret=api_secret, symbol="ETHUSD", ws=True, test=False)
order_resp = bybit1.place_active_order(side="Buy", symbol="ETHUSD", order_type="Market", qty=5,time_in_force='PostOnly', reduce_only=False)

print(order_resp)
def calcLastPrice(bybit1):
    ticker = bybit1.get_tickers("ETHUSD")
    print(json.dumps(ticker, indent=2))
    tickers = ticker["result"]
    print("Tickers ",tickers)
    tick = tickers[0]
    print("Last Price", tick['last_price'])
    last_price = float(tick['bid_price'])
    return last_price

last_price = calcLastPrice(bybit1)
print("Last Price", last_price)
print("None  Buy order being executed")
# Since a Buy Position has been Opened, First Thing we set data type to Limit
print('Take Profit by 100 ----------------------------------------------------------')
tprofit = 0.7
print(tprofit/100)
print('Multiply By Entry Price ----------------------------------------------------------')
takeProfitby100 = tprofit/100
print(takeProfitby100*last_price)
takeprofit = (takeProfitby100*last_price)+last_price
print('Take Profit Margin----------------------------------------------------------')
print(takeprofit)

print('Stop Loss by 100 ----------------------------------------------------------')
sLoss = 0.5
print(sLoss/100)
print('Multiply By Entry Price ----------------------------------------------------------')
stopLossby100 = sLoss/100
print(stopLossby100*last_price)
stoploss = last_price-(stopLossby100*last_price)
print('Stop Loss Margin----------------------------------------------------------')
print(stoploss)


# print('new_trailing_active Stop by 100 ----------------------------------------------------------')
# new_trailing_active1 = float(data['new_trailing_active'])
# print(new_trailing_active1/100)
# print('Multiply By Entry Price ----------------------------------------------------------')
# new_trailing_active100 = new_trailing_active1/100
# print(new_trailing_active100*last_price)
# new_trailing_active = (new_trailing_active100*last_price)+last_price
# print('new_trailing_active Margin ----------------------------------------------------------')
# print(new_trailing_active)
# print('Sending Order in ', data['side'],'position')


print('_________________________________________________________________________________________________')
print("Printing takeprofit",takeprofit)
order_resp = bybit1.place_active_order_ts(symbol="ETHUSD", take_profit = round(takeprofit, 3), stop_loss=stoploss, trailing_stop=takeprofit)
#error_ret(ret_error)
print('RESPONSE FROM ACTIVATING TRAILING_STOP')
print((order_resp))
print('RETURN MESSAGEE FROM ACTIVATING TRAILING_STOP')
print(order_resp['ret_msg'])
ret_msgd = order_resp['ret_msg']
print(ret_msgd)
