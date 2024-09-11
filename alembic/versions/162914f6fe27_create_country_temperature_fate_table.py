"""Create country temperature fate table

Revision ID: 162914f6fe27
Revises: beabcd2c2c95
Create Date: 2024-09-11 08:38:43.270783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '162914f6fe27'
down_revision: Union[str, None] = 'beabcd2c2c95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'country_temperature',
        sa.Column("avg_temperature",sa.Float, nullable=False),  
        sa.Column("avg_temperature_uncertainty",sa.Float),
        sa.Column("date",sa.Date, sa.ForeignKey('date.date'), nullable=False),
        sa.Column("country_id",sa.Integer, sa.ForeignKey('country.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('country_temperature')
