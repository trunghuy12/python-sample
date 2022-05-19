"""empty message

Revision ID: fa0b3ba0992e
Revises: 
Create Date: 2022-04-13 10:57:36.699356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa0b3ba0992e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stock_symbol', sa.String(length=255), nullable=False),
    sa.Column('number_of_shares', sa.Integer(), nullable=False),
    sa.Column('purchase_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_stocks'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stocks')
    # ### end Alembic commands ###