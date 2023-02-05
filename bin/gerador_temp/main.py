# CLASSE TEMPERATURA:

from random import randint

class Temperatura:

    def __init__ (self, temp_min, temp_max):
        self.tmin = temp_min
        self.tmax = temp_max
        pass

    def temps():
        tmin = randint(15,30)
        tmax = randint(30,45)
        lst_temp = {'min':tmin,'max':tmax}
        return lst_temp

    def ano():
        """[[dias],[dias],[dias]]"""
        # NO TERMO X = (MÊS - 1), ACESSE OS DIAS.
        lst = []
        lst1 = []
        for a in range(1,13):
            if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
                for i in range(1,32):
                    lst.append(i)
                lst1.extend([lst])
                lst = []
            elif a == 2:
                for i in range(1,29):
                    lst.append(i)
                lst1.extend([lst])
                lst = []
            else:
                for i in range(1,31):
                    lst.append(i)
                lst1.extend([lst])
                lst = []
        return lst1

    #BANCO DE DADOS
    def planilha ():
        """[mes-1][dia-1][1] = {min:   , max:   }"""
        lst = []
        lst1 = []
        for mes in Temperatura.ano():
            for dia in mes:
                a = [dia, Temperatura.temps()]
                lst.append(a)
            lst1.extend([lst])
            lst = []
        return lst1
