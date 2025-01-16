from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from models import db, Transaction
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return '<h1>Welcome to Expense Tracker App</h1>'

@app.route('/transactions/<int:id>')
def get_transaction(id):
    transaction = Transaction.query.get(id)

    print(transaction)

    transaction_obj = {
        'id': transaction.id,
        'amount': transaction.amount,
        'description': transaction.description,
        'category': transaction.category,
        'date': transaction.date
    }

    if transaction:
        response = make_response(transaction_obj, 200)

        return response
    
    return 'Transaction not found', 404

if __name__ == '__main__':
    app.run(debug=True,port=5555)