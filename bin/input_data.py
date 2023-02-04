# INPUT MÊS E DIA:

class Data:

    def __init__(self, dia, mes):
        self.d = dia
        self.m = mes
        pass
    
    def traducao(a):
        if a == 1:
            return 'janeiro'
        if a == 2:
            return 'fevereiro'
        if a == 3:
            return 'março'
        if a == 4:
            return 'abril'
        if a == 5:
            return 'maio'
        if a == 6:
            return 'junho'
        if a == 7:
            return 'julho'
        if a == 8:
            return 'agosto'
        if a == 9:
            return 'setembro'
        if a == 10:
            return 'outubro'
        if a == 11:
            return 'novembro'
        if a == 12:
            return 'dezembro'

    def data ():
        while 1:
            try:
                mes = int(input('\nInsira o mês: '))
                if mes < 1 or mes > 12:
                    raise Exception
                break
            except:
                print('\nMês inválido! Tente outro...')
        while 2:
            try:
                dia = int(input('\nInsira o dia: '))
                if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                    if dia < 1 or dia > 31:
                        raise Exception
                    break
                elif mes == 2:
                    if dia < 1 or dia > 28:
                        raise Exception
                    break
                else:
                    if dia < 1 or dia > 30:
                        raise Exception
                    break
            except:
                print('\nDia inválido! Tente outro...')

        return print('\nNo dia %i de %s, a variação de temperaturas foi de %i° a %i°.\n' %(dia,Data.traducao(mes),Temperatura.lista()['min'],Temperatura.lista()['max']))