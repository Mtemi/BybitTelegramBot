"""
The user operations:
***Registration
***Login

"""
from flask_restx import Resource, abort
from flask import request
import jwt
import re
import datetime
import functools
from backend.models import AdminModel, Telegram
from werkzeug.security import generate_password_hash, check_password_hash
import config
from time import gmtime, strftime
from db import db
from flask import current_app as app

from ..utils.dto import UserDto
from ..utils.dto import AuthDto
import json
from backend.services.userAccountInfo import getAssetWalletBalances, getUserPnlInfo,getAllBotUsers,getOneAssetWalletBalances, getOneTradePnl
api = UserDto.api
user = UserDto.user

def login_required(method):
    @functools.wraps(method)
    def wrapper(self):
        header = request.headers.get('Authorization')
        _, token = header.split()
        try:
            decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        except jwt.DecodeError:
            return {'message':'Token is not valid.', 'status':400}
        except jwt.ExpiredSignatureError:
            return {'message':'Token is expired.', 'status': 400}
        email = decoded['email']
        if len(AdminModel.query.filter_by(email = email).all()) == 0:
            return {'message':'User is not found.', 'status':400}
        user = AdminModel.query.filter_by(email = email).all()[0]
        return method(self, user)
    return wrapper
@api.route('/register')
class Register(Resource):
    @login_required
    @api.doc('register a user')
    @api.expect(user, validate=True)
    def post(self):
    	# get the details needed to register
    	# email, username, password, api_key, api_secret,inviter_id
        email = request.json['email']
        password = request.json['password']
        # role = request.json['role']
        if user.role == 0:
        # if 1==1:
            if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', email):
                return {'message':'email is not valid.','status':400}
            if len(password) < 6:
                return {'message':'password is too short.','status':400}

            AdminModel.query.filter_by(email = email).all()

            if len(AdminModel.query.filter_by(email = email).all()) != 0:
                return {'message':'email is alread used.', 'status':400}
            else:
                user = AdminModel(email= email, password =generate_password_hash(password), role = 1)
                db.session.add(user)
                db.session.commit()
            print("lodadada")

            return {'email': email,'mesage':'admin sucessifuly registed','status':201}
        else:
            return {"message":"Unauthorized user", "status":400}

api2 = AuthDto.api
auth = AuthDto.auth

@api.route('/login')
class Login(Resource):
    @api2.doc('Login a user')
    @api2.expect(auth, validate=True)
    def post(self):
        email = request.json['email']
        password = request.json['password']
        
        if len(AdminModel.query.filter_by(email = email).all()) == 0:
            return {'message':'User is not found.','status':400}
        user = AdminModel.query.filter_by(email = email).all()[0]
        if user.role == 0 or user.role == 1:
            print("--------------------------user------------------------\n", user)
            
            if not check_password_hash(user.password, password):
                return {'message':'Password is incorrect.', 'status':400}

            exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['TOKEN_EXPIRE_HOURS'])
            encoded = jwt.encode({'email': email,'userid':user.id, 'exp': exp}, app.config['SECRET_KEY'], algorithm='HS256')

            return { 'message':'login sucessifuly', 'email': email, 'token': encoded.decode('utf-8'),'status':200}
        else:
            return {"message":"Unauthorized user", "status":400}


@api.route('/all/profile')
class BotUserDbData(Resource):
    @login_required
    @api.doc("user Profile information")
    def post(self, user):
        """
        This endpoint return all user profile information from the database
        """
        botUsers = getAllBotUsers()
        if botUsers == []:
            return {"message":"No user users in the database"}, 400
        else:
            return {"message":"user profile information fetched successifully", "data":botUsers},200

@api.route('/1/wallets/')
class BotUserWallets(Resource):
    @login_required
    @api.doc(params = {"telegramid":"telegramid"})
    def post(self, user):
        """
        Return wallet balances for a single user
        """
        try:
            int(request.args.get('telegramid'))
        except:
            return {"message":"User does not exist"},404

        telegramid = int(request.args.get('telegramid'))
        wallets = getOneAssetWalletBalances(telegramid)
        if wallets is None:
            return {"message":"user does not exist"},404
        else:
            return {"message":"user wallets fetched successifully", "data": wallets}, 200

@api.route('/1/tradepnl/')
class BotUserTradePnl(Resource):
    @login_required
    @api.doc(params = {"telegramid":"telegramid"})
    def post(self, user):
        """
        Return wallet balances for a single user
        """
        try:
            int(request.args.get('telegramid'))
        except:
            return {"message":"User does not exist"},404

        telegramid = int(request.args.get('telegramid'))
        wallets = getOneTradePnl(telegramid)
        if wallets is None:
            return {"message":"user does not exist"},404
        else:
            return {"message":"user trade and pnl fetched successifully", "data": wallets}, 200