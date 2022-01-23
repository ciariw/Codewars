# https://www.codewars.com/kata/520446778469526ec0000001
'''
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''
# Second attempt
def same_structure_as(original, other):
    if type(original) is list and type(other) is list:
        if len(original) == len(other):
            for i, j in enumerate(original):
                if type(j) is list:
                    if not same_structure_as(j, other[i]):
                        return False
        else:
            return False
    else:
        if type(original) != type(other):
            return False

    return True

# First attempt
def same_structure_as(original, other, mapa={}, layer=1):
    mapa[layer] = []
    if type(original) is list and type(other) is list:
        if len(original) == len(other):
            for i, j in enumerate(original):
                if type(j) is list:
                    mapa[layer].append("L")
                    if not same_structure_as(j, other[i], mapa, layer + 1):
                        return False
                else:
                    mapa[layer].append("N")
        else:
            return False
    else:
        if type(original) != type(other):
            return False
    if layer == 1:
        return True
    return mapa