import networkx as nx

conv = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
def criar_tabuleiro(x):
    for i in range(8):
        row = []
        for j in range(8):
            row.append(j)
        x.append(row)
    return x
def cavalo(pos_x, pos_y):
    lista = []
    for a in [-2,2]:
        for b in [-1,1]:
            if (pos_x + a) > 0 and (pos_y + b) > 0: lista.append([conv[pos_x + a],pos_y + b])
    for a in [-1,1]:
        for b in [-2,2]:
            if (pos_x + a) > 0 and (pos_y + b) > 0: lista.append([conv[pos_x + a],pos_y + b])
    return lista

#criar_tabuleiro(teste)
print cavalo(1,1)
