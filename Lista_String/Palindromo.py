def palindromo(s):
    print(f"Descendo... Analisando a palavra: '{s}'")
    
    if len(s) <= 1:
        print(f"--- Base 1! Restou apenas '{s}'. É palíndromo! Retornando semente True ---")
        return True

    if s[0] != s[-1]:
        print(f"--- Base 2! Fim de jogo. A primeira letra '{s[0]}' é diferente da última '{s[-1]}'. Retornando False ---")
        return False

    meio_da_palavra = s[1:-1]
    print(f"Pausando '{s}'... '{s[0]}' == '{s[-1]}'. Cortando as pontas e descendo para '{meio_da_palavra}'")
    
    resultado_parcial = palindromo(meio_da_palavra)
    
    print(f"Voltando! O degrau de baixo entregou {resultado_parcial}. Apenas repassando para cima.")
    
    return resultado_parcial

print("=== TESTE 1: 'radar' ===")
resultado1 = palindromo("radar")
print("É palíndromo?", resultado1)

print("\n=== TESTE 2: 'rato' ===")
resultado2 = palindromo("rato")
print("É palíndromo?", resultado2)