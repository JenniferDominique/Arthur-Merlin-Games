f = open('cavaleiros.txt')
amigos = {}
for linha in f:
  linha = linha.strip().split()
  amigos[linha[0]] = linha[1:]
print (amigos)

from itertools import cycle
for p in permutações(list(amigos.keys())):
  mesa = cycle(p)
  anterior = p = next(mesa)
  while True:
    prox = next(mesa)
    if prox not in amigos[anteiror]:
      print ('Deu pau')
    if prox == p:
      break


#####OOOOUUUU#####

for p in permutações(list(amigos.keys())):
  for k in range(len(p)-1):
    if p[k+1] not in amigos[p[k]]:
      print ('Deu pau')
  if p[6] not in amigos[p[0]]:
    print ('deu pau')
