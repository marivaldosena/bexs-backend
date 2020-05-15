"""Create Question and Answer tables.

Revision ID: 8ac0acd78f1c
Revises: 
Create Date: 2020-05-14 11:10:35.688283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ac0acd78f1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.String(length=256), nullable=False),
        sa.Column('creationDate', sa.DateTime)
    )

    op.create_table(
        'answers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.Text, nullable=False),
        sa.Column('creationDate', sa.DateTime),
        sa.Column('question_id', sa.Integer, sa.ForeignKey('questions.id'), nullable=False)
    )


def downgrade():
    op.drop_table('answers')
    op.drop_table('questions')
