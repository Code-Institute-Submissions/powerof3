from po3 import db,login_manager,bcrypt
from flask_bcrypt import Bcrypt,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) #Getting id from db

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    # User Authentication fields
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),unique=True,index=True,nullable=False)
    username = db.Column(db.String(32),nullable=False,unique=True)
    password_hash = db.Column(db.String(128))

    # User fields
    first_name = db.Column(db.String(64),nullable=False)
    last_name = db.Column(db.String(64),nullable=False)
    profile_image = db.Column(db.String(128),default='default.svg')
    short_story = db.Column(db.Text(),default="This is my short story")

    # Relations
    recipes = db.relationship('Recipe',backref='chef',lazy=True)

    def __init__(self,first_name,last_name,email,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}" #for debugging

class Recipe(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    date = db.Column(db.DateTime,nullable=False,default=datetime.today)
    title = db.Column(db.String(140),nullable=False)
    description = db.Column(db.Text,nullable=False)
    ingriedient1 = db.Column(db.String(16),nullable=False)
    ingriedient2 = db.Column(db.String(16),nullable=False)
    ingriedient3 = db.Column(db.String(16),nullable=False)
    smoothie_video = db.Column(db.String(128),nullable=False)
    
    def __init__(self,title,description,smoothie_video,ingriedient1,
    ingriedient2,ingriedient3,user_id):
        self.title = title
        self.description = description
        self.smoothie_video = smoothie_video
        self.ingriedient1 = ingriedient1
        self.ingriedient2 = ingriedient2
        self.ingriedient3 = ingriedient3
        self.user_id = user_id 
    
    def __repr__(self):
        return f"Post ID: {self.id}" #for debugging

