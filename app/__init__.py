from typing import Dict
from flask import Flask
from app.extensions import db


def create_app(config: Dict[str, str] = {}) -> Flask:
    '''
    Cria e retorna uma instância da classe Flask. Dessa forma, é possível criar
    instâncias com parâmetros diferentes para cada tipo de ambiente de
    desenvolvimento, isto é, dev, teste, QA e produção.

    :param config: Dicionário com configurações personalizadas.
    :type config: Dict[str, str]
    :return: flask.Flask
    '''
    app = Flask(__name__ , instance_relative_config=True)

    app.config.from_object('config.settings')

    if config:
        app.config.update(config)

    load_extensions(app)

    @app.route('/')
    def home():
        return 'API running'

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
