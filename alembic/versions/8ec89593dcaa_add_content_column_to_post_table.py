"""add content column to post table

Revision ID: 8ec89593dcaa
Revises: b1ab0fae9727
Create Date: 2026-06-04 15:10:38.103799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ec89593dcaa'
down_revision: Union[str, Sequence[str], None] = 'b1ab0fae9727'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
