from __future__ import annotations
from ..extensions import db

class Plano(db.Model):
    __tablename__ = "planos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    limite_armazenamento_mb = db.Column(db.Integer, default=1024)
    recursos = db.Column(db.JSON, default={})
    usuarios = db.relationship("Usuario", back_populates="plano")
