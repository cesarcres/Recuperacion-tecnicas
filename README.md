## 1. Quina estratègia algorísimica es millor per resoldre aquest problema? Justifica la teva resposta.
La estrategia que he elegido es la de divide y vencerás, en la que se divide el problema en partes más pequeñas, haciendo que el problema inicial se vuelva mucho más sencillo.

## 2. Dissenyeu un algorisme que resolgui el problema i tingui el menor cost computacional.
def prefijo_comun(nombres):
    #Si la lista solo tiene un nonmbre, devuelve ese nombre.
    if len(nombres) == 1:
        return nombres[0]

    # Dividimos la lista en dos partes.
    mitad = len(nombres) // 2
    izquierda = prefijo_comun(nombres[0:mitad])
    derecha = prefijo_comun(nombres[mitad:])

    # Combina los resultados.
    return combina_prefijos(izquierda, derecha)

def combina_prefijos(prefijo1, prefijo2):
    i = 0
    # Itera sobre los prefijos siempre que sean iguales.
    while i < min(len(prefijo1), len(prefijo2)) and prefijo1[i] == prefijo2[i]:
        i += 1
    # Devuelve la parte comun.
    return prefijo1[:i]

## 3. Demostreu el cost computacional de l’algorisme. 
El coste computacional de mi codigo es O(n log n), donde n es la longitud de la lista de los nombres, ya que proviene de la recurrencia T(n)=2T(n/2)+O(k).
Donde n/2 proviene de la division en 2 de la lista.

## 4. Què canviarieu de l’algorisme per saber la seqüencia de caràcters finals més llarga (postfix)?

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



