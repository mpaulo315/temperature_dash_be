"""Create city table

Revision ID: 7646e91dd8a5
Revises: 3162b2a39363
Create Date: 2024-09-10 22:52:10.078276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7646e91dd8a5'
down_revision: Union[str, None] = '3162b2a39363'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'city',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('country_id', sa.Integer, sa.ForeignKey('country.id'), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('latitude', sa.Float(), sa.CheckConstraint("latitude>=-90 AND latitude<=90")),
        sa.Column('longitude', sa.Float(), sa.CheckConstraint("longitude>=-180 AND longitude<=180")),
        sa.Column('isMajorCity', sa.Boolean, default=False)       
    )


def downgrade() -> None:
    op.drop_table('city')
