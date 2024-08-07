"""create squeeze table

Revision ID: 085de908c797
Revises: 70dab65f6844
Create Date: 2024-08-01 00:05:04.351726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '085de908c797'
down_revision: Union[str, None] = '70dab65f6844'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('squeezes',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('url_slug', sa.String(), nullable=True),
    sa.Column('headline', sa.String(), nullable=True),
    sa.Column('sub_headline', sa.String(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('online', 'offline', name='squeezestatusenum'), nullable=True),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_squeezes_id'), 'squeezes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_squeezes_id'), table_name='squeezes')
    op.drop_table('squeezes')
    # ### end Alembic commands ###
