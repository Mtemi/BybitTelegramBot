from db import db
from .helpers import BaseClass
from sqlalchemy.orm import relationship
from datetime import datetime

class Telegram(BaseClass, db.Model):
    __tablename__ = "telegram"
    
    id = db.Column(db.Integer, primary_key=True)
    telegramid = db.Column(db.Integer, unique=True, nullable=False)
    verified = db.Column(db.String(255))
    api_key = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    second_name = db.Column(db.String(255))
    inviter_id = db.Column(db.String(255))
    api_secret = db.Column(db.String(255))
    auth_token = db.Column(db.String(255))
    registered_on = db.Column(db.DateTime, nullable=False)
    
    # trade_defaults = relationship("TradeDataDefaults", 
    #     backref="telegram",
    #     cascade="all, delete",
    #     passive_deletes=True
    #     )

    def __init__(self, telegramid, first_name, second_name, api_key, inviter_id, api_secret, verified, auth_token=None):
        now = datetime.now()
        self.registered_on = now.strftime("%Y-%m-%d %H:%M:%S")
        self.telegramid = telegramid
        self.api_key = api_key
        self.api_secret = api_secret
        self.first_name = first_name
        self.second_name = second_name
        self.inviter_id = inviter_id
        self.verified = verified
        self.auth_token = auth_token

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

class Bybit(db.Model):
    __tablename__ = "bybit"

    id = db.Column(db.Integer, primary_key=True)
    bybitid = db.Column(db.String(32))
    second_name = db.Column(db.String(32))
    def __init__(self, bybitid, second_name):
        self.bybitid = bybitid
        self.second_name = second_name
    
        print('Bybit_Data Model Class Under Backend/Security/Models CREATED')
   