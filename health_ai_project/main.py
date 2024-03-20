from flask import Flask, render_template, request
from static.constantes.SELECT_OPTION import BIRADS_USG, BIRADS_MAMOGRAFIA

app = Flask(__name__,  template_folder="templates")

@app.route("/", methods=['GET'])
def index():
    return render_template("tela_consulta.html", BIRADS_USG = BIRADS_USG, BIRADS_MAMOGRAFIA = BIRADS_MAMOGRAFIA)
 
app.run(debug=True)
