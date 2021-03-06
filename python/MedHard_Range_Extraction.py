# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
'''
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''
def solution(args):
    finali = []
    if len(args) < 2:
        return args
    fun = []
    # Assembly
    for index,i in enumerate(args):
        fun.append(i)
        if i + 1 != args[(index+1)%(len(args))]:
            if len(fun) != 2:
                finali.append(fun)
            else:
                finali.append([fun[0]])
                finali.append([fun[-1]])
            fun = []
    # Post processing
    final = []
    for i in finali:
        if len(i) > 1:
            final.append(f"{i[0]}-{i[-1]}")
        else:
            final.append(str(i[0]))
    return ",".join(final)
# Pretty cool stuff here
