lingua = ['AT', 'DF', 'lFR', 'FRo', 'HHHn']
print('Antes da listcomp: ', lingua)
lingua = [item.lower() for item in lingua]
print('\n Depois da listcomp: ', lingua)

