"""first migration

Revision ID: 1ad8012fafa0
Revises: 
Create Date: 2023-05-21 14:48:52.387894

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.engine import Inspector

# revision identifiers, used by Alembic.
revision = '1ad8012fafa0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()

    if 'chapterfile' not in tables:
        op.create_table('chapterfile',
        sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('file_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('file_unique_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('cbz_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('cbz_unique_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('telegraph_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint('url')
        )

    if 'lastchapter' not in tables:
        op.create_table('lastchapter',
        sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('chapter_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint('url')
        )

    if 'manganame' not in tables:
        op.create_table('manganame',
        sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint('url')
        )

    if 'mangaoutput' not in tables:
        op.create_table('mangaoutput',
        sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('output', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('user_id')
        )

    if 'subscription' not in tables:
        op.create_table('subscription',
        sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint('url', 'user_id')
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscription')
    op.drop_table('mangaoutput')
    op.drop_table('manganame')
    op.drop_table('lastchapter')
    op.drop_table('chapterfile')
    # ### end Alembic commands ###
