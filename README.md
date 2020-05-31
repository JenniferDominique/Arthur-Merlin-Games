# 🤴🏻 Arthur-Merlin-Games 🧙🏻‍♂️

### 👨🏽‍🏫 Professor Orientador: [Fernando Masanori](https://github.com/fmasanori)

## Enunciado

Na corte do Rei Arthur há quatro damas e sete cavaleiros. Existem outros cavaleiros e damas, porém estarão fora do reino durante um bom tempo. O Rei Arthur possui dois sérios problemas:

**a)** Saber se é possível casar todas as quatro damas com os atuais cavaleiros, seguindo suas preferências pessoais. Damas "encalhadas" são fofoqueiras e um sério perigo para o sigilo na corte. É uma tarefa difícil, pois existem alguns cavaleiros que são muito disputados e outros que não são atraentes por terem perdido alguma parte do corpo nas várias batalhas (olho, perna, braço, etc...) além daqueles que secretamente estão comprometidos com damas de outros reinos.

**b)** Arrumar uma disposição dos sete cavaleiros em torno da Távola Redonda de tal modo que não briguem. Os cavaleiros amam a guerra e caso a pessoa do lado não seja algum grande amigo, ela será desafiada para um duelo. Deste modo morreram muitos cavaleiros nos últimos anos, fragilizando o poderio do reinado.

O Mago Merlin foi incumbido destas duas tarefas e irá contar com ajuda dos alunos da FATEC-SJC. Entre seus vários poderes mágicos ele possui dois algoritmos prontos, no arquivo merlin.py, que geram todas as enumerações e permutações, respectivamente, para um dado número inteiro n positivo. Você deverá fazer um programa em Python, utilizando os algoritmos do Mago Merlin que resolva os dois problemas do Rei Arthur.

**Entradas:** arquivos _casamento.txt_ e _casamento no.txt_ com as preferências de cada dama e arquivos _cavaleiros.txt_ e _cavaleiros no.txt_ com os amigos de cada cavaleiro. Suponha sempre que a amizade é recíproca, neste caso se um cavaleiro disser que outro é amigo, o outro dirá o mesmo dele.

**Saídas:**

**1.** Responder se é possível casar todas as damas. O aluno não precisa mostrar uma possível combinação de casamentos, sendo opcional essa parte. Porém, se não for possível casar todas as damas, deverá ser apresentada uma situação impeditiva.

**2.** Mostrar uma disposição dos cavaleiros em torno da Távola Redonda em que eles não bringuem ou dizer que isso é impossível.

*Damas:* 

      * Jessica;
      * Fernanda;
      * Pamela;
      * Renata.

*Cavaleiros:*

      * Adriano;
      * Bruno;
      * Diogo;
      * Eclis;
      * Gabriel;
      * Leandro;
      * Walber.
      
**casamento.txt**

*Jessica Adriano*

*Fernanda Bruno Gabriel Leandro*

*Pamela Adriano Diogo Leandro*

*Renata Adriano Walber*


**cavaleiros.txt**

*Adriano Bruno Gabriel Leandro Walber*

*Bruno Adriano Eclis*

*Diogo Eclis Gabriel*

*Eclis Bruno Diogo*

*Gabriel Adriano Diogo Walber*

*Leandro Adriano Bruno Walber*

*Walber Adriano Gabriel Leandro*

**Possível Saída:** Casamento possível e mesa Adriano-Bruno-Eclis-Diogo-Gabriel-Walber-Leando-Adriano

**Opcional:** Jessica-Adriano Fernanda-Bruno Pamela-Diogo Renata-Walber

[Casamento]

[Cavaleiros]

**casamento no.txt**

*Jessica Eclis*

*Fernanda Eclis*

*Pamela*

*Renata Eclis*

**cavaleiros no.txt**

*Adriano Bruno Leandro*

*Bruno Adriano Gabriel*

*Diogo Eclis Walber*

*Eclis Diogo Walber*

*Gabriel Bruno Leandro*

*Leandro Adriano Walber*

*Walber Diogo Eclis Leandro*

**Possível Saída:** Preferências de Jessica-Fernanda-Renata insuficientes e não é possível arrumar a mesa.

OU

Preferências de Pâmela são insuficientes e não é possível arrumar a mesa.

[Casamento no]

Não é possível arrumar a mesa para os sete cavaleiros.

[Cavaleiros no]
