def mdc(x, y):
    print(f"x={x}, y={y}")
    
    if y == 0:
        return x
    else:
        resto = x % y
        print(f"Pausando mdc({x}, {y})... O resto de {x} / {y} é {resto}. Descendo para mdc({y}, {resto})")
        
        resultado_parcial = mdc(y, resto)
        
        print(f"Voltando! O degrau de baixo entregou {resultado_parcial}. Apenas repassando para cima.")
        
        return resultado_parcial
    
resultado = mdc(81, 36)
print("O resultado final do MDC é:", resultado)