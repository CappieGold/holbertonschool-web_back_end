#!/usr/bin/env python3
"""
Application Flask avec Babel pour l'internationalisation
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Classe de configuration pour l'application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """Route principale qui affiche la page d'accueil"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
