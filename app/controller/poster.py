from app.controller import poster_bp
from app.exceptions.base import BusinessError
from app.services.poster import create_poster
from app.utils.validators import validate_json_content_type, login_required
from flask import g
from app.utils import success, error
from app.schemas.poster import Poster
from app.utils.validators import validate_request


@poster_bp.route("/add", methods=["POST"])
@validate_json_content_type()
@validate_request(Poster)
@login_required()
def add():
    try:
        data = g.validated_data
        result = create_poster(data)
        return success(result)
    except BusinessError as e:
        return error(code="400", message=str(e))
    except Exception as e:
        raise
