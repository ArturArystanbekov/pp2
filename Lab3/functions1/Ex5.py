from itertools import permutations

def permutation(input_string):
    strings = permutations(input_string)
    for i in strings:
        print(''.join(i))


input_string = input("Enter the string: ")
permutation(input_string)