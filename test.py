
from src.meibo import Meibo

meibo = Meibo()

try:

    meibo.set_path('sample_files/meibo2.csv')
    meibo.load()
    
    print(meibo['M32'])
    print(meibo['B1']['2'])
    meibo.clear()
    print(meibo['M32'])

except Exception as e:
    print(e)


