from Merlin import *
from random import randint

print()
print('_____________________ ARTHUR MERLIN GAMES _____________________')
print()

#___________________ Problema das Damas _____________________#

print('....... Problema das Damas .......')
print()

arquivos = ['casamento.txt', 'casamento no.txt', 'casamento noo.txt']
n = randint(0,2)
f = open(arquivos[n]) # Abre um arquivo sorteado da lista de arquivos

damas = [] # Lista
queridos = {} # Dicionário
for pessoa in f:
    pessoa = pessoa.strip().split()
    # Strip -> tira os espaços do início e do fim do texto
    # Split -> separa os elementos do texto a partir de um parâmetro
    queridos[pessoa[0]] = pessoa[1:]
    # O primeiro elemento da lista nome é a key (chave)
    # Os outros são os amigos do nome key
    damas.append(pessoa[0])
    # Guardar o nome das damas
    # Elas também são as chaves para o dicionário dos queridos
#print(queridos)

x = 0
y = False
while x < (len(damas)-1):
    if len(queridos[damas[x]]) == 0:
        print(f'A {damas[x]} não tem preferências, ela prefere cuidar de 7 gatos ᓚᘏᗢ')
        print('Isso pode ser um problema para o reino ಠ_ಠ')
        print()
        y = True
        break
    x = x + 1

if y == False:
    for s in enumerações(damas):
        # Enumeração -> Fazer todas as combinações possíveis
        # desde a menor quantidade até a maior quantidade possível
        # Função descrita no arquivo Merlin.py
        pessoa = []
        for d in s:
            pessoa.extend(queridos[d])
        if len(s) > len(set(pessoa)):
            # Se a quantidade de damas for maior do que
            # a quantidade de cavaleiros únicos na lista
            print('Não é possível casar todas as damas, pois a')
            s = ' e '.join(s) # Nome das damas
            pessoa = ' '.join(set(pessoa)) # Querido disputado
            print(f'{s} gostam de {pessoa} ¯\_(ツ)_/¯')
            print()
            break
    else:
        print('É possível casar todas as damas!! (❤ ω ❤)')
    print()





#___________________ Problema dos Cavaleiros ___________________#

print('....... Problema dos Cavaleiros .......')
print()

arquivos = ['cavaleiros.txt', 'cavaleiros no.txt', 'cavaleiros noo.txt']
n = randint(0,2)

m = open(arquivos[n]) # Abre um arquivo sorteado da lista de arquivos
cavaleiros = [] # Lista
amigos = {} #Dicionário
for pessoa in m:
    pessoa = pessoa. strip().split()
    amigos[pessoa[0]] = pessoa[1:]
    # O primeiro elemento da lista nome é a key (chave)
    # Os outros são os amigos do nome key
    cavaleiros.append(pessoa[0])
    # Guardar o nome dos cavaleiros
    # Eles também são as chaves para o dicionário dos amigos
#print(amigos)

x = 0
y = False
while x < (len(cavaleiros)-1):
    if len(amigos[cavaleiros[x]]) < 2:
        print(f'O {cavaleiros[x]} não tem amigos suficientes para se sentar a mesa')
        print(f'que seriam no mínimo 2, por isso o {cavaleiros[x]} pode ser um problema (⊙_⊙;)')
        print()
        y = True
        break
    x = x + 1

if y == False:
    for p in permutações(cavaleiros):
        # Permutação -> Trocar as posições dos valores
        # todas as posições preenchidas possíveis
        # Função descrita no arquivo Merlin.py
        for k in range(len(p)):
            if p[k] not in amigos[p[(k+1)%len(p)]]:
                break
        else:
            print('Conseguimos uma mesa para todos os cavaleiros \o/')
            print('Sentados na seguinte sequência:')
            print(' '.join(p))
            break
    else:
        print('Não é possível arrumar uma mesa para os cavaleiros! (＞﹏＜)')
    
