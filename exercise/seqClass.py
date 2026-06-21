#!/usr/bin/env python
# tells the shell to run this script with the Python interpreter found in the user's environment.

import sys, re
# sys: used here to inspect command-line arguments and exit the program.
# re: regular expressions module, used to validate the sequence and search motifs.

from argparse import ArgumentParser
# Imports ArgumentParser, which helps define and parse command-line arguments.

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# Creates the argument parser object and sets a short description of the program.

parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
# Defines a required argument for the input sequence. The user can provide it as -s or --seq. type=str means the input will be treated as text.

parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
# Defines an optional argument for a motif to search inside the sequence.
# The user can provide it as -m or --motif.

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
# If the script is run with no arguments at all, show the help message
# and exit with status code 1 to indicate incorrect usage.


args = parser.parse_args()
# Parses the arguments provided by the user and stores them in 'args'.

args.seq = args.seq.upper()                 # Note we just added this line
# Converts the sequence to uppercase so validation and searches are case-insensitive.

# Check that the sequence contains only valid IUPAC nucleotide symbols
# This includes standard bases (A,C,G,T,U) and ambiguity codes
if re.search('^[ACGTURYSWKMBDHVN]+$', args.seq):

    # A valid biological sequence should not contain both T and U
    # T corresponds to DNA and U corresponds to RNA
    if 'T' in args.seq and 'U' in args.seq:
        print('Invalid sequence: contains both T and U')

    # If T appears, classify as DNA
    elif 'T' in args.seq:
        print('The sequence is DNA')

    # If U appears, classify as RNA
    elif 'U' in args.seq:
        print('The sequence is RNA')

    # If neither T nor U appears, the sequence could belong to DNA or RNA
    else:
        print('The sequence can be DNA or RNA')

# If characters outside the IUPAC alphabet appear, reject the sequence
else:
    print('The sequence is not a valid DNA/RNA sequence')


if args.motif:
    # This block runs only if the user provided the optional motif argument.

    args.motif = args.motif.upper()
    # Converts the motif to uppercase so the search matches the uppercase sequence.

    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    # Prints a message announcing the motif search.
    # end='' keeps the cursor on the same line so the result can be appended.
    if re.search(args.motif, args.seq):

        print("FOUND. Yai!")
        # If the motif pattern is found anywhere in the sequence, print success.

    else:
        print("NOT FOUND")
        # If the motif is not found, print failure.

