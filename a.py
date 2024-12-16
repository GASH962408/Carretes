def buscar_carrete(datos):
    # Solicitar el número del piezómetro
    piezometro_id = int(input("Ingresar número de piezómetro: "))
    piezometro = next((p for p in datos["piezometros"] if p["ID"] == piezometro_id), None)
    if not piezometro:
        print("El piezómetro ingresado no existe.")
        return

    # Solicitar la cantidad de cable requerida
    cable_requerido = int(input("Ingresar cantidad de cable requerida (en metros): "))
    if cable_requerido <= 0:
        print("Por favor, ingrese una cantidad válida de cable.")
        return

    # Buscar el carrete más adecuado (el inmediato superior)
    carretes = sorted(datos["carretes"].items(), key=lambda x: x[1])  # Ordenar de menor a mayor
    carrete_ideal = None

    for carrete_id, longitud in carretes:
        if longitud >= cable_requerido:
            carrete_ideal = (carrete_id, longitud)
            break

    if not carrete_ideal:
        print(f"No es posible cumplir con el requerimiento de {cable_requerido} metros usando un solo carrete.")
    else:
        carrete_id, longitud_carrete = carrete_ideal
        merma = longitud_carrete - cable_requerido
        print(f"Para 1 carrete : El carrete {carrete_id} puede cumplir con el requerimiento. Tiene {longitud_carrete} metros disponibles.")
        print(f"Merma después de usar el carrete: {merma} metros.")


# Datos
datos = {
    "piezometros": [
        {"ID": 1, "Nombre": "PP20-S18-03"},
        {"ID": 2, "Nombre": "PP23-S1-P24A"},
        {"ID": 3, "Nombre": "PP23-S1-P24B"},
        {"ID": 4, "Nombre": "PP20-S17-02A"},
        {"ID": 5, "Nombre": "PP20-S17-02C"},
        {"ID": 6, "Nombre": "PP20-S17-02B"},
        {"ID": 7, "Nombre": "PP21-CV5"},
        {"ID": 8, "Nombre": "PP22-S5-P17A"},
        {"ID": 9, "Nombre": "PP22-S5-P17B"},
        {"ID": 10, "Nombre": "PP22-S5-P17C"},
        {"ID": 11, "Nombre": "PP21-S5-PP17-33-01A"},
        {"ID": 12, "Nombre": "PP21-S5-PP17-33-01B"},
        {"ID": 13, "Nombre": "PP23-CV7"},
        {"ID": 14, "Nombre": "PP20-S34-01"},
        {"ID": 15, "Nombre": "PP22-S33-02"},
        {"ID": 16, "Nombre": "PP23-S33-03A"},
        {"ID": 17, "Nombre": "PP23-S33-03B"},
        {"ID": 18, "Nombre": "PP23-S32-03A"},
        {"ID": 19, "Nombre": "PP23-S32-03B"},
        {"ID": 20, "Nombre": "PP23-S32-02A"},
        {"ID": 21, "Nombre": "PP23-S32-02B"},
        {"ID": 22, "Nombre": "PP22-S32-1"},
        {"ID": 23, "Nombre": "PP22-S33-01"},
        {"ID": 24, "Nombre": "PP23-S31-02A"},
        {"ID": 25, "Nombre": "PP23-S31-01A"},
        {"ID": 26, "Nombre": "PP23-S31-01B"}
    ],
    "carretes": {
        "1": 478, "2": 479, "3": 674, "4": 446, "5": 824, "6": 821, "7": 740, "8": 156,
        "9": 128, "10": 513, "11": 680, "12": 502, "13": 1100, "14": 439, "15": 239,
        "16": 1100, "17": 1500, "18": 2438, "19": 2438, "20": 248, "21": 90, "22": 63,
        "23": 29, "24": 17, "25": 29, "26": 40, "27": 43, "28": 16, "29": 18, "30": 29,
        "31": 16, "32": 13, "33": 15, "34": 186, "35": 283, "36": 328, "37": 246
    }
}

# Llamar a la función
buscar_carrete(datos)
