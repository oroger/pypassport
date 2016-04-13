from pypassport.epassport import EPassport, mrz
from pypassport.reader import ReaderManager

reader = ReaderManager()._autoDetect()

p = EPassport(reader, 'EI123456<9BEL8001018M1507010<<<<<<<<<<<<<<06')
print p["DG1"]