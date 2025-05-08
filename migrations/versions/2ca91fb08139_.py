"""empty message

Revision ID: 2ca91fb08139
Revises: 
Create Date: 2025-05-08 20:17:44.664462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ca91fb08139'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('media_posts_id_fkey', 'media', type_='foreignkey')
    op.drop_table('post')
    
def downgrade():
    op.create_table('post', ...)
    op.create_foreign_key('media_posts_id_fkey', 'media', 'post', ['post_id'], ['id'])
