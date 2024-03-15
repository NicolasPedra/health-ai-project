from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/" , methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        teste = ''
        return render_template("tela-consulta.html")
    else:
        return render_template("tela-consulta.html", **locals())
 
app.run(debug=True)
