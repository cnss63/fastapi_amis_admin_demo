"""add url

Revision ID: bcd68ae939ea
Revises: c79e1785119e
Create Date: 2022-01-23 20:19:53.488209

"""
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd68ae939ea'
down_revision = 'c79e1785119e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('source', sqlmodel.sql.sqltypes.AutoString(length=200), nullable=True))
    op.drop_index('ix_article_category_id', table_name='article')
    op.drop_index('ix_article_content', table_name='article')
    op.drop_index('ix_article_create_time', table_name='article')
    op.drop_index('ix_article_description', table_name='article')
    op.drop_index('ix_article_id', table_name='article')
    op.drop_index('ix_article_img', table_name='article')
    op.drop_index('ix_article_status', table_name='article')
    op.drop_index('ix_article_title', table_name='article')
    op.drop_index('ix_articletaglink_article_id', table_name='articletaglink')
    op.drop_index('ix_articletaglink_tag_id', table_name='articletaglink')
    op.drop_index('ix_category_description', table_name='category')
    op.drop_index('ix_category_id', table_name='category')
    op.drop_index('ix_category_status', table_name='category')
    op.drop_index('ix_tag_id', table_name='tag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_tag_id', 'tag', ['id'], unique=False)
    op.create_index('ix_category_status', 'category', ['status'], unique=False)
    op.create_index('ix_category_id', 'category', ['id'], unique=False)
    op.create_index('ix_category_description', 'category', ['description'], unique=False)
    op.create_index('ix_articletaglink_tag_id', 'articletaglink', ['tag_id'], unique=False)
    op.create_index('ix_articletaglink_article_id', 'articletaglink', ['article_id'], unique=False)
    op.create_index('ix_article_title', 'article', ['title'], unique=False)
    op.create_index('ix_article_status', 'article', ['status'], unique=False)
    op.create_index('ix_article_img', 'article', ['img'], unique=False)
    op.create_index('ix_article_id', 'article', ['id'], unique=False)
    op.create_index('ix_article_description', 'article', ['description'], unique=False)
    op.create_index('ix_article_create_time', 'article', ['create_time'], unique=False)
    op.create_index('ix_article_content', 'article', ['content'], unique=False)
    op.create_index('ix_article_category_id', 'article', ['category_id'], unique=False)
    op.drop_column('article', 'source')
    # ### end Alembic commands ###
