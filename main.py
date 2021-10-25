from flask import Flask
from flask import render_template
import pyodbc


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/menuEstudiantes")
def ingresar():
    return render_template("menuEstudiantes.html")


@app.route("/registro")
def ingresar():
    return render_template("registro.html")


@app.route("/ingresar")
def ingresar():
    return render_template("Ingresar.html")


# Entry point
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)