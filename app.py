from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Transaction, User
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

# CRUD operations for User model
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return make_response([user.to_dict() for user in User.query.all()], 200)
    elif request.method == 'POST':
        data = request.get_json()
        user = User(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return make_response(user.to_dict(), 201)

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def user_by_id(id):
    user = User.query.get(id)

    if user == None:
        return make_response({'error': 'User not found'}, 404)

    else:
        if request.method == 'GET':
            return make_response(user.to_dict(), 200)

        elif request.method == 'PATCH':
            data = request.get_json()

            if 'name' in data:
                user.name = data['name']
            if 'email' in data:
                user.email = data['email']

            db.session.commit()
            return make_response(user.to_dict(), 200)

        elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()
            return make_response({'message': 'User deleted successfully'}, 200)


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