def potencia(k, n):
    print(f"k é {k}, n é {n}")
    
    if n == 0:
        return 1
    else:
        print(f"Pausando n={n}... Chamando potencia({k}, {n})")

        valor_que_subiu = potencia(k, n - 1)
        
        resultado_parcial = k * valor_que_subiu
        
        print(f"Voltando! n={n}. Multiplicando {k} * {valor_que_subiu}. Valor parcial = {resultado_parcial}")
        
        return resultado_parcial
    
resultado = potencia(3, 3)
print("O resultado final da potência é:", resultado)