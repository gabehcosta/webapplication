from flask import Flask, render_template
from uuid import uuid4

app = Flask(__name__)

jogadores = [
    {'nome':'Neymar JR', 'posicao':'Atacante', 'idade':30, 'clube':'PSG'},
    {'nome':'Weverton', 'posicao':'Goleiro', 'idade':34, 'clube':'Palmeiras'},
    {'nome':'Gabriel Jejum', 'posicao':'Atacante', 'idade':25, 'clube':'Manchester City'}
]

@app.route('/')
def index():
    return render_template('index.html', jogadores=jogadores)

@app.route('/cadastro-jogador')
def cadastro():
    return render_template('cadastro-jogador.html')


app.run(debug=True)