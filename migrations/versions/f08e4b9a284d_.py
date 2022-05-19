"""empty message

Revision ID: f08e4b9a284d
Revises: fa0b3ba0992e
Create Date: 2022-04-13 14:08:20.897761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f08e4b9a284d'
down_revision = 'fa0b3ba0992e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password_hashed', sa.String(length=128), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.Column('email_confirmation_sent_on', sa.DateTime(), nullable=True),
    sa.Column('email_confirmed', sa.Boolean(), nullable=True),
    sa.Column('email_confirmed_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###