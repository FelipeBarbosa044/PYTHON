def notas(*notas,sit = False):
    """
    Essa função serve para calculos de notas.
    :param notas: Aceita varios numeros de notas de alunos.
    :param sit: (opcional) Caso True: EXIBI  situação,Caso False: Não vai exibir
    :return: A media o maior,menor e o total das notas serão calculados e exibidos
    """

    total = len(notas)
    soma = sum(notas)
    media = soma/total
    if sit == True:
        if media > 7:
            situacao =  'APROVADO'
            return {'total' : total,'maior': max(notas),'menor': min(notas),'media':round(media,2),'situacao': situacao }
        if media > 5 and media < 7:
            situacao  = 'RECUPERAÇÃO'
            return {'total' : total,'maior': max(notas),'menor': min(notas),'media':round(media,2),'situacao': situacao }
        else:
            situacao = 'REPROVADO'
            return {'total' : total,'maior': max(notas),'menor': min(notas),'media':round(media,2),'situacao': situacao }
    if sit == False:
         return {'total' : total,'maior': max(notas),'menor': min(notas),'media':round(media,2) }

resp = (notas(5,6,8,sit=True))
print(resp)
help(notas)