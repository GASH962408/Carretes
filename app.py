# app.py
from flask import Flask, render_template, request
from logic import buscar_carrete

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        piezometro_id = int(request.form["piezometro_id"])
        cable_requerido = int(request.form["cable_requerido"])
        costo_por_metro = float(request.form["costo_por_metro"])
        
        result = buscar_carrete(piezometro_id, cable_requerido, costo_por_metro)
        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
