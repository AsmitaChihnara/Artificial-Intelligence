# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:01:27 2018

@author: Asmita
"""
graph = {'A' : set(['B', 'C', 'E']),
         'B' : set([ 'D', 'E', 'A']),
         'C' : set(['A', 'G', 'F']),
         'D' : set(['B', 'E']),
         'E' : set(['A', 'B', 'D']),
         'F' : set(['C']),
         'G' : set(['C'])}

def dfs(graph,start):
        visited, stack = set(), [start]
        #print(stack)
        while stack:
            #print(stack)
            node = stack.pop()
            print(node)
            if node not in visited:
                visited.add(node)
            neighbour=graph[node]
            for v in neighbour:
                if v not in stack and v not in visited:
                    stack.append(v)
            #print(visited)
        return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    #print(queue)
    while queue:
        #print(queue)
        node = queue.pop(0)
        print(node)
        if node not in visited:
            visited.add(node)
        neighbour=graph[node]
        for v in neighbour:
            if v not in queue and v not in visited:
                queue.append(v)
            #print(visited)
    return visited

print('----------dfs----------')
dfs(graph, 'A')
print('----------bfs----------')
bfs(graph, 'A')