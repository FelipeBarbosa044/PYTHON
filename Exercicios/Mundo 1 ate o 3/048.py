total = 0
qt = 0
for c in range(3,501,3):
    if c % 2 != 0:
        print(' -',c,end = '')
        qt += 1
        total += c
print(f'\nO total dos multiplos de 3 (do 3 até o 500) é : {total} dos {qt} numeros somados')