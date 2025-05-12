def analise_lista(numeros):
    s = sum(numeros)
    qt = len(numeros)
    media = round(soma / quantidade, 2)
    maior = max(numeros)
    menor = min(numeros)
    qt_pares = sum(1 for num in numeros if num % 2 == 0)

    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "quantidade_pares": qt_pares
    }
