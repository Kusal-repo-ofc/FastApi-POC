"""Create post table

Revision ID: b1ab0fae9727
Revises: 
Create Date: 2026-06-04 15:05:45.636485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1ab0fae9727'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op. create_table('posts', sa. Column('id', sa. Integer(), nullable=False,
                     primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
