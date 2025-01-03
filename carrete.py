from data import obtener_datos  # Importamos la función obtener_datos

def buscar_carrete(piezometro_id, cable_requerido, costo_por_metro):
    datos = obtener_datos()  # Obtenemos los datos desde data.py

    # Buscar el piezómetro por su ID (en lugar de buscar por Nombre)
    piezometro = next((p for p in datos["piezometros"] if p["ID"] == piezometro_id), None)

    if not piezometro:
        print("El piezómetro ingresado no existe.")
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

    # Crear los resultados
    resultados = []
    
    if carrete_ideal_1:
        costo_1 = round(cable_requerido * costo_por_metro, 2)
        resultados.append({
            "opcion": "Opción : 1 carrete",
            "detalles": [
                f"El carrete {carrete_ideal_1[0]} puede cumplir con el requerimiento. Tiene {carrete_ideal_1[1]} metros disponibles.",
                f"Merma después de usar el carrete: {carrete_ideal_1[2]} metros."
            ],
            "costo_total": f"Costo total: ${costo_1} USD."  # Añadir la clave 'costo_total'
        })
    else:
        resultados.append({
            "opcion": f"Opción 1: No es posible cumplir con el requerimiento de {cable_requerido} metros usando un solo carrete con merma mayor a 30 metros."
        })

    if carretes_ideal_2:
        costo_2 = round(cable_requerido * costo_por_metro + 15, 2)  # Añadir el costo del empalme
        resultados.append({
            "opcion": "Opción : 2 carretes",
            "detalles": [
                f"Carrete {carretes_ideal_2[0][0]} puede cumplir con la mitad del requerimiento. Tiene {carretes_ideal_2[0][1]} metros disponibles.",
                f"Merma después de usar el carrete: {carretes_ideal_2[0][2]} metros.",
                f" ",
                f"Carrete {carretes_ideal_2[1][0]} puede cumplir con la otra mitad del requerimiento. Tiene {carretes_ideal_2[1][1]} metros disponibles.",
                f"Merma después de usar el carrete: {carretes_ideal_2[1][2]} metros."
            ],
            "costo_total": f"Costo total: ${costo_2} USD."
        })
    else:
        resultados.append({
            "opcion": f"Opción 2: No es posible cumplir con el requerimiento de {cable_requerido} metros usando dos carretes."
        })

    if carretes_ideal_3:
        costo_3 = round(cable_requerido * costo_por_metro + 30, 2)  # Añadir el costo del empalme
        resultados.append({
            "opcion": "Opción: 3 carretes",
            "detalles": [
                f"Carrete {carretes_ideal_3[0][0]} puede cumplir con un tercio del requerimiento. Tiene {carretes_ideal_3[0][1]} metros disponibles.",
                f"Merma después de usar el carrete: {carretes_ideal_3[0][2]} metros.",
                f" ",
                f"Carrete {carretes_ideal_3[1][0]} puede cumplir con otro tercio del requerimiento. Tiene {carretes_ideal_3[1][1]} metros disponibles.",
                f"Merma después de usar el carrete: {carretes_ideal_3[1][2]} metros.",
                f" ",
                f"Carrete {carretes_ideal_3[2][0]} puede cumplir con el último tercio del requerimiento. Tiene {carretes_ideal_3[2][1]} metros disponibles.",
                f"Merma después de usar el carrete: {carretes_ideal_3[2][2]} metros."
            ],
            "costo_total": f"Costo total: ${costo_3} USD."
        })
    else:
        resultados.append({
            "opcion": f"Opción 3: No es posible cumplir con el requerimiento de {cable_requerido} metros usando tres carretes."
        })

    # Imprimir los resultados para verificar
    print("Resultados de la búsqueda de carretes:")
    for resultado in resultados:
        print(resultado)

    return resultados  # Retornar una lista de diccionarios con los resultados


# Llamada a la función con parámetros de ejemplo
resultados = buscar_carrete(1, 150, 5)  # Ajusta los parámetros según sea necesario
