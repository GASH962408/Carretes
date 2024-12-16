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

    # Solicitar el costo por metro de cable en USD
    costo_por_metro = float(input("Ingresar costo en USD por metro: "))
    if costo_por_metro <= 0:
        print("Por favor, ingrese un costo válido por metro.")
        return

    # Opción 1: Usar un solo carrete (con merma >= 30)
    carretes = sorted(datos["carretes"].items(), key=lambda x: x[1])  # Ordenar de menor a mayor
    carrete_ideal_1 = None

    for carrete_id, longitud in carretes:
        merma = round(longitud - cable_requerido, 2)
        if longitud >= cable_requerido and merma >= 30:
            carrete_ideal_1 = (carrete_id, longitud, merma)
            break

    # Opción 2: Usar dos carretes (dividir la cantidad por la mitad)
    mitad_cable_requerido = cable_requerido / 2
    carretes_ideal_2 = []
    carretes_usados_2 = set()  # Para registrar los carretes ya usados

    for _ in range(2):
        for carrete_id, longitud in carretes:
            if carrete_id not in carretes_usados_2:  # Verificar que el carrete no haya sido usado
                merma = round(longitud - mitad_cable_requerido, 2)
                if longitud >= mitad_cable_requerido and merma >= 0:
                    carretes_ideal_2.append((carrete_id, longitud, merma))
                    carretes_usados_2.add(carrete_id)  # Marcar el carrete como usado
                    break

    # Opción 3: Usar tres carretes (dividir la cantidad por tres)
    tercio_cable_requerido = cable_requerido / 3
    carretes_ideal_3 = []
    carretes_usados_3 = set()  # Para registrar los carretes ya usados

    for _ in range(3):
        for carrete_id, longitud in carretes:
            if carrete_id not in carretes_usados_3:  # Verificar que el carrete no haya sido usado
                merma = round(longitud - tercio_cable_requerido, 2)
                if longitud >= tercio_cable_requerido and merma >= 0:
                    carretes_ideal_3.append((carrete_id, longitud, merma))
                    carretes_usados_3.add(carrete_id)  # Marcar el carrete como usado
                    break

    # Mostrar los resultados

    if carrete_ideal_1:
        carrete_id, longitud_carrete, merma = carrete_ideal_1
        costo_1 = round(cable_requerido * costo_por_metro, 2)
        print(f"Opción 1: Usar 1 carrete: El carrete {carrete_id} puede cumplir con el requerimiento. Tiene {longitud_carrete} metros disponibles.")
        print(f"Merma después de usar el carrete: {merma} metros.")
        print(f"Costo total: ${costo_1} USD.")

    else:
        print(f"Opción 1: No es posible cumplir con el requerimiento de {cable_requerido} metros usando un solo carrete con merma mayor a 30 metros.")

    if carretes_ideal_2:
        print(f"\nOpción 2: Usar 2 carretes:")
        costo_2 = round(cable_requerido * costo_por_metro + 15, 2)  # Añadir el costo del empalme
        for carrete_id, longitud_carrete, merma in carretes_ideal_2:
            print(f"Carrete {carrete_id} puede cumplir con la mitad del requerimiento. Tiene {longitud_carrete} metros disponibles.")
            print(f"Merma después de usar el carrete: {merma} metros.")
        print(f"Costo total: ${costo_2} USD.")

    else:
        print(f"\nOpción 2: No es posible cumplir con el requerimiento de {cable_requerido} metros usando dos carretes.")

    if carretes_ideal_3:
        print(f"\nOpción 3: Usar 3 carretes:")
        costo_3 = round(cable_requerido * costo_por_metro + 30, 2)  # Añadir el costo del empalme
        for carrete_id, longitud_carrete, merma in carretes_ideal_3:
            print(f"Carrete {carrete_id} puede cumplir con un tercio del requerimiento. Tiene {longitud_carrete} metros disponibles.")
            print(f"Merma después de usar el carrete: {merma} metros.")
        print(f"Costo total: ${costo_3} USD.")

    else:
        print(f"\nOpción 3: No es posible cumplir con el requerimiento de {cable_requerido} metros usando tres carretes.")


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
