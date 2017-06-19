#!/bin/bash

odir=$lotusLogsCF2
mkdir -p $odir

for batch in $(seq 0 101); do
    bsub -o ./$odir/%J.out -W 24:00  python2.7 batch_cf_check.py $batch
done
