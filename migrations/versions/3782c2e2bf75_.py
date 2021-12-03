"""empty message

Revision ID: 3782c2e2bf75
Revises: ef23d9a68770
Create Date: 2021-10-14 22:15:26.690877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3782c2e2bf75'
down_revision = 'ef23d9a68770'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_quotes_author', table_name='quotes')
    op.create_index(op.f('ix_quotes_author'), 'quotes', ['author'], unique=False)
    op.drop_index('ix_quotes_book_title', table_name='quotes')
    op.create_index(op.f('ix_quotes_book_title'), 'quotes', ['book_title'], unique=False)
    op.drop_index('ix_quotes_quote', table_name='quotes')
    op.create_index(op.f('ix_quotes_quote'), 'quotes', ['quote'], unique=False)
    op.drop_index('ix_quotes_user_id', table_name='quotes')
    op.create_index(op.f('ix_quotes_user_id'), 'quotes', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quotes_user_id'), table_name='quotes')
    op.create_index('ix_quotes_user_id', 'quotes', ['user_id'], unique=False)
    op.drop_index(op.f('ix_quotes_quote'), table_name='quotes')
    op.create_index('ix_quotes_quote', 'quotes', ['quote'], unique=False)
    op.drop_index(op.f('ix_quotes_book_title'), table_name='quotes')
    op.create_index('ix_quotes_book_title', 'quotes', ['book_title'], unique=False)
    op.drop_index(op.f('ix_quotes_author'), table_name='quotes')
    op.create_index('ix_quotes_author', 'quotes', ['author'], unique=False)
    # ### end Alembic commands ###
