# https://www.codewars.com/kata/52774a314c2333f0a7000688
'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''

# First attempt
def valid_parentheses(string):
    oc = []
    for i, c in enumerate(string):
        #two states, open and closed. Starts from open and ends with closed. When closed, delete open
        #if you close without opening, return false
        if string[i] == "(":
            oc.append("open")
        if string[i] == ")":
            if len(oc) > 0 and oc[len(oc)-1] == "open":
                oc.remove(oc[len(oc)-1])
            else:
                return False
        i += 1
    if len(oc) != 0:
        return False
    return True

# Second attempt after more research
def valid_parentheses(string):
    c = str()
    for i in string:
        if i == "(" or i == ")":
            c += i
        c = c.replace("()", "")
    return len(c) == 0