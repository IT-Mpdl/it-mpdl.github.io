#!/usr/bin/python3

import sys
import os
import uuid

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

data   = sys.stdin.read()
nuuid  = str(uuid.uuid1())
nfn    = "../json-queue/gln_" + nuuid + ".json"
fp     = open(nfn, "w+")

#eprint("gln - nfn = ", nfn)

fp.write(data)
fp.close()

# Return empty body
print("Content-Type: text/html")
print("")

