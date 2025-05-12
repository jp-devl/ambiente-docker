from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
            'datahora': datetime.datetime.now(),
            'nome': 'Teste',
            'disciplina': 'Sistemas Operacionais'
    }

    return jsonify(data)