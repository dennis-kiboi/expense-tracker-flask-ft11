"""Add foreign key to Transactions

Revision ID: a8e95d7ace75
Revises: cefa8dc8fc16
Create Date: 2025-01-15 16:28:40.823901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8e95d7ace75'
down_revision = 'cefa8dc8fc16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('users')
    # ### end Alembic commands ###