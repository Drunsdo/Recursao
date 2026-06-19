def max_lista(lista, n):
    print(f"n={n}. Olhando para: {lista[:n]}")
    
    if n == 1:
        return lista[0]
    else:
        desafiante = lista[n - 1]
        print(f"Pausando n={n}... O Desafiante aqui é o '{desafiante}'. Descendo para buscar o campeão do resto da lista...")
        
        aux = max_lista(lista, n - 1)
        
        if aux > desafiante:
            print(f"Voltando! n={n}. Luta: Campeão ({aux}) vs Desafiante ({desafiante}). O Campeão VENCEU e continua subindo!")
            return aux
        else:
            print(f"Voltando! n={n}. Luta: Campeão ({aux}) vs Desafiante ({desafiante}). O Desafiante VENCEU e roubou a coroa!")
            return desafiante

minha_lista = [3, 9, 5]
resultado = max_lista(minha_lista, 3)
print("O resultado final (o maior da lista) é:", resultado)