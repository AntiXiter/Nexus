from __future__ import annotations
from app import criar_app
from app.extensions import db
from app.models.usuario import Usuario

app = criar_app()

@app.cli.command("criar-admin")
def criar_admin():
    """Cria usuário admin padrão (use: flask criar-admin)."""
    email = "admin@local"
    if Usuario.query.filter_by(email=email).first():
        print("Admin já existe.")
        return
    u = Usuario(email=email, nome="Admin", role="admin")
    u.definir_senha("admin123")
    db.session.add(u)
    db.session.commit()
    print("Admin criado: admin@local / admin123")
