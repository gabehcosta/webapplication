from flask import Flask, render_template, request, redirect, url_for
from uuid import uuid4
from os.path import exists
import csv
app = Flask(__name__)

jogadores = []

if not exists('jogadores.csv'):
    with open('jogadores.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'nome', 'posicao', 'idade', 'clube']) 
        escritor.writeheader()
        escritor.writerows(jogadores)
else:
    with open('jogadores.csv', 'rt') as file_in:
        leitor = csv.DictReader(file_in)
        jogadores = []
        for linha in leitor:
            jogador = dict(linha)
            jogadores.append(jogador)


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

    jogadores.append({'id':uuid4(), 'nome':nome.title(), 'posicao':posicao.title(), 'idade':idade, 'clube':clube.title()})

    with open('jogadores.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'nome', 'posicao', 'idade', 'clube']) 
        escritor.writeheader()
        escritor.writerows(jogadores)
    
    return redirect(url_for('index'))


@app.route('/excluir/<id>')
def excluir(id):
    for jogador in jogadores:
        if str(jogador['id']) == str(id):
            jogadores.remove(jogador)
    
    with open('jogadores.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'nome', 'posicao', 'idade', 'clube']) 
        escritor.writeheader()
        escritor.writerows(jogadores)

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
            jogador['nome'] = nome_editado.title()
            jogador['posicao'] = posicao_editado.title()
            jogador['idade'] = idade_editado
            jogador['clube'] = clube_editado.title()

    with open('jogadores.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'nome', 'posicao', 'idade', 'clube']) 
        escritor.writeheader()
        escritor.writerows(jogadores)

    return redirect(url_for('index'))


app.run()