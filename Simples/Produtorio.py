def produtorio(m, n):
    if m == n:
        return m
    else:
        return produtorio(m, n - 1) * n

resultado = produtorio(2,3)
print(resultado)