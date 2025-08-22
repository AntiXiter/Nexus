from __future__ import annotations
from datetime import datetime
from ..extensions import db

class Ideia(db.Model):
    __tablename__ = "ideias"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), index=True, nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text)
    status = db.Column(db.String(50), default="rascunho")  # rascunho, em_progresso, concluida
    prioridade = db.Column(db.Integer, default=2)          # 1 alta, 2 média, 3 baixa
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
