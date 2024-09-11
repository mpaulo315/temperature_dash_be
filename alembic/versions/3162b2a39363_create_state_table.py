"""Create state table

Revision ID: 3162b2a39363
Revises: c5d37f206df3
Create Date: 2024-09-10 22:51:59.418981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3162b2a39363'
down_revision: Union[str, None] = 'c5d37f206df3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'state',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(30), nullable=False),
        sa.Column('country_id', sa.Integer, sa.ForeignKey('country.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('state')
