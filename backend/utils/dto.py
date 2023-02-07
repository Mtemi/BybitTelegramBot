from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class BotDto:
    api = Namespace('bot', description='bot realated operations')
    bot = api.model('bot', {
      'bot_name': fields.String(required=True, description='The bot name specified by a user. It must be unique'),
      'exchange_name': fields.String(required=True, description='The exchange platform, Binance'),
      'pairs': fields.String(required=True, description='the trading symbol pair'),
      'strategy': fields.String(required=True, description='the order type either Sell or Buy'),
      'profit_currency': fields.String(required=True, description='the asset to collect profits'),
      'base_order_size': fields.String(required=True, description='the quantity to place an order'),
      'safety_order_size': fields.String(required=True, description='safety quantity price to place an order'),
      'start_order_type': fields.String(required=True, description='the order type Market, Limit...'),
      'signal_type': fields.String(required=True, description='the trigger mechanism, Manual, Automated, TradingView'),
      'take_profit': fields.String(required=True, description='percentage to calculate takeprofit price'),
      'stop_loss': fields.String(required=True, description='percentatage to calculate stoploss price')
    })
    botId = api.model('botId', {'bot_id': fields.Integer(required=True, description='The bot Id')})
    botOrder = api.model('botOrder', {'bot_id': fields.Integer(required=True, description='The bot Id')})

class ExchangeDto:
    api = Namespace('exchange', description='exchnage related operations')
    exchange = api.model('exchange', {
        'exch_name': fields.String(required=True, description='The name of the exchange as selected by user.Must be unique'),
        'api_key': fields.String(required=True, description='the Binance Api Key'),
        'api_secret': fields.String(required=True, description='the Binance Api Secret'),
    } )