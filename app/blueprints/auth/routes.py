from __future__ import annotations
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from ...extensions import db
from ...models.usuario import Usuario
from . import bp

@bp.get("/login")
def login():
    return render_template("auth/login.html")

@bp.post("/login")
def login_post():
    email = request.form.get("email", "").strip().lower()
    senha = request.form.get("senha", "")
    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not usuario.verificar_senha(senha):
        flash("Credenciais inválidas.", "danger")
        return redirect(url_for("auth.login"))
    login_user(usuario)
    return redirect(url_for("dashboard.index"))

@bp.get("/register")
def register():
    return render_template("auth/register.html")

@bp.post("/register")
def register_post():
    nome = request.form.get("nome", "").strip()
    email = request.form.get("email", "").strip().lower()
    senha = request.form.get("senha", "")
    if Usuario.query.filter_by(email=email).first():
        flash("E-mail já cadastrado.", "warning")
        return redirect(url_for("auth.register"))
    usuario = Usuario(nome=nome, email=email)
    usuario.definir_senha(senha)
    db.session.add(usuario)
    db.session.commit()
    flash("Registro efetuado! Faça login.", "success")
    return redirect(url_for("auth.login"))

@bp.get("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
