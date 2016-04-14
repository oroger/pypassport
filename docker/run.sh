#!/bin/bash

service pcscd start
#service pcscd status

rm scripts/*.out
rm scripts/*.bin
rm scripts/*.key
rm scripts/*.cer
rm scripts/*.jpg

for file in scripts/*.py
do
  python $file 2>&1 | tee $file.out
done