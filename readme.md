# Quickstart Instructions

## Installation

The setup is trivial. You only need a version of python in the 3.x family

## Running the server

Include instructions here required to to start and stop the development server.
This is n/a

## Running tests

To run tests: type 'python -m test/test_search.py'

# Explanation of methods

1. Uses the string find() command to find the first occurrence (loc) of target in reference[0:],
   Then continues to look for the target in reference from that point forward reference[loc+1:]

Get reverse complement of target as follows:
  - First create a list of reverse order character in string.
  - Then converting them with a simple dictionary lookup.
  - Finally coalescing the list back to a string.

2. Time complexity for a reference of length m, and target of length n (Specifically, to determine locations in the
reference where you can find the target and it's reverse complement).
  - O(m)
  - does not appear to depend on length of target.

# TODO
Issues, suggestions, future plans

If we need to handle human genome that could be an issue, since it is on the order of 3 GB.
  - Test larger genomes
  - How to do db comparisons more quickly

It appears to be almost as fast to calculate results as it is to look it up in dictionary.

Of course, investigate real dna/biology libraries for faster timing.
 
 