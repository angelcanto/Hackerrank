#!/usr/bin/python
from collections import deque
def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    S = deque()
    dictionary = {}
    discovered = []
    explored = []
    path = []
    S.append((pacman_r,pacman_c))
    discovered.append((pacman_r,pacman_c))
    while len(S) != 0:
        v = S.popleft()
        explored.append(v)
        if v[0] == food_r and v[1] == food_c:
            #FOOD!!
            break
        exp = ExpandNode(v,grid,r,c,S) 
        for e in exp:
            if e not in discovered:
                S.append(e)
                dictionary[e]=v
                discovered.append(e)
    #GET EXPLORED
    print len(explored)
    for n in explored:
        print str(n[0]) + " " + str(n[1])
    #GET PATH
    node = dictionary[(food_r,food_c)]
    path.insert(0,(food_r,food_c))
    path.insert(0,node)
    while node != (pacman_r,pacman_c):
        node = dictionary[(node[0],node[1])]
        path.insert(0,node)
    print len(path) - 1
    for n in path:
        print str(n[0]) + " " + str(n[1])
    return

def ExpandNode(node, grid, r, c,S):
    more_nodes = deque()
    #check UP
    if node[0] != 0:
        if grid[node[0]-1][node[1]] != '%':
            more_nodes.append((node[0]-1,node[1]))
    #check LEFT
    if node[1] != 0:
        if grid[node[0]][node[1]-1] != '%':
            more_nodes.append((node[0],node[1]-1))
    #check RIGHT
    if node[1] != c-1:
        if grid[node[0]][node[1]+1] != '%':
            more_nodes.append((node[0],node[1]+1))
    #check DOWN
    if node[0] != r-1:
        if grid[node[0]+1][node[1]] != '%':
            more_nodes.append((node[0]+1,node[1]))
    return more_nodes
pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)
