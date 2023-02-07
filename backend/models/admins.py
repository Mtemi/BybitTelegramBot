from db import db
from .helpers import BaseClass
from sqlalchemy.orm import relationship
from datetime import datetime

class AdminModel(BaseClass, db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self,email,password, role):
        now = datetime.now()
        self.registered_on = now.strftime("%Y-%m-%d %H:%M:%S")
        self.email = email
        self.password = password
        self.role = role
        