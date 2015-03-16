# 1 Data source #

```
import time
from pypassport import epassport, reader
```
## 1.1 RFID Reader ##
  * Reader auto-detection
Drop the passport on a connected reader and if it is compatible, it will be selected.
```
r = reader.pcscAutoDetect()[0]
while not r:
    r = reader.pcscAutoDetect()[0]
    time.sleep(0.5)
```
  * Manual selection
Use the reader factory to create a specific driver, and to connect to a specific reader number.
```
r = reader.ReaderFactory().create("GENERIC")
while not r.connect(1):
    time.sleep(0.5)
```
## 1.2 Simulator ##
Just set the path to the dump directiry into a variable.
```
r = "D:\\workspace\\pypassport\\src\\data\\dump\\Oli"
```

# 2 MRZ verification #
Create the MRZ object and check its validity.
```
mrz = epassport.mrz.MRZ("EH276509<0BEL8406158M1302217<<<<<<<<<<<<<<04")

if not mrz.checkMRZ():
    raise Exception ("Unvalid MRZ")
```

# 3 Front end epassport object #
## 3.1 Data groups operations ##

The front end object is a lazy dictionnary populated when values are requested. When the EPassport object is created, the Passport Aplication is automatically selected.
```
ep = epassport.EPassport(mrz, r)
```

You can then select any data group present in the epassport. The secure messaging is automatically activated if needed. To know the list of the data groups present in the epassport, select the Common file and read the content of the tag '5C':

```
com = ep["Common"]
tagList = com["5C"]
>>> print tagList
>>> ['61', '75', '67', '6B', '6C', '6F']
```

Once you have the tag list you can access any data group using the EPassport object:

```
ep["61"]
ep["75"]
```

The data group is read only once from the data source (the first time the data group is requested).

You can also access data group using the DG name. Each DatGroup object is also a dictionnay where each value is a tag present into the file.

```
>>> dg1 = ep["DG1"]
>>> print dg1 
Reading DG1
{'5F05': '8', '5F04': '0', '5F07': '4', '5F06': '7', '59': '130221', '5F03': 'P<', '5F02': '0', '5F5B': 'ROGER<<OLIVIER<VINCENT<MICHAEL<<<<<<<<<', '5F1F': 'P<BELROGER<<OLIVIER<VINCENT<MICHAEL<<<<<<<<<EH276509<0BEL8406158M1302217<<<<<<<<<<<<<<04', '53': '<<<<<<<<<<<<<<', '5F2C': 'BEL', '5F57': '840615', '5F28': 'BEL', '5F35': 'M', '5A': 'EH276509<'}
```

To know the meaning of a tag, you can use the dictionnary present in the file pypassport.doc9303.tagconverter.py

```
>>> for tag in dg1:
>>>     print tag + "> " + epassport.tagconverter.tagToName[tag] + ": " + str(dg1[tag])
5F05> Check digit - DOB: 8
5F04> Check digit - Doc Number: 0
5F07> Composite: 4
5F06> Expiry date: 7
59> Date of Expiry or valid Until Date: 130221
5F03> Document Type: P<
5F02> Check digit - Optional data (ID-3 only): 0
5F5B> Name of Holder: ROGER<<OLIVIER<VINCENT<MICHAEL<<<<<<<<<
5F1F> MRZ data elements: P<BELROGER<<OLIVIER<VINCENT<MICHAEL<<<<<<<<<EH276509<0BEL8406158M1302217<<<<<<<<<<<<<<04
53> Optional Data: <<<<<<<<<<<<<<
5F2C> Nationality: BEL
5F57> Date of birth (6 digit): 840615
5F28> Issuing State or Organization: BEL
5F35> Sex: M
5A> Document Number: EH276509<
```

When an invalid data group is requested, a DataGroupException is raised. You can access data groups using tag (like before) or using Common, DG1 .. DG16, SecurityData notation.
Have a look at this file for every valid notations: pypassport.doc9303.converter.py

