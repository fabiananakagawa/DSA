def busca_sequencial(lista, procurado):
    for i in range(len(lista)):
        if lista[i] == procurado:
            return i
    return -1

nome = ['Mariana', 'José', 'João', 'Benedito', 'Geraldo', 'Antônio']

posicao = busca_sequencial(nome, 'João')

print(posicao)