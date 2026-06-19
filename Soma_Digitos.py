def soma_digitos(n):
    print(f"o número atual é n={n}")
    
    # Condição de parada
    if n == 0:
        return 0
    else:
        # 1. Separamos as coisas para enxergar melhor
        ultimo_digito = n % 10
        resto_do_numero = n // 10
        
        print(f"Pausando n={n}... Separou o dígito '{ultimo_digito}'. Descendo com o resto '{resto_do_numero}'")
        
        # 2. A recursão desce enviando o número sem o último dígito
        valor_que_subiu = soma_digitos(resto_do_numero)
        
        # 3. Na volta, ele soma o que subiu com o dígito que ele havia separado
        resultado_parcial = valor_que_subiu + ultimo_digito
        
        print(f"Voltando! n={n}. Somando valor que subiu ({valor_que_subiu}) + dígito ({ultimo_digito}). Valor parcial = {resultado_parcial}")
        
        return resultado_parcial

resultado = soma_digitos(11)
print("O resultado final da soma dos dígitos é:", resultado)