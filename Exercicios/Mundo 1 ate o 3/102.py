def fatorial(n=0,show=False):
    """
    Essa função calcula o fatorial...
    :param n: O numero,em que a função vai calcular a fatorial
    :param show: False =  Não Exibira o processo, True = Exibira
    :return: Vai retornar o resultado do fatorial

    """
    total = 1
    if show == True:
        print(f'{n}',end='')
        total = n
        n = n - 1
        while n > 1:
            print(f' X {n}',end='')
            total = total * n
            n-= 1
        print(f' X 1 = {total}')
    else:
        while n > 1:
            total *= n
            n-= 1
        print(total)


fatorial(10,False)
print('=='*55)
help(fatorial)




