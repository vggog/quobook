"""empty message

Revision ID: 62ed252ddeca
Revises: 366e678f584c
Create Date: 2021-11-16 20:22:26.699428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62ed252ddeca'
down_revision = '366e678f584c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'quotes', ['quote_id'])
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.drop_index('ix_users_username', table_name='users')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.drop_column('users', 'email')
    op.drop_constraint(None, 'quotes', type_='unique')
    # ### end Alembic commands ###
