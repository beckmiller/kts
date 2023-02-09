from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = []
        stack = [self._root]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.append(node)
            for n in node.outbound[::-1]:
                if n not in visited:
                    stack.append(n)
        return visited

    def bfs(self) -> list[Node]:
        result = []
        queue = [self._root]
        visited = set()

        while queue:
            node = queue.pop(0)
            if node not in visited:
                result.append(node)
                visited.add(node)
                for neighbor in node.outbound:
                    queue.append(neighbor)

        return result






