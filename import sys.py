from flask import Flask, request, render_template_string, jsonify
from heapq import heappop, heappush

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, goal):
        visited = set()
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            if vertex in visited:
                continue
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in self.graph.get(vertex, []):
                stack.append((neighbor, path + [neighbor]))
        return None

    def bfs(self, start, goal):
        visited = set()
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            if vertex in visited:
                continue
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in self.graph.get(vertex, []):
                queue.append((neighbor, path + [neighbor]))
        return None

    def a_star(self, start, goal, h):
        open_set = [(0, start, [start])]
        g_scores = {start: 0}
        while open_set:
            _, current, path = heappop(open_set)
            if current == goal:
                return path
            for neighbor in self.graph.get(current, []):
                tentative_g_score = g_scores[current] + 1
                if tentative_g_score < g_scores.get(neighbor, float('inf')):
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + h(neighbor, goal)
                    heappush(open_set, (f_score, neighbor, path + [neighbor]))
        return None

def heuristic(a, b):
    return abs(ord(a) - ord(b))