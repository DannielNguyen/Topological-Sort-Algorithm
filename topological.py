from collections import deque

def topological_sort(vertices,edges):
  sorted = []
  if vertices <= 0:
    return sorted
  #initialize graph
  inDegrees = {i:0 for i in range(vertices)}
  graph = {i:[] for i in range(vertices)}
  #build graph
  for edge in edges:
    graph[edge[0]].append(edge[1])
    inDegrees[edge[1]] +=1
        
  sources = deque()
  for i in inDegrees:
    if inDegrees[i] == 0:
      sources.append(i)
  while sources:
    vertex = sources.popleft()
    sorted.append(vertex)
    for i in graph[vertex]: #decrement incoming vertices
      inDegrees[i] -=1
      if inDegrees[i] == 0: #if no vertices add to source
        sources.append(i)
        #check if topological sort is possible
  if len(order) != vertices:
    return []
  return sorted
