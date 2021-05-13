"""empty message

Revision ID: dfae13cbd321
Revises: 5080958356d4
Create Date: 2021-05-12 15:53:03.748753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfae13cbd321'
down_revision = '5080958356d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'goal')
    # ### end Alembic commands ###