class Graph_ES:
    def __init__(self, V = None, E = None):
        self._V = set()
        self._E = set()
        if V != None:
            for i in V: self.add_vertex(i)
        if E != None:
            for i in E: self.add_edge(i)

    def __len__(self):
        return len(self._V)

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, v):
        self._V.add(v)

    def remove_vertex(self, v):
        if v not in self._V: raise KeyError
        else: self._V.remove(v)

    def add_edge(self, e):
        self._E.add(e)

    def remove_edge(self, e):
        if e not in self._E: raise KeyError
        else: self._E.remove(e)

    def _neighbors(self, v):
        return (j for i, j in self._E if i == v)


class Graph_AS:
    def __init__(self, V = None, E = None):
        self._V = set()
        self._nbrs = dict()
        if V != None:
            for i in V: self.add_vertex(i)
        if E != None:
            for i in E: self.add_edge(i)

    def __len__(self):
        return len(self._V)

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, v):
        self._V.add(v)

    def remove_vertex(self, v):
        if v not in self._V: raise KeyError
        else: self._V.remove(v)

    def add_edge(self, e):
        if e[0] not in self._nbrs: self._nbrs[e[0]] = {e[1]}
        else: self._nbrs[e[0]].add(e[1])

    def remove_edge(self, e):
        if e[0] not in self._nbrs: raise KeyError
        else:
            self._nbrs[e[0]].remove(e[1])
            if len(self._nbrs[e[0]]) == 0: self._nbrs.pop(e[0])
        
    def _neighbors(self, v):
        return iter(self._nbrs[v])