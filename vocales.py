def contar_vocales(poema):
    contador_vocales = 0
    for line in poema:
        for vocales in line:
            if vocales in "aeiouAEIOUáéíóúÁÉÍÓÚ":
                contador_vocales += 1
    return contador_vocales



if __name__ == "__main__":
    with open("poema.txt") as poema:
        poema = poema.read()
    total_vocales = contar_vocales(poema)
    print(f"El número de vocales en total es  {total_vocales}")