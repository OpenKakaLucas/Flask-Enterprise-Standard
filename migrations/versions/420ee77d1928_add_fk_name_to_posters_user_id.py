"""add fk name to posters.user_id

Revision ID: 420ee77d1928
Revises:
Create Date: 2026-02-04 11:53:33.893251

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "420ee77d1928"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # SQLite 下：只在 posters 表上显式创建 FK
    with op.batch_alter_table("posters") as batch_op:
        batch_op.create_foreign_key(
            "fk_posters_user_id_users", "users", ["user_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table("posters") as batch_op:
        batch_op.drop_constraint("fk_posters_user_id_users", type_="foreignkey")
    # ### end Alembic commands ###
