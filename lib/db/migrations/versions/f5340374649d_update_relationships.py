"""Update relationships

Revision ID: f5340374649d
Revises: 
Create Date: 2023-08-29 02:09:10.313948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5340374649d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('user_username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('game',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_username', sa.String(), nullable=True),
    sa.Column('game_difficulty', sa.String(), nullable=True),
    sa.Column('game_outcome', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_username'], ['users.user_username'], ),
    sa.PrimaryKeyConstraint('game_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    op.drop_table('users')
    # ### end Alembic commands ###
