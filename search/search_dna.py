
class BadDnaString(Exception):
    """ Special exception for invalid DNA input strings"""
    def __int__(self, msg):
        super().__init__(self, msg)


class DnaLookupTable():
    """ Table for saving results to lookup if available"""
    def __init__(self):
        self.lookup_table = {}

    def search_reference(self, reference, target):
        if reference in self.lookup_table:
            if target in self.lookup_table[reference]:
                return self.lookup_table[reference][target]

        return None

    def add_result(self, reference, target, result):
        if reference not in self.lookup_table:
            self.lookup_table[reference] = {}
        if target not in self.lookup_table[reference]:
            self.lookup_table[reference][target] = result

_lookup = DnaLookupTable()

DICT_COMPLEMENT = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}


def validate_dna(dna_string, valid_elements):
    for char in dna_string:
        if char not in valid_elements:
            return False
    return True


def complement(char):
    """ Returns the complement on the input nucleotide"""
    return DICT_COMPLEMENT[char]

def reverse_complement(dna_string):
    """ return the reverse complement of the input value

    :param dna_string: a DNA string with the letters from the set {A,C,T,G}
    :return: reverse complement of dna_string
    """

    i = len(dna_string) - 1
    rc_list = []
    while i > -1:
        rc_list.append(dna_string[i])
        i -= 1

    assert(len(rc_list) == len(dna_string))

    for i, char in enumerate(rc_list):
        rc_list[i] = complement(char)

    rc = ''.join(rc_list)

    return rc


def search_reference(reference, target, cache=True):
    """ Search for target and reverse-complement (rc) of target in reference.

    :param reference: A DNA sequence consisting of letters from the set {A,C,T,G}, as a string
    :param target: Typically a shorter DNA sequence consisting of same letters as reference, as a string
    :return: a tuple: (total, {'target': [<start-locations], 'rc': [<start_locations]})
    """

    # Todo: would this be faster if we converted to ints and used a numpy array
    # e.g. A -> 1, T -> -1, C -> 2, G -> -2
    # Then compliment would be a simple sign transformation

    valid_elements = ['A', 'C', 'G', 'T']
    if not validate_dna(reference, valid_elements):
        raise BadDnaString("Invalid reference DNA string. Can only contain {}".format(valid_elements))
    if not validate_dna(target, valid_elements):
        raise BadDnaString("Invalid target DNA string. Can only contain {}".format(valid_elements))

    if cache:
        res = _lookup.search_reference(reference, target)
        if res is not None:
            return res, 'db'

    def get_list(r, t):
        found = True
        list = []
        start = 0
        end = len(r)
        while(found):
            location = r.find(t, start, end)
            if location > -1:
                list.append(location)
                start = location + 1
            else:
                found = False
        return list

    target_list = get_list(reference, target)
    target_rc = reverse_complement(target)
    rc_list = get_list(reference, target_rc)

    res = (len(target_list) + len(rc_list), {'target': target_list, 'rc': rc_list})

    if cache:
        _lookup.add_result(reference, target, res)

    return res, 'calc'