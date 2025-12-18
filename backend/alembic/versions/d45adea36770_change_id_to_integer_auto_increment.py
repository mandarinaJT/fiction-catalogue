"""Change id to Integer auto-increment

Revision ID: d45adea36770
Revises: 
Create Date: 2025-12-19 00:37:26.727274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd45adea36770'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.drop_table('Users')
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password', sa.String(length=255), nullable=False),
    )
    op.create_index('ix_Users_id', 'Users', ['id'], unique=False)
    

def downgrade() -> None:
    op.drop_table('Users')
    op.create_table(
        'Users',
        sa.Column('id', sa.String(length=255), primary_key=True, nullable=False),
        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
    )
    op.create_index('ix_Users_id', 'Users', ['id'], unique=False)
