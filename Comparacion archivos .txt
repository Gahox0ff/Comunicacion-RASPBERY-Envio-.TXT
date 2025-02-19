def comparar_archivos(D1, Datos_Recibidos):
    with open(D1, 'r') as f1, open(Datos_Recibidos, 'r') as f2:
        contenido1 = f1.read()
        contenido2 = f2.read()
        errores = sum(1 for a, b in zip(contenido1, contenido2) if a != b)
        errores += abs(len(contenido1) - len(contenido2))
        print(f"Errores (caracteres diferentes): {errores}")

comparar_archivos('D1.txt', 'Datos_Recibidos.txt')
