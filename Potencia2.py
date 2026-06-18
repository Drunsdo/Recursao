def potencia(k, n):
    print(f"k={k}, n={n}")
    
    if n == 0:
        return 1
    else:
        metade = n // 2
        print(f"Pausando n={n}... Chamando potencia({k}, {metade}) para achar o 'aux'")
        
        aux = potencia(k, metade)
        
        if n % 2 == 0:
            resultado_parcial = aux * aux
            print(f"Voltando! n={n} (PAR). Calculando aux * aux ({aux} * {aux}). Valor parcial = {resultado_parcial}")
            return resultado_parcial
        else:
            resultado_parcial = k * aux * aux
            print(f"Voltando! n={n} (ÍMPAR). Calculando k * aux * aux ({k} * {aux} * {aux}). Valor parcial = {resultado_parcial}")
            return resultado_parcial

resultado = potencia(3, 9)
print("O resultado final da potência é:", resultado)