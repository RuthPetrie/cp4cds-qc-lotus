#!/usr/bin/python2.7

import os
from sys import argv
from subprocess import call

file = argv[1]

GWSDIR = "/group_workspaces/jasmin/cp4cds1/qc/CFchecks/CF-OUTPUT/"
AREATABLE = "/group_workspaces/jasmin/cp4cds1/qc/CFchecks/area-type-table.xml"
STDNAMETABLE = "/group_workspaces/jasmin/cp4cds1/qc/CFchecks/cf-standard-name-table.xml"
institute, model, experiment, frequency, realm, table, ensemble, version, variable, ncfile = file.split('/')[6:]

odir = os.path.join(GWSDIR, institute, model, experiment, table, version)
if not os.path.exists(odir):
    os.makedirs(odir)

cf_out_file = os.path.join(odir, ncfile.replace(".nc", ".cf-log"))
cf_err_file = os.path.join(odir, ncfile.replace(".nc", ".cf-err"))


run_cmd = ["cf-checker", "-a", AREATABLE, "-s", STDNAMETABLE, "-v", "auto", file]
cf_out = open(cf_out_file, "w")
cf_err = open(cf_err_file, "w")
call(run_cmd, stdout=cf_out, stderr=cf_err)
cf_out.close()
cf_err.close()
