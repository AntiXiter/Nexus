from __future__ import annotations
from datetime import datetime
from ..extensions import db

class Foto(db.Model):
    __tablename__ = "fotos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(
        db.Integer, db.ForeignKey("usuarios.id"), index=True, nullable=False
    )
    caminho = db.Column(db.String(500), nullable=False)
    legenda = db.Column(db.String(255))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
