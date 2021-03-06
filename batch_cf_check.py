#!/usr/bin/python2.7

from sys import argv
from subprocess import call
start = int(argv[1])
files_per_batch = 2000
srt_idx = start * files_per_batch
end_idx = srt_idx + files_per_batch

with open("cp4cds_filelist2.log", 'r') as fr:
    files = fr.readlines()

for file in files[srt_idx: end_idx]:
    run_cmd = ["python2.7", "run_cf_checker.py", file.strip()]
    run = call(run_cmd)
    if run != 0:
        print "ERROR RUNNING %s" % run_cmd
