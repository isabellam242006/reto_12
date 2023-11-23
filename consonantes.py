def contar_consonantes(poema):
    contador_consonantes = 0
    for lineas in poema:
        for consonantes in lineas:
            if consonantes in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ":
                contador_consonantes+=1
    return contador_consonantes

if __name__ == "__main__":
    with open ("poema.txt") as poema:
        poema = poema.read()
    total_consonantes = contar_consonantes(poema)
    print(f"La cantidad de consonantes es {total_consonantes}")