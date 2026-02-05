from app.exceptions.base import BusinessError
from app.models import Poster
from app.extensions.extensions import db
from flask import g


def create_poster(data):
    content = data.content.strip()
    title = data.title.strip()
    status = data.status
    user_id = g.user_id
    if not content:
        raise BusinessError("内容不能为空", code=400)
    if not title:
        raise BusinessError("标题不能为空", code=400)
    if status not in (4, 256):
        raise BusinessError("状态错误", code=400)
    poster = Poster(content=content, title=title, status=status, user_id=user_id)
    try:
        db.session.add(poster)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise BusinessError("新增失败", code=500)
    return {"id": poster.id}
