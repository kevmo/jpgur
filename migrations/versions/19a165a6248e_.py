"""empty message

Revision ID: 19a165a6248e
Revises: 52b189abe995
Create Date: 2014-12-13 14:06:41.610638

"""

# revision identifiers, used by Alembic.
revision = '19a165a6248e'
down_revision = '52b189abe995'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('image_url', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('links', 'image_url')
    ### end Alembic commands ###
