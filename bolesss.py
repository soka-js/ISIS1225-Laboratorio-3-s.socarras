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

