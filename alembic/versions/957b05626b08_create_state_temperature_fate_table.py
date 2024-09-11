"""Create state temperature fate table

Revision ID: 957b05626b08
Revises: 162914f6fe27
Create Date: 2024-09-11 08:47:24.254983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '957b05626b08'
down_revision: Union[str, None] = '162914f6fe27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'state_temperature',
        sa.Column("land_avg_temperature",sa.Float),
        sa.Column("date",sa.Date, sa.ForeignKey('date.date'), nullable=False),
        sa.Column("state_id",sa.Integer, sa.ForeignKey('state.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('state_temperature')
