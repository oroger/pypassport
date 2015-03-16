# 1 Modules Import #

Before starting using the API, modules are imported:

```
>>> from pypassport import epassport, reader
>>> from pypassport.doc9303 import converter
```

# 2 Data Sources #

The first step is to initialize a reader. A reader can be a true rfid reader or a
simulator.

## 2.1 RFID Reader ##

To use an RFID reader, the application waits until an ePassport is put on a plugged
reader. Once the ePassport is put on the reader, the method tries to detect
the plugged reader on which the ePassport is put as well as the corresponding
Reader implementation. If the detection succeed, the Reader implementation is
returned, else the reader is not supporter and the waiting loop continues until
the timeout triggers (set to 10 seconds in this example)

```
>>> r = reader.ReaderManager().waitForCard(10)
```

To use a determined Reader implementation, its name as well as the reader
number are given to the method:

```
>>> r = reader.ReaderManager().waitForCard("PcscReader", 1)
```


## 2.2 Simulator ##

The simulator is created by asking to the ReaderManager factory the DumpReader
implementation. The simulator is configured to read files named using the Golden Reader Tool naming convention with a '.bin' file extension.

In this case, the connect does not take the PCSC reader number
anymore but the dump directory.

```
>>> r = reader.ReaderManager().create("DumpReader")
>>> r.format = converter.types.GRT
>>> r.ext = ".bin"
>>> r.connect("d:\\dumps")
```

# 3 EPassport Front End #

The front end is the EPassport object. It is implemented as a dictionary filled
as the data groups are requested. The object is initialized with the Reader
implementation and a string corresponding to the ePassport second line MRZ.
The given MRZ is verified by the EPassport object. If the verification fails an EPassportException is raised because a valid MRZ is required for the BAC.

```
>>> mrz = "EH123456<0BEL0310859M0705109<<<<<<<<<<<<<<00"
>>> ep = epassport.EPassport(r,mrz)
```

## 3.1 Files operations ##

When the front-end is initialized, it can be used to access ePassport’s files. They
are read by requesting one of the following values to the dictionary: Common,
DG1. . . DG16, SecurityData. If the requested file does exist, it is returned; else
the file is read, parsed, set in the dictionary and returned in its DataGroup
implementation. If the requested data group does not exist, a DataGroupException
is raised.

To know present data group in the ePassport, the Common file is first read.
Both the BAC and the Secure Messaging are managed transparently if required.

```
>>> com = ep["Common"]
>>> print ep
{'60': {'5F36': '040000', '5F01': '0107', '5C': ['61', '75', '67', '6B', '6C', '6F']}}
>>> print com
{'5F36': '040000', '5F01': '0107', '5C': ['61', '75', '67', '6B', '6C','6F']}
>>> print com['5C']
['61', '75', '67', '6B', '6C', '6F']
>>> print ep['Common']['5C']
['61', '75', '67', '6B', '6C', '6F']
```

The code example above shows how to read the Common file using the EPassport
front-end, and how to access its Data Objects. To well understand how the EPassport
object works, a few examples are provided. In line 3, the EPassport object
content is show; it contains one entry, the read object Com. The Com content
is printed in line 5. It is composed of three Data Objects:

  * 5F36 : The LDS version number
  * 5F01 : The Unicode version number
  * 5C : Tag list of all data group present

As explained previously, once a file is read, it is put inside the dictionary
under its tag notation and won’t be read again. Despite the fact that the
Common file was requested; the ep’s dictionary contains the key ’60’.
Indeed a data group can be requested using any notation supported by the converter.
The notation is then internally transformed to its tag value, used as key to
stored the read object.

All the statements in the following code example are equivalent to read the data group DG1. It leads to the single ’61’ entry inside the EPassport dictionary.

```
>>> ep['DG1']
>>> ep['61']
>>> ep['EF.DG1']
>>> ep['01'] 
>>> ep['0101'] 
```

The DataGroup1 dictionary can then be iterated inside a loop. To translate
tag values to their meaning, the API proposes the tagToName method from
the tagconverter module. It takes the tag value as input and returns the tag
meaning.

```
>>> dg1 = ep['DG1']
>>> for tag in dg1:
>>>   print tag + "> " + epassport.tagconverter.tagToName[tag] 
>>>   + ": " + str(dg1[tag])
...
59> Date of Expiry or valid Until Date: 150807
5F03> Document Type: P<
5F5B> Name of Holder: SMITH<<JOHN<<<<<<<<<<<<<<<<<<<<<<<<<<<<
5F2C> Nationality: BEL
5F57> Date of birth (6 digit): 851003
5F28> Issuing State or Organization: BEL
5F35> Sex: M
5A> Document Number: EH123456<
...
```

The EPassport dictionary can also be iterated. All files not yet present are
read and inserted into the dictionary before the iteration.

