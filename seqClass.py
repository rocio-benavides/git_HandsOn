#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = 
"Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA') # DNA
    elif re.search('U', args.seq):
        print ('The sequence is RNA') # RNA
    else:
        print ('The sequence can be DNA or RNA') # DNA or RNA
else:
    print ('The sequence is not DNA nor RNA') # not DNA nor RNA
