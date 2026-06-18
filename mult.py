def mult(x, y):

    if y == 1:
        print("valor inicial de x: ", x)
        return x
    resultado_parcial = mult(x, y - 1) + x
    print(f"Voltando! Para y={y}, o valor da multiplicação parcial é {resultado_parcial}")

    return resultado_parcial

resultado = mult(5, 3)
print("O resultado final da multiplicação é:", resultado)