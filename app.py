from flask import Flask, render_template, request
from carrete import buscar_carrete  # Importa la función buscar_carrete

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    if request.method == "POST":
        piezometro_id = int(request.form["piezometro_id"])
        cable_requerido = int(request.form["cable_requerido"])
        costo_por_metro = float(request.form["costo_por_metro"])

        # Llamar a la función buscar_carrete para obtener los resultados
        resultados = buscar_carrete(piezometro_id, cable_requerido, costo_por_metro)

    return render_template("home.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
