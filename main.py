from flask import Flask
from flask import render_template
from flask import url_for
import pydoc


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/menuEstudiantes")
def menu():
    return render_template("MenuEstudiantes.html")


@app.route("/registro")
def resgistrar():
    return render_template("Registro.html")


@app.route("/ingresar")
def ingresar():
    return render_template("Ingresar.html")


# Entry point
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)