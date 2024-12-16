from flask import Flask, render_template
from data import obtener_datos  # Importar la función que obtiene los datos

app = Flask(__name__)

@app.route('/')
def home():
    # Obtener los datos
    datos = obtener_datos()  # Aquí obtenemos los datos
    piezometros = datos["piezometros"]  # Extraemos la lista de piezómetros

    # Pasamos la lista de piezómetros al template
    return render_template('home.html', piezometros=piezometros)

if __name__ == '__main__':
    app.run(debug=True)
