"""products table

Revision ID: b30ce1171494
Revises: 
Create Date: 2020-09-06 12:15:20.586079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b30ce1171494'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('brand', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('in_stock_quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_brand'), 'product', ['brand'], unique=False)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_brand'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###
