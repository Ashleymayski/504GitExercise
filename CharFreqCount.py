def count_frequencies(sequence):
    '''
    Takes an iterable (e.g., a string) and returns a dictionary 
    where the keys are unique elements from the input, and the 
    values are the count of occurrences of those elements.
    
    Args:
        a (iterable): An iterable, such as a string, where elements 
                      are counted.
    
    Returns:
        dict: A dictionary with elements as keys and their frequency 
              of occurrence as values.
    
    Example:
        >>> count_frequencies('ATCTGACGCGCGCCGC')
        {'A': 2, 'T': 2, 'C': 6, 'G': 5}

    '''
    frequencies = dict()
    for element in sequence:
        if element not in frequencies:
            frequencies[element] = 1
        else:
            frequencies[element] += 1
    return frequencies

def print_relative_frequencies(a):
    '''
 Takes a frequency dictionary and prints the relative frequency 
    of each key in the dictionary.

    Args:
        a (dict): A dictionary with elements as keys and their 
                  frequency of occurrence as values.
    
    Example:
        >>> print_relative_frequencies({'A': 2, 'T': 2, 'C': 6, 'G': 5})
        freqs
        A:0.11764705882352941
        T:0.11764705882352941
        C:0.35294117647058826
        G:0.29411764705882354
    """
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b] / total))
    '''
    print('freqs')
    total_count = float(sum([a[element] for element in a.keys()]))
    for element in a.keys():
        print(element + ':' + str(a[element]/total_count))

print_relative_frequencies(count_frequencies('ATCTGACGCGCGCCGC'))
