from flask import Flask, render_template
from uuid import uuid4

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro-jogador')
def cadastro():
    return render_template('cadastro-jogador.html')


app.run(debug=True)