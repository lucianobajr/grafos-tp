class AdjNode:
    def __init__(self, data, weight):
        self.vertex = data
        self.weight = weight
        self.next = None
        self.explored = False