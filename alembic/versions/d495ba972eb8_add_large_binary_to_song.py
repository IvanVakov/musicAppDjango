"""add large binary to song

Revision ID: d495ba972eb8
Revises: cdd6a91562fd
Create Date: 2023-12-17 14:28:56.628230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd495ba972eb8'
down_revision: Union[str, None] = 'cdd6a91562fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('music_file_data', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songs', 'music_file_data')
    # ### end Alembic commands ###
