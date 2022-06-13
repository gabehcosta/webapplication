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

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    posicao = request.form['posicao']
    idade = request.form['idade']
    clube = request.form['clube']

    jogadores.append({'id':uuid4(), 'nome':nome, 'posicao':posicao, 'idade':idade, 'clube':clube})
    return redirect(url_for('index'))

@app.route('/excluir/<id>')
def excluir(id):
    for jogador in jogadores:
        if str(jogador['id']) == str(id):
            jogadores.remove(jogador)

    return render_template('index.html', jogadores=jogadores)

@app.route('/editar/<id>')
def editar(id):
    for jogador in jogadores:
        if str(jogador['id']) == str(id):
            jogador_escolhido = jogador

    return render_template('edicao-jogador.html', jogador=jogador_escolhido)
    
    

@app.route('/salvar-edicao', methods=['POST'])
def salvar_edicao():
    id_editado = request.form['id_edicao']
    nome_editado = request.form['nome_edicao']
    posicao_editado = request.form['posicao_edicao']
    idade_editado = request.form['idade_edicao']
    clube_editado = request.form['clube_edicao']

    for jogador in jogadores:
        if str(jogador['id']) == str(id_editado):
            jogador['nome'] = nome_editado
            jogador['posicao'] = posicao_editado
            jogador['idade'] = idade_editado
            jogador['clube'] = clube_editado

    return redirect(url_for('index'))




app.run(debug=True)