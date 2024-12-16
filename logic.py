# logic.py
from data import datos

def buscar_carrete(piezometro_id, cable_requerido, costo_por_metro):
    piezometro = next((p for p in datos["piezometros"] if p["ID"] == piezometro_id), None)
    if not piezometro:
        return "El piezómetro ingresado no existe."

    if cable_requerido <= 0:
        return "Por favor, ingrese una cantidad válida de cable."
    
    if costo_por_metro <= 0:
        return "Por favor, ingrese un costo válido por metro."

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
            if carrete_id not in carretes_usados_2:
                merma = round(longitud - mitad_cable_requerido, 2)
                if longitud >= mitad_cable_requerido and merma >= 0:
                    carretes_ideal_2.append((carrete_id, longitud, merma))
                    carretes_usados_2.add(carrete_id)
                    break

    # Opción 3: Usar tres carretes (dividir la cantidad por tres)
    tercio_cable_requerido = cable_requerido / 3
    carretes_ideal_3 = []
    carretes_usados_3 = set()

    for _ in range(3):
        for carrete_id, longitud in carretes:
            if carrete_id not in carretes_usados_3:
                merma = round(longitud - tercio_cable_requerido, 2)
                if longitud >= tercio_cable_requerido and merma >= 0:
                    carretes_ideal_3.append((carrete_id, longitud, merma))
                    carretes_usados_3.add(carrete_id)
                    break

    # Mostrar los resultados
    result = []
    if carrete_ideal_1:
        carrete_id, longitud_carrete, merma = carrete_ideal_1
        costo_1 = round(cable_requerido * costo_por_metro, 2)
        result.append(f"Opción 1: Usar 1 carrete: El carrete {carrete_id} puede cumplir con el requerimiento. Tiene {longitud_carrete} metros disponibles.")
        result.append(f"Merma después de usar el carrete: {merma} metros.")
        result.append(f"Costo total: ${costo_1} USD.")
    else:
        result.append(f"Opción 1: No es posible cumplir con el requerimiento usando un solo carrete con merma mayor a 30 metros.")

    if carretes_ideal_2:
        result.append(f"\nOpción 2: Usar 2 carretes:")
        costo_2 = round(cable_requerido * costo_por_metro + 15, 2)
        for carrete_id, longitud_carrete, merma in carretes_ideal_2:
            result.append(f"Carrete {carrete_id} puede cumplir con la mitad del requerimiento. Tiene {longitud_carrete} metros disponibles.")
            result.append(f"Merma después de usar el carrete: {merma} metros.")
        result.append(f"Costo total: ${costo_2} USD.")
    else:
        result.append(f"\nOpción 2: No es posible cumplir con el requerimiento usando dos carretes.")

    if carretes_ideal_3:
        result.append(f"\nOpción 3: Usar 3 carretes:")
        costo_3 = round(cable_requerido * costo_por_metro + 30, 2)
        for carrete_id, longitud_carrete, merma in carretes_ideal_3:
            result.append(f"Carrete {carrete_id} puede cumplir con un tercio del requerimiento. Tiene {longitud_carrete} metros disponibles.")
            result.append(f"Merma después de usar el carrete: {merma} metros.")
        result.append(f"Costo total: ${costo_3} USD.")
    else:
        result.append(f"\nOpción 3: No es posible cumplir con el requerimiento usando tres carretes.")
    
    return "\n".join(result)
