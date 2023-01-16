"""add fist and last name to user model

Revision ID: 20654f54161c
Revises: 9f0140e27581
Create Date: 2023-01-16 23:49:27.059388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20654f54161c'
down_revision = '9f0140e27581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=160), server_default='', nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=160), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
