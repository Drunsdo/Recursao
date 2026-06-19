def inverte(s):
    print(f"Descendo... Palavra: '{s}'")

    if len(s) <= 1:
        print(f"Base alcançada! Restou apenas '{s}'. Retornando semente '{s}'")
        return s
    else:
        primeira_letra = s[0]
        ultima_letra = s[-1]
        meio_da_palavra = s[1:-1]
        
        print(f"Pausando '{s}'... Guardou a última ('{ultima_letra}') e a primeira ('{primeira_letra}'). Descendo para inverter o meio: '{meio_da_palavra}'")
        
        meio_invertido = inverte(meio_da_palavra)
        
        resultado_parcial = ultima_letra + meio_invertido + primeira_letra
        
        print(f"Voltando! Juntando: '{ultima_letra}' + '{meio_invertido}' + '{primeira_letra}'. Valor parcial = '{resultado_parcial}'")
        
        return resultado_parcial
    
resultado = inverte("MC102")
print("O resultado final da inversão é:", resultado)