def verificar_diccionarios(diccionario1, diccionario2):
    # Iterar sobre cada clave en el primer diccionario
    for clave, valor in diccionario1.items():
        # Verificar si la clave está en el segundo diccionario y si el valor coincide
        if clave not in diccionario2 or diccionario1[clave] != diccionario2[clave]:
            return False
    # Si se recorren todas las claves sin problemas, entonces todos los pares clave:valor están presentes
    return True

# Ejemplo de uso
dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

resultado = verificar_diccionarios(dic1, dic2)
print(resultado)  # Esto imprimirá True


