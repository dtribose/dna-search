# Quickstart Instructions

## Installation

The setup is trivial. You only need a version of python in the 3.x family

## Running the server

Include instructions here required to to start and stop the development server.
This is n/a

## Running tests

Include instructions here for how to run tests.
type: python -m test/test_search.py

# Explanation of methods

1. In this section please explain the method or methods you have used here.
   Include both why and how they work in general terms.

Uses the string find() command to find the first occurrence (loc) of target in reference[0:],
Then continues to look for the target in reference from that point forward reference[loc+1:]

Get reverse complement of target as follows:
  First create a list of reverse order character in string.
  Then converting them with a simple dictionary lookup.
  Finally coalescing the list back to a string.

2. Also include an estimate of the time complexity required for a reference of length m, and target of length n.
   Specifically, to determine locations in the reference where you can find the target and it's reverse complement.

O(m)
does not appear to depend on length of target.

# TODO

Explain any problems that you encountered and possible solutions you would implement if you had time.
This is also a good place to describe any UI and operational improvement you might want to make in the future.

If we need to handle human genome that could be an issue, since it is on the order of 3 GB.
It appears to be almost as fast to calculate results as it is to look it up in dictionary.
#   d n a - s e a r c h  
 