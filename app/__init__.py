import os
import click
from typing import Dict
from flask import Flask, jsonify
from app.extensions import db
from flask.cli import with_appcontext
from app import seeds

from app.routes import (
    question_bp,
    answer_bp
)


def create_app(config: Dict[str, str] = {}) -> Flask:
    '''
    Cria e retorna uma instância da classe Flask. Dessa forma, é possível criar
    instâncias com parâmetros diferentes para cada tipo de ambiente de
    desenvolvimento, isto é, dev, teste, QA e produção.

    :param config: Dicionário com configurações personalizadas.
    :type config: Dict[str, str]
    :return: flask.Flask
    '''
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    if config:
        app.config.update(config)

    load_extensions(app)
    load_commands(app)

    V1_API = '/api/v1'

    # Questions Routes
    app.register_blueprint(question_bp, url_prefix=f'{V1_API}/question')
    app.register_blueprint(question_bp, url_prefix=f'{V1_API}/questions')

    # Answers Routes
    app.register_blueprint(answer_bp, url_prefix=f'{V1_API}/answer')
    app.register_blueprint(answer_bp, url_prefix=f'{V1_API}/answers')

    @app.after_request
    def configure_cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Methods'] = '*'

        return response

    @app.route('/')
    @app.route(f'{V1_API}/')
    def home():
        return jsonify({'status': 'API running'}), 200

    return app


def load_extensions(app: Flask) -> None:
    '''
    Carrega as bibliotecas de terceiros acopladas ao Flask.
    :param app: Instância da classe Flask.

    :type app: flask.Flask
    :return: None
    '''
    db.init_app(app)

    return None


def load_commands(app: Flask) -> None:
    def get_db_config():
        from alembic.config import Config as AlembicConfig
        INI_FILE = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'alembic.ini'))
        alembic_oonfig = AlembicConfig(INI_FILE)
        alembic_oonfig.set_main_option(
            'sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])

        return alembic_oonfig

    @app.cli.command('migrate')
    @with_appcontext
    def migrate():
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from alembic.command import upgrade as alembic_upgrade

        engine = create_engine(
            app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
        session_factory = sessionmaker(bind=engine)
        _db = {
            'engine': engine,
            'session_factory': session_factory,
        }

        alembic_upgrade(get_db_config(), 'head')

        session = _db['session_factory']()
        session.rollback()
        session.close()
        engine.dispose()

    @app.cli.command('drop-tables')
    @with_appcontext
    def drop_all():
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from alembic.command import downgrade as alembic_downgrade

        engine = create_engine(
            app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
        session_factory = sessionmaker(bind=engine)
        _db = {
            'engine': engine,
            'session_factory': session_factory,
        }

        alembic_downgrade(get_db_config(), 'base')

        session = _db['session_factory']()
        session.rollback()
        session.close()
        engine.dispose()

    @app.cli.command('test')
    @click.argument('coverage', default=False)
    @with_appcontext
    def test(coverage):
        import pytest

        commands = ['-s', './app/tests', '-p', 'no:warnings']

        if coverage:
            commands.extend(['--cov', './app'])

        pytest.main(commands)

    @app.cli.command('seed')
    @with_appcontext
    def seed():
        seeds.seed_all()
