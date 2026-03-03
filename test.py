
from src.meibo import Meibo

meibo = Meibo()

try:

    meibo.set_path('sample_files/meibo.csv')
    meibo.load()

    s= meibo.lookup('M31')
    print(s)
    
    s = meibo.lookup('M31', '1')
    print(s)
    
    meibo.clear()

    
    s = meibo.lookup('M31', '1')
    print(s)
    

except Exception as e:
    print(e)


