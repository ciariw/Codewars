# https://www.codewars.com/kata/52bef5e3588c56132c0003bc
'''
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
'''
def tree_by_levels(node, mapy={}, lvl=0):
    if lvl not in mapy:
        mapy[lvl] = []
    if node is None:
        return []
    tree_by_levels(node.left, mapy, lvl + 1)
    tree_by_levels(node.right, mapy, lvl + 1)
    mapy[lvl].append(node.value)

    if lvl == 0:
        li = []
        for i in mapy:
            li.extend(mapy[i])
        mapy.clear()
        return li
# This took me maybe an hour? I really enjoyed it but I want to improve my speed when solving challenges
