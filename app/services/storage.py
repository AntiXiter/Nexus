from __future__ import annotations
import os
from werkzeug.utils import secure_filename
from flask import current_app

EXTENSOES_PERMITIDAS = {"txt","pdf","png","jpg","jpeg","gif","csv","xlsx","docx"}

def extensao_permitida(nome_arquivo: str) -> bool:
    return "." in nome_arquivo and nome_arquivo.rsplit(".", 1)[1].lower() in EXTENSOES_PERMITIDAS

def salvar_arquivo(arquivo, subpasta: str = "") -> str:
    if not arquivo or arquivo.filename == "":
        raise ValueError("Arquivo inválido.")
    if not extensao_permitida(arquivo.filename):
        raise ValueError("Extensão não permitida.")
    nome_seguro = secure_filename(arquivo.filename)
    destino_base = os.path.join(current_app.config["UPLOAD_FOLDER"], subpasta)
    os.makedirs(destino_base, exist_ok=True)
    destino = os.path.join(destino_base, nome_seguro)
    arquivo.save(destino)
    return destino
