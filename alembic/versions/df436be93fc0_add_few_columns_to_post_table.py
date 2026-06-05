"""add few columns to post table

Revision ID: df436be93fc0
Revises: 120f9be37825
Create Date: 2026-06-04 15:39:44.956444

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df436be93fc0'
down_revision: Union[str, Sequence[str], None] = '120f9be37825'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        'posts',
        sa.Column('published', sa.Boolean(), nullable=False,
                  server_default=sa.text('TRUE'))
    )

    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  nullable=False, server_default=sa.text('now()'))
    )

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
