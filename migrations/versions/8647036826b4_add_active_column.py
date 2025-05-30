"""Add active column

Revision ID: 8647036826b4
Revises: 18f83b8065c3
Create Date: 2025-05-23 17:18:50.092384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8647036826b4'
down_revision = '18f83b8065c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###
