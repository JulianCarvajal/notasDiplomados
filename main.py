from flask import Flask
from flask import render_template, request
from flask import url_for
import os
import pyodbc


app = Flask(__name__)
pasword = str(input("Ingrese la clave del super usuario "))
def get_db_connection(pasword):
    server = '(localdb)\MSSQLLocalDB'
    sapassword=pasword
    print(sapassword)
    basesdatos= 'Dimplomados'
    user = 'sa'
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server+';DATABASE='+basesdatos+ ';UID='+user+';PWD='+sapassword)
    return conexion

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        n_ID = request.form.get('comment1')
        password = request.form.get('comment2')
        print(n_ID)
        conexion=get_db_connection(pasword)
        crs=conexion.cursor()
        crs.execute("Select * FROM Usuarios WHERE Cedula='{}' AND Cod_Usuario='{}'".format(n_ID, password))
        rows=crs.fetchall()
        if len(rows)!=0:
            print(rows)
            for row in rows:
                nombres=row.Nombres +" "+ row.Apellidos
                cedula=row.Cedula
                email=row.Email
                celular=row.Tel
                Dip=row.Cod_Dip
                crs.execute("Select * FROM Cursos WHERE Cod_Dip='{}'".format(Dip))
                rows=crs.fetchall()
                for row in rows:
                        diplomado=row.Name
            return render_template('userProfile.html', nombres=nombres, cedula=cedula, email=email, celular=celular, diplomado=diplomado)
        if len(rows)==0:   
            print("Jajajaj")
            return render_template("index.html")

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