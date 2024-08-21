def mezclar_diccionarios(diccionario1, diccionario2):
    # Crear una copia del primer diccionario para comenzar la mezcla
    diccionario_mezclado = diccionario1.copy()
    
    # Agregar las claves y valores del segundo diccionario
    for clave, valor in diccionario2.items():
        # Solo agregar si la clave no está ya en el primer diccionario
        if clave not in diccionario_mezclado:
            diccionario_mezclado[clave] = valor
    
    return diccionario_mezclado

# Ejemplo de uso
dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'b': 20, 'c': 30, 'd': 4}

resultado = mezclar_diccionarios(dic1, dic2)
print(resultado)  # Esto imprimirá {'a': 1, 'b': 2, 'c': 3, 'd': 4}
