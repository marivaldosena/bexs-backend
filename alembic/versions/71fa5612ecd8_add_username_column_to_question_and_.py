"""Add username column to question and answer tables

Revision ID: 71fa5612ecd8
Revises: 8ac0acd78f1c
Create Date: 2020-05-14 23:10:19.197287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71fa5612ecd8'
down_revision = '8ac0acd78f1c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('questions', sa.Column('username', sa.String(length=120)))
    op.add_column('answers', sa.Column('username', sa.String(length=120)))

def downgrade():
    op.drop_column('answers', 'username')
    op.drop_column('questions', 'username')
