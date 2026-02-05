from flask import Blueprint

auth_bp = Blueprint("auth", __name__)
message_bp = Blueprint("message", __name__)
health_bp = Blueprint("health", __name__)
poster_bp = Blueprint("poster", __name__)

from . import auth  # noqa: E402, F401
from . import message  # noqa: E402, F401
from . import health  # noqa: E402, F401
from . import poster  # noqa: E402, F401
