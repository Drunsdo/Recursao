def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return soma_digitos(n // 10) + (n % 10)
resultado = soma_digitos(11)
print(resultado)