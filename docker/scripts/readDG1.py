from pypassport.epassport import EPassport, mrz
from pypassport.reader import ReaderManager

reader = ReaderManager()._autoDetect()

p = EPassport(reader, 'EI303692<9BEL8406158M1507218<<<<<<<<<<<<<<06')
print p["DG1"]