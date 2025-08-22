from __future__ import annotations
import os
from flask import Flask
from dotenv import load_dotenv
from .config import carregar_config
from .extensions import db, migrate, login_manager, csrf, cache, limiter

def criar_app() -> Flask:
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(carregar_config())

    # extensões
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    # modelos (side-effect para mapeamento)
    from .models import usuario, plano, arquivo, pensamento, foto, transacao, ideia  # noqa

    # blueprints
    from .blueprints.auth import bp as auth_bp
    from .blueprints.dashboard import bp as dashboard_bp
    from .blueprints.files import bp as files_bp
    from .blueprints.thoughts import bp as thoughts_bp
    from .blueprints.photos import bp as photos_bp
    from .blueprints.finance import bp as finance_bp
    from .blueprints.ideas import bp as ideas_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(files_bp)
    app.register_blueprint(thoughts_bp)
    app.register_blueprint(photos_bp)
    app.register_blueprint(finance_bp)
    app.register_blueprint(ideas_bp)

    login_manager.login_view = "auth.login"

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # comandos CLI
    from .cli import criar_admin
    app.cli.add_command(criar_admin)

    return app
