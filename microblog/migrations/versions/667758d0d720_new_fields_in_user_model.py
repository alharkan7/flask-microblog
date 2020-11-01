"""new fields in user model

Revision ID: 667758d0d720
Revises: 03cc7433627b
Create Date: 2020-11-01 14:06:05.559018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '667758d0d720'
down_revision = '03cc7433627b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###