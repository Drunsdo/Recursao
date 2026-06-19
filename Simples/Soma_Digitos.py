def soma_digitos(n):
    print(f"o número atual é n={n}")
    
    if n == 0:
        return 0
    else:
        ultimo_digito = n % 10
        restante_do_numero = n // 10
        
        print(f"Pausando n={n}... Separou o dígito '{ultimo_digito}'. Descendo com o resto '{restante_do_numero}'")
        
        valor_que_subiu = soma_digitos(restante_do_numero)
        
        resultado_parcial = valor_que_subiu + ultimo_digito
        
        print(f"Voltando! n={n}. Somando valor que subiu ({valor_que_subiu}) + dígito ({ultimo_digito}). Valor parcial = {resultado_parcial}")
        
        return resultado_parcial

resultado = soma_digitos(121)
print("O resultado final da soma dos dígitos é:", resultado)