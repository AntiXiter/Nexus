from __future__ import annotations
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from ..extensions import db, login_manager

class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    nome = db.Column(db.String(120), nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="user")
    plano_id = db.Column(db.Integer, db.ForeignKey("planos.id"))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    plano = db.relationship("Plano", back_populates="usuarios")

    def definir_senha(self, senha: str) -> None:
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha: str) -> bool:
        return check_password_hash(self.senha_hash, senha)

@login_manager.user_loader
def carregar_usuario(user_id: str):
    return Usuario.query.get(int(user_id))
