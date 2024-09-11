"""Create country table

Revision ID: c5d37f206df3
Revises: f1d5ceb9cb34
Create Date: 2024-09-10 20:56:01.958360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5d37f206df3'
down_revision: Union[str, None] = 'f1d5ceb9cb34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'country',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(30), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('country')
