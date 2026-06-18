def soma(x, y):
    print("valor de y: ", y)
    if y == 0:
        print("valor final de x: ", x)
        return x
    print("valor de x: ", x)
    return soma(x + 1, y - 1)

resultado = soma(5, 3)
print("O resultado final da soma é:", resultado)