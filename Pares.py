def soma_par(n):
    print(f"valor de n: {n}")
    
    if n <= 0:
        return 0
    else:
        if n % 2 == 0:
            resultado_parcial = soma_par(n - 2) + n
            print(f"Voltando! n={n} (PAR). Somando {n}. Valor parcial = {resultado_parcial}")
            return resultado_parcial
        else:
            resultado_parcial = soma_par(n - 1)
            print(f"Voltando! n={n} (ÍMPAR). Não soma nada. Repassando valor = {resultado_parcial}")
            return resultado_parcial
        
resultado = soma_par(6)
print("O resultado final da soma é:", resultado)