```
>>> for dg in ep:
>>>   print "tag: " + dg
>>>   print "content: " + str(ep[dg])
...
tag: 60
content: {'5F36': '040000', .., '5C': ['61', '75', .., '6F']}
tag: 61
content: {'5F05': '8', ..., '5F35': 'M', '5A': 'EH123456<'}
tag: 75
...
```

The readPassport method is used to read every ePassport’s files and set the
EPassport’s dictionary with the corresponding objects: Com, DataGroupXX
and SOD.

```
>>> ep.readPassport()
```

Four shortcuts are also available to retrieve the owner face and its signature
(if available), the CDS and the DG15 public key (if available) from the ePassport.
The images are returned in a list of binary string and both the CDS and its public
key are returned in text + PEM format.

```
>>> signatures = ep.getSignatures()
>>> faces = ep.getFaces()
>>> pubKey = ep.getPublicKey()
>>> DSC = ep.getCertificate()
```

## 3.2 Security Operations ##

### 3.2.1 Security Operations Initilization ###

Before performing security operations, two EPassport parameters must be set.

```
>>> ep.setCSCADirectory("D:\\CSCACertificates", True) 
>>> ep.openSsl = "C:\\OpenSSL\\bin\\openssl"
```

The first line indicates the Certificates CSCA directory. It accepts certificates in both
PEM and DER format. The False parameter specifies that Certificates must be
renames with their issuer hash value 16. The parameter can then be set to False
until new certificates are added to avoid the hash operations.

The second line is optional. If openssl is not in the path, its location can be
set manually. The openssl binary is mandatory to perform the Passive Authentication.

### 3.2.2 Active Authentication ###

The AA works ony with an RFID reader. If the AA is not supported by the
ePassport or if it is called by the simulator, an ActiveAuthenticationException
is raised. Otherwise a Boolean is returned. Both API’s exceptions inherit from
Exception, so the Exception exception can be catched if the exception’s nature
is not important.

```
>>> try:
>>>   ep.doActiveAuthentication()
>>>   except Exception, msg:
>>>     print msg
True
```

### 3.2.3 Passive Authentication ###

The PA is performed in two steps:

1. The SOD is read and verified using the CDS, itself verified with the
CSCA Certificate. Finally the signature’s data is read. The method returns True if
the verification succeeds or raises an exception with the appropriate error
message.

```
>>> try:
>>>   print ep.doVerifySODCertificate()
>>>   except Exception, msg:
>>>     print msg
/C=BE/O=Kingdom of Belgium/OU=Federal Public Service 
Foreign Affairs Belgium/CN=DSPKI_BE
error 20 at 0 depth lookup:unable to get local issuer 
certificate
```

In this example the verification fails because the Belgian CSCA is not
available. It means that the signature is valid according the CDS, but
that the CDS has not been verified by the unavailable CSCA.

2. The hash values of all data group are computed and compared to the
hash values retrieved from the signature in step 1. The method returns
a dictionary with a Boolean for each data group. True means that the
comparison succeeds.

```
>>> try:
>>>   print ep.doVerifyDGIntegrity()    
>>>     except Exception, msg:
>>>     print msg
{'DG15': True, 'DG11': True, 'DG12': False, 'DG2': True, 'DG1': True, 'DG7': True}
```

The verification was run on an ePassport with one altered data group: the
DG12.

## 3.3 Data Dump ##

To dump the ePassport files as well as the face(s), the signature(s), the Document Signer Certificate and the data group DG15 Public Key, the dump method is used.

By default the files are saved with the Golden Reader Tool naming convention
in the user directory, but all these parameters can be personalized. For
example, the dumps can be saved in the c:/dumps directory in the FID notation
with the .bin extension.

```
>>> ep.dump('c:\\dumps', 'FID', '.bin')
```

As an ePassport can contain several faces and signatures, they are stored
under the name signatureX.jpg and faceX.jpg, where X is the picture number.
The Document Signer Certificate is saved in PEM under the DocumentSigner.cer name and the DG15 Public Key is stored in PEM under the DG15PublicKey.key name.

## 3.4 Log ##

The EPassport gives access to the logs of every class behind EPassport. To
access these logs, the user must register a 2-parameter method to the EPassport
object. The first parameter is the sender name and the second its log message.

```
>>> def trace(name, msg):
>>>   print name + "> " + msg
>>> ep.register(trace)
>>> ep.readPassport()
EPassport> Reading Passport
ISO7816> Select File
ISO7816> > 00 A4 02 0C 02 [011E]
ISO7816> < [] 69 82
BAC> Read the mrz
BAC> MRZ: EH276509<0BEL8406158M1302217<<<<<<<<<<<<<<04
BAC> Construct the 'MRZ\_information' out of the MRZ
BAC> Document number: EH276509< check digit: 0
...
```

The log messages can then be filtered using the name parameter of the trace
method to only print or save to disk the messages from a set of sender.