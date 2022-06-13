from flask import Flask, render_template, request, redirect, url_for
from uuid import uuid4

app = Flask(__name__)

jogadores = [
    {'id':uuid4(), 'nome':'Neymar JR', 'posicao':'Atacante', 'idade':30, 'clube':'PSG'},
    {'id':uuid4(), 'nome':'Weverton', 'posicao':'Goleiro', 'idade':34, 'clube':'Palmeiras'},
    {'id':uuid4(), 'nome':'Gabriel Jejum', 'posicao':'Atacante', 'idade':25, 'clube':'Manchester City'}
]

@app.route('/')
def index():
    return render_template('index.html', jogadores=jogadores)

@app.route('/cadastro-jogador')
def cadastro():
    return render_template('cadastro-jogador.html')

@app.route('/salvar', methods=['post'])
def salvar():
    nome = request.form['nome']
    posicao = request.form['posicao']
    idade = request.form['idade']
    clube = request.form['clube']

    jogadores.append({'id':uuid4(), 'nome':nome, 'posicao':posicao, 'idade':idade, 'clube':clube})
    return redirect(url_for('index'))

# @app.route('')

app.run(debug=True)