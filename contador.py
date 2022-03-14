#!/bin/python3

from collections import Counter

def contar_letras(x: str) -> Counter:
    return Counter(x)

if __name__ == "__main__":
    frase = "Hola Mundo, estamos en el curso de metodologías agiels y machine learning"
    print(contar_letras(frase))
