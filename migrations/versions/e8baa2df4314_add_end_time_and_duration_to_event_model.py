"""Add end_time and duration to Event model

Revision ID: e8baa2df4314
Revises: 06438e9b749c
Create Date: 2024-07-09 22:41:11.011262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8baa2df4314'
down_revision = '06438e9b749c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('playlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=150), nullable=False))
        batch_op.drop_column('title')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('spotify_token', sa.String(length=500), nullable=True))
        batch_op.drop_column('spotify_refresh_token')
        batch_op.drop_column('spotify_access_token')

    with op.batch_alter_table('user_event', schema=None) as batch_op:
        batch_op.drop_column('date_joined')

    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DATETIME(), nullable=True))

    with op.batch_alter_table('user_event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_joined', sa.DATETIME(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('spotify_access_token', sa.VARCHAR(length=500), nullable=True))
        batch_op.add_column(sa.Column('spotify_refresh_token', sa.VARCHAR(length=500), nullable=True))
        batch_op.drop_column('spotify_token')

    with op.batch_alter_table('playlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.VARCHAR(length=150), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###