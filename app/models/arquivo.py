from __future__ import annotations
from datetime import datetime
from ..extensions import db

class Arquivo(db.Model):
    __tablename__ = "arquivos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), index=True, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    caminho = db.Column(db.String(500), nullable=False)
    tipo_mime = db.Column(db.String(120))
    tamanho_bytes = db.Column(db.Integer)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
