from __future__ import annotations
from flask import jsonify
from flask_login import login_required
from . import bp

@bp.get("/ping")
@login_required
def ping():
    return jsonify(msg="thoughts ok")
