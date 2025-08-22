from __future__ import annotations
from flask import render_template
from flask_login import login_required
from . import bp

@bp.get("/")
@login_required
def index():
    return render_template("dashboard/index.html")
