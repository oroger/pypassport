# ePassport Viewer #

by

Jean-François Houzard (jhouzard@gmail.com)

Olivier Roger (olivier.roger@gmail.com)


http://sites.uclouvain.be/security/epassport.html



## DISCLAIMER ##
Before using _ePassport_ _Viewer_, you must be sure that you are allowed to read

the contactless chip of your passport, according to the laws and

regulations of the country that issued it.


## PURPOSE ##
This program reads ePassport and display the result on screen.

It allows any ePassport holder to view its content.


## INSTALLATION ##


The _ePassport_ _Viewer_ package uses _distutils_ for installation:

> $ tar zxf epassportviewer-0.1.tar.gz
> $ cd epassportviewer-0.1
> $ python setup.py install



## FEATURES ##

_ePassport_ _Viewer_:
  * reads the passport and display the result on screen.
  * can perform security mechanism as explained in DOC 9303 standard:
    * Basic Access Control (BAC);
    * Secure Messaging (SM);
    * Active Authentication (AA);
    * Passive Authentication (PA).
  * can save data in many file format (PDF, XML, Binary).
  * can extract data contained in the RFID tag (Face, Signature, Public Key, ...).
  * can analyse a passport and report specificities generating a 'Finger Print'.
  * is cross platform (windows, linux, mac).
  * is opensource.

## TECHNICAL DETAILS ##
This program is written in [Python](http://www.python.org/).
A similar API exists in Java and is called [JMRTD](http://www.jmrtd.org/).

## REQUIREMENTS ##
No requirements.
Unzip and launch the ePassportViewer.exe.

## FAQ ##
  * Why is it called ePassport Viewer ?
Because it allows the user to see the digital content of the new biometric passports.

  * Why choose Python ?
ePassport Viewer uses the pyPassport API which is written in Python.
Python provides: Efficiency, readability, portability, large standard libraries.

  * What smartcard reader are supported by ePassport Viewer ?
At the moment pyPassport handle generic PCSC readers.
Passport reading have been successfully performed with the following smartcard readers:
    * Omnikey 5321;
    * ACS ACR 122.
A specific module has been written for the latter.

## LICENCE ##
_ePassport_ _Viewer_ is released under GNU/GPL 3 license terms.
Full text available here in the [GNU GPL, version 3 LICENSE](WikiSyntax.md) file, present in this package.

## USAGE ##
All you should know to use the software is available in the [ePassport Viewer User Manual](WikiSyntax.md).

## HISTORY ##
  * 0.2b (2009-05-02):
    * Windows: Try to start the smartcard service if not running.
  * 0.2a (2009-05-01):
    * Windows: Resolved the pyasn1 problem on startup.
  * 0.2 (2009-04-30):
    * First public release. GPL 3 license.