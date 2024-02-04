import sys

def prefijo_sufijo_comun(nombres):
    #Si la lista solo tiene un nonmbre, devuelve ese nombre.
    if len(nombres) == 1:
        return nombres[0], nombres[0]

    # Dividimos la lista en dos partes.
    mitad = len(nombres) // 2
    izquierda_pref, izquierda_suf = prefijo_sufijo_comun(nombres[0:mitad])
    derecha_pref, derecha_suf = prefijo_sufijo_comun(nombres[mitad:])

    prefijo_comun = combina_prefijos(izquierda_pref, derecha_pref)
    sufijo_comun = combina_sufijos(izquierda_suf, derecha_suf)

    # Combina los resultados.
    return prefijo_comun, sufijo_comun

def combina_prefijos(prefijo1, prefijo2):
    i = 0
    # Itera sobre los prefijos siempre que sean iguales.
    while i < min(len(prefijo1), len(prefijo2)) and prefijo1[i] == prefijo2[i]:
        i += 1
    # Devuelve la parte comun del prefijo.
    return prefijo1[:i]

def combina_sufijos(sufijo1, sufijo2):
    i = 0
    len1, len2 = len(sufijo1), len(sufijo2)
    # Itera sobre los sufijos siempre que sean iguales.
    while i < min(len1, len2) and sufijo1[len1 - 1 - i] == sufijo2[len2 - 1 - i]:
        i += 1
    # Devuelve la parte comun del sufijo.
    return sufijo1[len1 - i:]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Usar: python main.py <prefijo/sufijo>")
        sys.exit(1)

    tipus_seq = sys.argv[1]

    # Ejemplo de uso del examen 
    nombres = ["Aldolin", "Alendi", "Allomancy", "Alethi"]

    if tipus_seq.lower() == 'prefijo':
        resultado_prefijo, _ = prefijo_sufijo_comun(nombres)
        print(f"Prefijo común: {resultado_prefijo}")
    elif tipus_seq.lower() == 'sufijo':
        _, resultado_sufijo = prefijo_sufijo_comun(nombres)
        print(f"Sufijo común: {resultado_sufijo}")
    else:
        print("La opción debe ser 'prefijo' o 'sufijo'.")