```
>>> try:
>>>     ep["DG33"]
>>> except epassport.datagroup.DataGroupException, msg:
>>>    print msg
The data group 'DG33' does not exist
```

The iterator is also available on the EPassport dictionnary. It will read every available data groups from the epassport

```
for dg in ep:
    print ep[dg]
```

## 3.2 OpenSSL ##

The API needs openssl to perform the security features. It have to know the localization of openssl. The main executable must be in the path. If it is not the case, set manually the complete path to openssl.exe

```
ep.openSslDirectory = "C:\\OpenSSL\\bin\\openssl"
```

## 3.3 Active Authentication ##

The Active Authentication can only be performed using an rfid reader. It does not work with the simulator.

```
>>> try:
>>>     print ep.doActiveAuthentication()
>>> except epassport.activeauthentication.ActiveAuthenticationException, msg:
>>>     print msg
>>> except epassport.iso7816.SimIso7816Exception, msg:
>>>     print msg
True
```

## 3.4 Passive Authentication ##

The Passive Authentication is done in two distinct steps:

  * First verify the DS Certificate contained in the SOD.
To verify the Document Signer Certificate you need the CVCA Certificate. You have to specify the directory containing these certificates, and to ask the hash operation each time new certificates are added into the directory.

If you do not hash the certificates, openssl will not be able to find the CVCA certificate associated with the DS certificate.

```
ep.setCSCADirectory('D:\\workspace\\pypassport\\src\\data\\cert', hash=True)
try:
    print ep.doVerifySODCertificate()
except epassport.passiveauthentication.PassiveAuthenticationException, msg:
    print msg
except epassport.openssl.OpenSSLException, msg:
    print msg
```

  * Once the certificate is verified (or not), you can verify the data group integrity.

If you call it without argument, the verification is done for every epassport
data groups.

The method returns a dictionnary with the DG name as key and a boolean as value.

```
>>> try:
>>>     print ep.doVerifyDGIntegrity()
>>> except epassport.passiveauthentication.PassiveAuthenticationException, msg:
>>>     print msg
>>> except epassport.openssl.OpenSSLException, msg:
>>>     print msg
{'DG15': True, 'DG11': True, 'DG12': False, 'DG2': True, 'DG1': True, 'DG7': True}
```

Or you can give a list of DataGroup object to verify.

```
>>> try:
>>>     l = []
>>>     l.append(ep["DG1"])
>>>     l.append(ep["DG2"])
>>>     print ep.doVerifyDGIntegrity(l)
>>> except epassport.passiveauthentication.PassiveAuthenticationException, msg:
>>>     print msg
>>> except epassport.datagroup.DataGroupException , msg:
>>>     print msg
>>> except epassport.openssl.OpenSSLException, msg:
>>>     print msg
{'DG2': True, 'DG1': True}
```

## 3.5 Information retrieval and data dump ##

Finally you can retrieve the face, the signature, the DS Certificate and the public key from the epassport (if available), and you can write it on disk.

The getSignatures and getFaces method return a list of binary string, and getPublicKey and getCertificate return a text string.

```
signatures = ep.getSignatures()
faces = ep.getFaces()
pubKey = ep.getPublicKey()
DSC = ep.getCertificate()

dgd = epassport.datagroup.DataGroupDump("C:\\tmp")

cpt=0
for sig in signatures:
    dgd.dumpData(sig, "signature" + str(cpt) + ".jpg")
    cpt += 1
    
cpt=0
for face in faces:
    dgd.dumpData(face, "face" + str(cpt) + ".jpg")
    cpt += 1

dgd.dumpData(pubKey, "pubKey.pk")
dgd.dumpData(DSC, "DS.cer")
```

You can also dump some specific data group

```
dgd.dumpDG(ep["DG1"])
```

Or the whole epassport content

```
dgd.dump(ep)
```