import random
al1 = input('Digite seu nome aluno: ')
al2 = input('Digite seu nome aluno 2: ')
al3 = input('Digite seu nome aluno 3: ')
al4 = input('Digite seu nome aluno 4: ')
sort = [al1,al2,al3,al4]
random.shuffle(sort)
print(f'A ordem de chamada para apagar apresentar o trabalho é {sort}')