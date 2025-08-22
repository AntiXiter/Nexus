from __future__ import annotations
from datetime import datetime
from ..extensions import db

class Pensamento(db.Model):
    __tablename__ = "pensamentos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), index=True, nullable=False)
    titulo = db.Column(db.String(200))
    conteudo = db.Column(db.Text, nullable=False)
    tags = db.Column(db.ARRAY(db.String), default=list)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
