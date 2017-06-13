#!/usr/bin/python2.7

import os
from sys import argv
from subprocess import call
from ceda_cc import c4

file = argv[1]

GWSDIR = "/group_workspaces/jasmin/cp4cds1/qc/QCchecks/CEDACC-OUTPUT/"

if os.path.exists(file):

    institute, model, experiment, frequency, realm, table, ensemble, version, variable, ncfile = file.split('/')[6:]

    odir = os.path.join(GWSDIR, institute, model, experiment, table, version)
    if not os.path.exists(odir):
        os.makedirs(odir)

    cedacc_args = ['-p', 'CMIP5', '-f', file, '--log', 'multi', '--ld', odir, '--cae', '--blfmode', 'a']
    run_cedacc = c4.main(cedacc_args)
