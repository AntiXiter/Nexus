from flask import Blueprint
bp = Blueprint("ideas", __name__, url_prefix="/ideas")
from . import routes  # noqa
