#!/bin/bash

mkdir -p lotus-logs

for batch in $(seq 0 101); do
    bsub -o ./lotus-logs/%J.out -W 04:00  python2.7 batch_cf_check.py batch
done
