from po3 import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'

    # User Authentication fields
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),unique=True,index=True)
    username = db.Column(db.String(32),nullable=False,unique=True)
    password_hash = db.Column(db.String(128))

    # User fields
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    profile_image = db.Column(db.String(128,nullable=False,default='default.svg'))

    # Relations
        # Set when create Recipe model






# Recipe model