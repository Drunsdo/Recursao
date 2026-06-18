def soma(x, y):
    print("valor de y: ", y)
    if y == 0:
        print("valor inicial de x: ", x)
        return x
    resultado_parcial = soma(x, y - 1) + 1
    print(f"Voltando! Para y={y}, o valor da soma parcial é {resultado_parcial}")

    return resultado_parcial

resultado = soma(5, 3)
print("O resultado final da soma é:", resultado)