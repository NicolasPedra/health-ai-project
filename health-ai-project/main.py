from flask import Flask, render_template, request

app = Flask(__name__,  template_folder="templates")

@app.route("/", methods=['GET'])
def index():
    return render_template("tela-consulta.html" )
 
app.run(debug=True)
