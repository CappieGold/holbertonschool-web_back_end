#!/usr/bin/env python3
"""
Application Flask avec sélection automatique de locale
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Classe de configuration pour l'application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Détermine la meilleure langue à utiliser pour l'utilisateur
    basée sur les langues acceptées par le navigateur
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route principale qui affiche la page d'accueil"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
