#!/bin/bash

odir=lotus-logs-cedacc2
mkdir -p $odir

for batch in $(seq 0 101); do
    . setup_venv.sh
    bsub -o ./$odir/%J.out -W 24:00  python2.7 batch_cedacc_checks.py $batch
done
