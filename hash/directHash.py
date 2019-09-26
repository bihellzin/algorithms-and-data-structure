import numpy as np

class direct_hash:
    def __init__(self, m):
        self.array = np.full(m, None, None)
        self.leng = m
    
    def inserir_hash(self, value):
        i = 0
        h = (5 * value + i**2)%self.leng
        if self.array[h] is None:
            self.array[h] = value
        
        else:
            while self.array[h] is not None and i < self.leng:
                i += 1
                h = (5 * value + i**2)%self.leng
            self.array[h] = value
            if i == self.leng:
                print('erro')
                return False
        
        print('Valor inserido na tabela hash')
        return True
            