from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Transaction(db.Model, SerializerMixin):

    __tablename__ = 'transactions'    
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='transactions')

    def __repr__(self):
        return f'<Transaction {self.id}>'
    
class User(db.Model, SerializerMixin):

    __tablename__ = 'users'    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    transactions = db.relationship('Transaction', back_populates='user')

    def __repr__(self):
        return f'<User {self.id}>'
