from faker import Faker
from models import db, Transaction, User
from app import app
from datetime import datetime

fake = Faker()

with app.app_context():
    # delete all data from tables
    db.session.query(Transaction).delete()
    db.session.query(User).delete()
    db.session.commit()

    # Seed users
    for _ in range(10):
        user = User(
            name=fake.name(),
            email=fake.unique.email()
        )
        db.session.add(user)

    # Seed transactions
    for _ in range(100):
        transaction = Transaction(
            amount=fake.random_int(100, 10000),
            description=fake.word(),
            category=fake.random_element(elements=('income', 'expense')),
            date=fake.date_time_between(start_date='-1y', end_date='now'),
            user_id=fake.random_int(1, 10)
        )
        db.session.add(transaction)

    db.session.commit()