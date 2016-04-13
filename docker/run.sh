#!/bin/bash

service pcscd start
#service pcscd status

for file in scripts/*.py
do
  python $file
done