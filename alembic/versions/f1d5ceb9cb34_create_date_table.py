"""Create Date table

Revision ID: f1d5ceb9cb34
Revises: 
Create Date: 2024-09-10 12:51:48.802140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1d5ceb9cb34'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "date",
        sa.Column("date", sa.Date, primary_key=True)
    )

    op.execute(
        """
            ALTER TABLE date
            ADD COLUMN year SMALLINT GENERATED ALWAYS AS (DATE_PART('year', date)) STORED;
        """
    )
    op.execute(
        """
            ALTER TABLE date
            ADD COLUMN month SMALLINT GENERATED ALWAYS AS (DATE_PART('month', date)) STORED;
        """
    )
    op.execute(
        """
            ALTER TABLE date
            ADD COLUMN day SMALLINT GENERATED ALWAYS AS (DATE_PART('day', date)) STORED;
        """
    )


def downgrade() -> None:
    op.drop_table("date")
