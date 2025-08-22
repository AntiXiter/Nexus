from __future__ import annotations
from datetime import date, datetime
from ..extensions import db

class TransacaoFinanceira(db.Model):
    __tablename__ = "transacoes_financeiras"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), index=True, nullable=False)
    data = db.Column(db.Date, default=date.today, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), index=True)
    valor = db.Column(db.Numeric(12, 2), nullable=False)  # positivo=receita / negativo=despesa
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
