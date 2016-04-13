from pypassport.epassport import EPassport, mrz
from pypassport.reader import ReaderManager

reader = ReaderManager().waitForCard()

p = EPassport(reader, 'EI123456<9BEL8001018M1507010<<<<<<<<<<<<<<06')
p.readPassport()
print p
