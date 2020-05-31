f = open('casamento no.txt')
queridos = {}
for linha in f:
  linha = linha.strip().split()
  queridos[linha[0]] = linha[1:]
print (queridos)

from Merlin import *
for s in enumerações (list(queridos.keys())):
  # Pego as chaves das damas e transformou em lista
  #print (s)
  lista = []
  for d in s:
    lista.extends(queridos[d])
  print (s,lista)
  if len(s) > len(set(lista)):
    print ('Não é possível')
    print (f'Damas: {s}')
    print (f'Queridos: {lista}')
    break

  


