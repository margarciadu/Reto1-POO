def same_characters(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    result = []
    for group in groups.values():
        if len(group) > 1:
            result.extend(group)

    return result


if __name__ == "__main__":
    x = input("Ingrese una lista de palabras separadas por espacios: ")
    y = list(map(str, x.split()))
    result = same_characters(y)

    if result:
        print("Palabras con los mismos caracteres (anagramas):")
        print(result)
    else:
        print("No se encontraron palabras con los mismos caracteres.")
