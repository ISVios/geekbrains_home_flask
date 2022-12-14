"""add email field to user model

Revision ID: 959bae6f0995
Revises: 29c9837981a9
Create Date: 2022-12-28 15:57:12.648503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959bae6f0995'
down_revision = '29c9837981a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###
