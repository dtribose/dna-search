# Quickstart Instructions

## Installation

After unzipping these files:
 - Make sure the PYTHONPATH variable contains the full path of the root directory of this module (dna-search)
 - Use a python version 3.5 or later. Confirm by typing 'python' on the command line and view the output.

Note: current code was only tested on windows powershell command line. Minor changes may be needed for Linux or OSX.

## Running the server

Include instructions here required to start and stop the development server.
This is not applicable - since no Django, or Flask components included.

## Running tests

To run tests: type 'python test/test_search.py'

# Explanation of methods

1. Uses the string find() command to find the first occurrence (loc) of target in reference[0:],
   Then continues to look for the target in reference from that point forward reference[loc+1:]

Get reverse complement of target as follows:
  - First create a list of reverse order character from string.
  - Then converting them to their complement with a simple dictionary lookup.
  - Finally coalescing the list back to a string.

2. Time complexity for a reference of length m, and target of length n (Specifically, to determine locations in the
reference where you can find the target and it's reverse complement).
  - O(m)
  - does not appear to depend on length of target.

# TODO
Issues, suggestions, future plans

If we need to handle human genome that could be an issue, since it is on the order of 3 GB.
  - Test larger genomes
  - Consider how to do db string lookups more quickly

It appears to be almost as fast to calculate results as it is to look it up in dictionary.

Investigate availability of dna/biology libraries for possibly faster timing.

Add Django to create db and gui as requested.

Setup to run in Docker
 
 