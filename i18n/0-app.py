#!/usr/bin/env python3
"""
Application Flask basique
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Route principale qui affiche la page d'accueil"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
