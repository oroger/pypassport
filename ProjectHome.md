In 2004, the [ICAO](http://en.wikipedia.org/wiki/International_Civil_Aviation_Organization) published a new version of [Doc9303](http://www2.icao.int/en/MRTD/Pages/Doc9393.aspx) that defines the specifications of the [electronic passports](http://en.wikipedia.org/wiki/Biometric_passport), known as ePassports. These passports, easily recognizable with their logo on the front cover, contain a passive contactless chip featured with some cryptographic mecanisms.

_pyPassport_ is a GPL-friendly tool to read and checks ePassports, developped by Jean-Francois Houzard and Olivier Roger during their Master Thesis achieved in the [Information Security Group](http://www.uclouvain.be/sites/security/) of the [UCL](http://www.uclouvain.be) in Belgium.
pyPassport is currently available as beta version.


---

## News ##
|August 8, 2009|Version 1.0 of pyPassport released|[Source](http://pypassport.googlecode.com/files/pypassport-1.0.zip)|
|:-------------|:---------------------------------|:------------------------------------------------------------------|
|May 18, 2009|Version 0.1a of pyPassport released|[Source](http://pypassport.googlecode.com/files/pypassport-0.1a.zip)|
|May 1, 2009|First Public Release|


---

## pyPassport ##

pyPassport is an API written in [Python](http://python.org) that allows to interact with electronic passports compliant with ICAO Doc9303. The downloadable version is still a work in progress but is stable enough to be tested as a beta version. The API provides an interface with the following functionalities:

  * Perform the Basic Access Control and Secure Messaging;
  * Perform the passive and active authentications;
  * Read the content of the ePassport, including the pictures in JPEG format.
  * Create "valid" auto-signed ePassport content. (require java 1.6)

pyPassport is released under [GNU Lesser General Public License, Version 3](http://www.gnu.org/licenses/lgpl-3.0.txt) License.


---

## Disclaimer ##

Before using pyPassport, you must be sure that you are allowed to read the contactless chip of your passport, according to the laws and regulations of the country that issued it.


---

## Documentation ##

  * [Installation Instructions](http://code.google.com/p/pypassport/wiki/Installation_Instructions)
  * [API User Guide](http://code.google.com/p/pypassport/wiki/API_1_0_User_Guide)
  * [API Usage Example](http://code.google.com/p/pypassport/wiki/API_1_0_Usage_Example)
  * [ePassport Forgery](http://code.google.com/p/pypassport/wiki/Forgery)
  * [Hardware Compatibility](http://code.google.com/p/pypassport/wiki/Hardware_Compatibility)


---

## Known Use ##
  * [ePassportViewer](http://code.google.com/p/epassportviewer/): GUI using pyPassport to read and display the ePassport content.


---

## Dependencies ##
_pyPassport_ uses two tools and several python supporting frameworks:

### Tools ###
  * [OpenSSL](http://www.openssl.org/) for certificate and signature manipulation.
  * [Geojasper](http://dimin.m6.net/software/geojasper/) to handle JPEG2000 image format.

### Supporting frameworks ###
  * [pyasn1](http://pyasn1.sourceforge.net/) to manipulate asn1 data structures.
  * [pyCrypto](http://www.dlitz.net/software/pycrypto/) for de/cipher data.
  * [pyScard](http://pyscard.sourceforge.net/) to communicate with smartcard readers.


---

## Links ##

The [JMRTD](http://jmrtd.org/csca.shtml) website list some Country Signing Certificates found using [Google](http://www.google.com).

You can learn more about electronic passports: [Belgian Biometric Passport does not get a pass...](http://www.dice.ucl.ac.be/crypto/passport/index.html) by Gildas Avoine, Kassem Kalach, and Jean-Jacques Quisquater (2007).


---

## Related softwares ##

  * [Golden Reader Tool](http://www.bsi.de/literat/faltbl/F25GRT.htm) by BSI
  * [JMRTD](http://www.jmrtd.org/): A Free Implementation of Machine Readable Travel Documents (JAVA)
  * [RFIDIOt](http://www.rfidiot.org/): RFID tools (Python)
  * [wzMRTD](http://www.waazaa.org/wzmrtd/index.php?lang=en): ePassport API by Johann Dantant (C++)


---

## Acknowledgment ##

We would like to thank J.-P. Szikora, A. Laurie, M. Oostdijk, I. Etingof, Ph. Teuvens, and M. Vuagnoux for their comments or advices.