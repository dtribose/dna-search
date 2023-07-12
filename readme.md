# Quickstart Instructions

## Installation

After unzipping these files:
 1. Make sure the PYTHONPATH variable contains the full path of the root directory of this module (dna-search)
 2. Use a python version 3.5 or later. Confirm by typing 'python' on the command line and view the output.
 3. Either (a) make sure pyTest is installed, or 
           (b) create a new virtual environment and run 'pip install pyTest'.

Note: 
  current code was only tested on windows powershell command line. 
  Minor changes to the instructions may be needed for Linux or Mac OS.


## Running tests

To run tests, type:
    python -m pytest --verbose

Should contain 8 tests and the first 7 should pass on all systems.
The last is a speed test, and would just indicate that your system is particularly slow, or you have resource constraints.

# Explanation of methods and time complexity

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

## TODO

# Issues

If we need to handle human genome that could be an issue, since it is on the order of 3 GB.
  - Test larger genomes
  - Consider how to do db string lookups more quickly

# Suggestions & Future plans

Compare speed of calculating results vs. looking it up in dictionary.

Investigate availability of other dna/biology libraries for possibly faster timing.

Use Django or Flask to add a gui front end.

Implement an SQL backend with PostgreSQL or other DB.

Setup to run in Docker
 
 
