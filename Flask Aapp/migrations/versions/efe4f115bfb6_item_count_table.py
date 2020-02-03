"""item count table

Revision ID: efe4f115bfb6
Revises: 5bc8ab4861a8
Create Date: 2019-12-13 09:00:46.701080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efe4f115bfb6'
down_revision = '5bc8ab4861a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'cart', 'user', ['u_cart_id'], ['id'])
    op.drop_column('cart', 'prod_cost')
    op.drop_column('cart', 'user_id')
    op.drop_column('cart', 'prod_desc')
    op.drop_column('cart', 'prod_name')
    op.add_column('user', sa.Column('item_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'item_count')
    op.add_column('cart', sa.Column('prod_name', sa.VARCHAR(length=64), nullable=True))
    op.add_column('cart', sa.Column('prod_desc', sa.VARCHAR(length=140), nullable=True))
    op.add_column('cart', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.add_column('cart', sa.Column('prod_cost', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'cart', type_='foreignkey')
    # ### end Alembic commands ###