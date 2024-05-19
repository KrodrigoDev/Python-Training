lista_fora_ordem = [5, 1, 8, 0, 4, 45, 18, 2]

for i in range(0, len(lista_fora_ordem)):
    menor_indice = i

    for j in range(i + 1, len(lista_fora_ordem)):
        if lista_fora_ordem[j] < lista_fora_ordem[menor_indice]:
            menor_indice = j

    aux = lista_fora_ordem[i]
    lista_fora_ordem[i] = lista_fora_ordem[menor_indice]
    lista_fora_ordem[menor_indice] = aux

print(lista_fora_ordem)
