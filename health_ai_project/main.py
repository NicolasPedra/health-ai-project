import json
from flask import Flask, render_template, request
from static.constantes.select_option.SELECT_OPTION import BIRADS_USG, BIRADS_MAMOGRAFIA
from data_base.paciente.paciente_db import PacienteDB

app = Flask(__name__,  template_folder="templates")

@app.route("/", methods=['GET'])
def index():
    return render_template("consulta_paciente/consulta_paciente.html")

@app.route("/", methods=['POST'])
def index_post():
    prontuario = request.form['prontuario']
    paciente_db = PacienteDB()
    paciente = paciente_db.obter_dados_paciente(prontuario)
    return render_template("/dados_paciente/dados_paciente.html", paciente = paciente, BIRADS_USG = BIRADS_USG, BIRADS_MAMOGRAFIA = BIRADS_MAMOGRAFIA)

@app.route("/dados_paciente", methods=['GET'])
def dados_paciente():
    return render_template("/dados_paciente/dados_paciente.html", BIRADS_USG = BIRADS_USG, BIRADS_MAMOGRAFIA = BIRADS_MAMOGRAFIA)
 
app.run(debug=True)
