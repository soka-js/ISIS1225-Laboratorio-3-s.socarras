class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        # Diccionario para almacenar el color de cada nodo
        color = {}

        for node in range(len(graph)):
            if node not in color:
                # Iniciar BFS desde este nodo
                queue = deque([node])
                color[node] = 0  # Asignar color 0 al nodo inicial

                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if neighbor not in color:
                            # Asignar color opuesto al del nodo actual
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        else:
                            # Si el vecino ya tiene el mismo color, no es bipartito
                            if color[neighbor] == color[current]:
                                return False
        return True


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Número de nodos en el grafo
        n = len(edges)
        
        # Construir la lista de adyacencia
        adj = [[] for _ in range(n + 1)]  # Los nodos están etiquetados de 1 a n

        for u, v in edges:
            # Añadir aristas al grafo
            adj[u].append(v)
            adj[v].append(u)
            
            # Verificar si se crea un ciclo al agregar esta arista
            visited = [False] * (n + 1)
            if self.is_cyclic(u, adj, visited, -1):
                return [u, v]
        
        return []

    def is_cyclic(self, v, adj, visited, parent):
        # Marcar el nodo actual como visitado
        visited[v] = True

        # Recorrer los nodos adyacentes
        for i in adj[v]:
            if not visited[i]:
                if self.is_cyclic(i, adj, visited, v):
                    return True
            elif i != parent:
                return True
        return False


from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        count = 0

        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses

        
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        visited = {}

        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]

            clone = Node(current_node.val)
            visited[current_node] = clone

            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
