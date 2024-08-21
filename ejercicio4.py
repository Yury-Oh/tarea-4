def filtrar_personas_por_edad(lista_personas, edad_minima, edad_maxima):
    # Iterar sobre la lista de personas
    for persona in lista_personas:
        # Verificar si la edad de la persona está dentro del rango especificado
        if edad_minima <= persona['edad'] <= edad_maxima:
            # Imprimir los nombres y apellidos
            print(f"{persona['nombres']} {persona['apellidos']}")

# Ejemplo de uso
personas = [
    {"nombres": "Pedro Julio", "apellidos": "Tristan Merchan", "edad": 101},
    {"nombres": "María Paula", "apellidos": "Gómez Pérez", "edad": 35},
    {"nombres": "Jungkook", "apellidos": "Jeon", "edad": 28},
    {"nombres": "Lucía", "apellidos": "Martínez Jiménez", "edad": 45}
]

# Filtrar y mostrar personas con edades entre 30 y 50 años
filtrar_personas_por_edad(personas, 28, 50)
