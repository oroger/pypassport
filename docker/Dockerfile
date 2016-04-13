FROM ubuntu:14.04

MAINTAINER Olivier Roger <"Olivier.Roger@gmail.com">
ENV refreshed_at 20160413

RUN apt-get update

# Install dependencies for USB Smartcard Reader
RUN apt-get install -y pcscd libpcsclite1 pcsc-tools libccid git wget swig usbutils 

# Install pypassport dependencies
RUN apt-get install -y python python-setuptools python-imaging python-pyscard python-crypto python-pyasn1 

# Checkout sources from Github ...
RUN git clone https://github.com/oroger/pypassport.git
WORKDIR pypassport/pypassport/src
# Switch to release 1.1.0 (comment to use master instead)
RUN git checkout dev-feat-20160413-dump-no-signature
# ... and install from source
RUN python setup.py install

# Add Docker run script to start the pcscd service before running the script
ADD scripts/ ./scripts
ADD run.sh ./run.sh
# Default entry point
CMD ./run.sh
