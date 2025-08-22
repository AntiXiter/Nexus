from flask import Blueprint
bp = Blueprint("thoughts", __name__, url_prefix="/thoughts")
from . import routes  # noqa
