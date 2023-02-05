# INPUT MÊS E DIA:

from bin.gerador_temp.main import Temperatura

class Data:

    def __init__(self, dia, mes):
        self.d = dia
        self.m = mes
        pass
    
    def traducao(mes):
        lst = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
        return lst[mes - 1]

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
        return [mes,dia]