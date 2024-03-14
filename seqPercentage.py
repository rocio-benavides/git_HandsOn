import sys, re
from argparse import ArgumentParser
from collections import Counter

# input
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# classify the sequence
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq):
        print('The sequence is RNA')
    elif re.search('U', args.seq) and re.search('T', args.seq):
        print('The sequence is not DNA nor RNA')
    else:
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not valid DNA or RNA')

# Calculate and give the percentage of each nucleotide
sequence_counter = Counter(args.seq)
total_nucleotides = len(args.seq)
print("\nNucleotide percentages:")
for nucleotide, count in sequence_counter.items():
    percentage = (count / total_nucleotides) * 100
    print(f"{nucleotide}: {percentage
