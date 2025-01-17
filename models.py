from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):

    __tablename__ = 'users'

    serialize_rules = ('-transactions.user', '-transactions.transaction_tags', '-transactions.transaction_tags.tag')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    transactions = db.relationship('Transaction', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.id}>'

class Transaction(db.Model, SerializerMixin):

    __tablename__ = 'transactions'

    serialize_rules = ('-user.transactions', '-transaction_tags.transaction', '-transaction_tags.tag.transactions')

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='transactions')

    transaction_tags = db.relationship('TransactionTag', back_populates='transaction', cascade='all, delete-orphan')
    
    
    # tags = db.relationship('Tag', secondary='transaction_tags', back_populates='transactions')

    def __repr__(self):
        return f'<Transaction {self.id}>'

class TransactionTag(db.Model, SerializerMixin):
    
    __tablename__ = 'transaction_tags'

    serialize_rules = ('-transaction.transaction_tags', '-tag.transaction_tags')

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)

    transaction = db.relationship('Transaction', back_populates='transaction_tags')
    tag = db.relationship('Tag', back_populates='transaction_tags')

    def __repr__(self):
        return f'<TransactionTag {self.id}>'

class Tag(db.Model, SerializerMixin):
    
    __tablename__ = 'tags'

    serialize_rules = ('-transaction_tags.tag', '-transaction_tags.transaction.transaction_tags')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    transaction_tags = db.relationship('TransactionTag', back_populates='tag', cascade='all, delete-orphan')

    # transactions = db.relationship('Transaction', secondary='transaction_tags', back_populates='tags')
    
    def __repr__(self):
        return f'<Tag {self.id}>'