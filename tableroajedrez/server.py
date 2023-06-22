#ACTIVIDAD TABLERO DE AJEDREZ
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", methods=['GET'])
def tablero_ajedrez():
    num_filas = 8
    num_columnas = 8
    colores = [['white' if (fila+columna) % 2 == 0 else 'black' for columna in range(num_columnas)] for fila in range(num_filas)]
    return render_template("index.html", num_filas=num_filas, num_columnas=num_columnas, colores=colores)

@app.route("/<int:num_filas>", methods=['GET'])
def tablero_ajedrez_per1(num_filas):
    num_columnas = 8
    colores = [['white' if (fila+columna) % 2 == 0 else 'black' for columna in range(num_columnas)] for fila in range(num_filas)]
    return render_template("index.html", num_filas=num_filas, num_columnas=num_columnas, colores=colores)

@app.route("/<int:num_filas>/<int:num_columnas>", methods=['GET'])
def tablero_ajedrez_per2(num_filas, num_columnas):
    colores = [['white' if (fila+columna) % 2 == 0 else 'black' for columna in range(num_columnas)] for fila in range(num_filas)]
    return render_template("index.html", num_filas=num_filas, num_columnas=num_columnas, colores=colores)

@app.route("/<int:num_filas>/<int:num_columnas>/<color1>/<color2>", methods=['GET'])
def tablero_ajedrez_per3(num_filas, num_columnas, color1, color2):
    colores = [[color1 if (fila+columna) % 2 == 0 else color2 for columna in range(num_columnas)] for fila in range(num_filas)]
    return render_template("index.html", num_filas=num_filas, num_columnas=num_columnas, colores=colores, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True, port=5004)
