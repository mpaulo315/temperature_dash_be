"""Create global temperature fate table

Revision ID: beabcd2c2c95
Revises: 7646e91dd8a5
Create Date: 2024-09-11 08:33:46.832027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'beabcd2c2c95'
down_revision: Union[str, None] = '7646e91dd8a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'global_temperature',
        sa.Column("land_avg_temperature",sa.Float),
        sa.Column("land_avg_temperature_uncertainty",sa.Float),
        sa.Column("land_max_temperature",sa.Float),
        sa.Column("land_max_temperature_uncertainty",sa.Float),
        sa.Column("land_min_temperature",sa.Float),
        sa.Column("land_min_temperature_uncertainty",sa.Float),
        sa.Column("land_ocean_avg_temperature",sa.Float),
        sa.Column("land_ocean_avg_temperature_uncertainty",sa.Float),
        sa.Column("date",sa.Date, sa.ForeignKey('date.date'), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('global_temperature')
