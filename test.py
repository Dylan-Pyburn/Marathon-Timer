
from src.meibo import Meibo

meibo = Meibo()

try:

    meibo.set_path('sample_files/meibo.csv')
    meibo.load()

    s= meibo.get_students('M31')
    print(s)
    
    
    
    

except Exception as e:
    print(e)


