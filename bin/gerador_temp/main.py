# CLASSE TEMPERATURA:

from random import randint

class Temperatura:

    def __init__ (self, temp_min, temp_max):
        self.tmin = temp_min
        self.tmax = temp_max
        pass

    def lista():
        tmin = randint(15,30)
        tmax = randint(30,45)
        lst_temp = {'min':tmin,'max':tmax}
        return lst_temp

    def ano():
        lst = []
        while 1:
            for i in range(1,366):
                a = [i,Temperatura.lista()]
                lst.extend(a)
            break
        return lst
