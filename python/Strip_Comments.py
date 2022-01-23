# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''


def solution(string, markers):
    # Sike!

    cut = True
    cutque = []
    string = list(string)
    for index, i in enumerate(string):

        if i in markers:
            cut = False
            #
            if len(cutque) > 0 and cutque[-1] == ' ':
                cutque.pop(-1)

        if i == '\n':
            cut = True

        if cut:
            cutque.append(i)

    return ''.join(cutque)
# doing slightly more complicated string manipulation.....
