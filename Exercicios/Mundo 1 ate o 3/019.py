import random
al1 = input('Digite seu nome aluno: ')
al2 = input('Digite seu nome aluno 2: ')
al3 = input('Digite seu nome aluno 3: ')
al4 = input('Digite seu nome aluno 4: ')
sort = [al1,al2,al3,al4]
print(f'O aluno sorteado que vai apagar a lousa é você {random.choice(sort)}')