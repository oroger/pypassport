# 1. Python #

[Install python 2.6](http://python.org/download/releases/2.6.2/)

Add the python directory to the path variable displayed in the Environment Variable panel (Windows Control Panel > System > Advanced > Environment Variables).

# 2. Dependances #

There are two kind of dependences. The first ones are for the basic ePassport data groups reading and verification procedures such as Active Authentication and Passive Authentication. The seconds are for the ePassport forgery such as data group creation and the applet installation on the java card.

## 2.1 ePassport Reading and Verification ##

### 2.1.1 Setup tool ###

  1. [Download setuptools sources](http://pypi.python.org/pypi/setuptools)
  1. Unzip it
  1. cd setuptools-x.x
  1. python setup.py install

### 2.1.2 pyCrypto ###

  1. [Download pycrypto-2.0.1.win32-py2.6.exe](http://www.voidspace.org.uk/python/modules.shtml#pycrypto)
  1. Install it

### 2.1.3 pyasn1 ###
  1. [Download pyasn1 sources](http://sourceforge.net/projects/pyasn1/files/)
  1. Unzip it
  1. cd pyasn1-x.x.x
  1. python setup.py install

### 2.1.4 pyscard ###

  1. [Download pyscard-1.6.8.win32-py2.6.msi](http://sourceforge.net/projects/pyscard/files/)
  1. Install it

### 2.1.5 OpenSSL ###

  1. [Download Win32 OpenSSL v0.9.8k Light](http://www.slproweb.com/products/Win32OpenSSL.html)
  1. Install it
  1. Add the OpenSSL/bin directory to the path variable displayed in the Environment Variable panel.

## 2.2 ePassport Forgery ##

### 2.2.1 Data Groups Forgery ###

The following dependence is needed for the data group DG2 forgery.

#### 2.2.1.2 PIL ####

  1. [Download Python Imaging Library 1.1.6 for Python 2.6](http://www.pythonware.com/products/pil/)
  1. Install it

### 2.2.2 ePassport emulator uploading ###

The following dependences are requries if you plan to upload the dexlab applet on your
java card using the pyPassport API, for later upload the forger data groups.

### 2.2.2.1 GPShell ###
  1. [Download GPShell](http://sourceforge.net/projects/globalplatform/)
  1. Unzip it
  1. Add the GPShell-x.x.x directory to the path variable displayed in the Environment Variable panel.

### 2.2.2.2 dexlab ePassport emulator ###
  1. [Download ePassport emulator](http://www.dexlab.nl/downloads.html)

The applet will be later uploaded to the JCOP card of your choice.


# 3. pyPassport installation #

  1. [Download pyPassport 1.0](http://pypassport.googlecode.com/files/pypassport-1.0.zip)
  1. Unzip it
  1. cd pypassport-1.0
  1. python setup.py install

[You can then follow the user guide to learn how to use the API](http://code.google.com/p/pypassport/wiki/API_1_0_User_Guide), or [try the working example.](http://code.google.com/p/pypassport/wiki/API_1_0_Usage_Example)
