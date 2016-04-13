#!/bin/bash

service pcscd start
#service pcscd status

rm scripts/*.out

for file in scripts/*.py
do
  python $file 2>&1 | tee $file.out
done