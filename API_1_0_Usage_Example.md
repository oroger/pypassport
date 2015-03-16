The API contains fake dumps and certificates in the directory testData

```
from pypassport import epassport, reader
from pypassport import fingerPrint
from pypassport.doc9303 import converter

def trace(name, msg):
    print name + "> " + msg

Sim=True
AA=False
PA=True
HASH_CERTIF=False

MRZ = "EH123456<0BEL8510035M1508075<<<<<<<<<<<<<<02"
READER = "DumpReader"
CSCA_DIR = "testData"
DUMP_DIR = "testData"
FILES_EXT = ".bin"

r=None

if not Sim:
    r = reader.ReaderManager().waitForCard()
else:
    r = reader.ReaderManager().create(READER)
    r.format = converter.types.GRT
    r.ext = FILES_EXT 
    r.connect(DUMP_DIR)

ep = epassport.EPassport(r, MRZ)
ep.register(trace)
ep.setCSCADirectory(CSCA_DIR, HASH_CERTIF)

for dg in ep:
    print ep[dg]

if PA:
    try:
        ep.doVerifySODCertificate()
    except Exception, msg:
       print msg
    try:
        p = ep.readDataGroups()
        ep.doVerifyDGIntegrity(p)
    except Exception, msg:
        print msg

if AA:
    ep.doActiveAuthentication()

```