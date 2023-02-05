from bin.input_data import Data
from bin.gerador_temp.main import Temperatura

a = Data.data()

print('\n')
print('~'*70)
print('   No dia %i de %s, a variação de temperatura foi de %i° à %i°' % (a[1], Data.traducao(a[0]),Temperatura.planilha()[a[0] - 1][a[1] -1][1]['min'],Temperatura.planilha()[a[0] - 1][a[1] -1][1]['max']))
print('~'*70)
print('\n')


