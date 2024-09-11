"""Create city temperature fate table

Revision ID: 510eb056954f
Revises: 957b05626b08
Create Date: 2024-09-11 08:59:31.587322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '510eb056954f'
down_revision: Union[str, None] = '957b05626b08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'city_temperature',
        sa.Column("avg_temperature",sa.Float, nullable=False),  
        sa.Column("avg_temperature_uncertainty",sa.Float),
        sa.Column("date",sa.Date, sa.ForeignKey('date.date'), nullable=False),
        sa.Column("city_id",sa.Integer, sa.ForeignKey('city.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('city_temperature')
