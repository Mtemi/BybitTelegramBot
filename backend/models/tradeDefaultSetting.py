from .helpers import BaseClass
from db import db
from datetime import datetime

class TradeDataDefaults(BaseClass, db.Model):
    __tablename__ = "trade_defaults"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telegramid = db.Column(db.Integer,nullable=False)
    asset = db.Column(db.String(50),  nullable=False)
    amount = db.Column(db.String(50))
    takeprofit = db.Column(db.String(50))
    stoploss= db.Column(db.String(50))
    trailingstop = db.Column(db.String(50))
    newtrailingactive= db.Column(db.String(50))
    leverage = db.Column(db.String(50))
    mtype = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime)



    # # relationships
    # user_id = db.Column(db.Integer, db.ForeignKey('telegram.id',  ondelete="CASCADE"), nullable=False)
    # user = db.relationships('users', backref('exchange', lazy=True))

    def __init__(self,telegramid, asset, amount, takeprofit, stoploss, trailingstop, newtrailingactive, leverage,mtype):
        now = datetime.now()
        self.telegramid = telegramid
        self.asset = asset
        self.amount = amount
        self.takeprofit = takeprofit
        self.stoploss = stoploss
        self.trailingstop= trailingstop
        self.newtrailingactive = newtrailingactive
        self.leverage = leverage
        self.mtype = mtype
        self.modified_on = now.strftime("%Y-%m-%d %H:%M:%S")
    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

   