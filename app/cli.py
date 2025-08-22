from __future__ import annotations
from flask.cli import with_appcontext
import click
from .extensions import db
from .models.usuario import Usuario

@click.command("criar-admin")
@with_appcontext
def criar_admin():
    """Cria usuário admin padrão."""
    email = "admin@local"
    if Usuario.query.filter_by(email=email).first():
        click.echo("Admin já existe.")
        return
    u = Usuario(email=email, nome="Admin", role="admin")
    u.definir_senha("admin123")
    db.session.add(u)
    db.session.commit()
    click.echo("Admin criado: admin@local / admin123")
