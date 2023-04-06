import random
from functools import reduce
from utils import data_to_dictionary

class PageRankDiGraph:
    def __init__(self,data):
        self.data=data
        self.link_dict = data_to_dictionary(data)  
    def __len__(self):
        return len(self.data)
    def get_nodes(self):
        sung_to = reduce(lambda x, y: x+y, self.link_dict.values())
        singer = list(self.link_dict.keys())
        return list(set(sung_to + singer)) 
    def __contains__(self, item):
        return item in self.link_dict
    def __str__(self):
        return f"PageRankDiGraph with {0} nodes and {1} edges.".format(len(get_nodes()), __len__())
    def __add__(self, other):
        return PageRankDiGraph(self.data + other.data)
    def linked_by(self, x):
        return self.link_dict[x]


class PageRankIterator:
    def __init__(self, graph, iteration_limit, jump_prob):
        if not isinstance(graph, PageRankDiGraph):
            raise TypeError('Must be an instance of PageRankDiGraph')
        self.graph = graph
        self.iteration_limit = iteration_limit
        self.jump_prob = jump_prob
        self.iter = 0
        self.current_state = "hamilton"
    def follow_link(self):
        
        try:
            links = self.graph.linked_by(self.current_state)
            next_state = random.choice(links)
            if next_state != self.current_state:
                self.current_state = next_state
            else:
                self.teleport()
        except KeyError:
            self.teleport()
    def teleport(self):
        self.current_state = random.choice(self.graph.get_nodes())
    def __iter__(self):
        self.iter = 0
        return self
    def __next__(self):
        if self.iter >= self.iteration_limit:
            raise StopIteration
        self.iter += 1
        if random.random() < self.jump_prob:
            self.follow_link()
        if random.random() < 1-self.jump_prob:
            self.teleport()
        return self.current_state
    
class IterablePageRankDiGraph(PageRankDiGraph):
    def __init__(self, data, iteration_limit=20, jump_prob=0.75):
        super().__init__(data)
        self.iteration_limit = iteration_limit
        self.jump_prob = jump_prob
    def __str__(self):
        return f"IterablePageRankDiGraph with {0} nodes and {1} edges.".format(len(self.get_nodes()), len(self.data))
    def __iter__(self):
        return PageRankIterator(self, self.iteration_limit, self.jump_prob)

# Implement class IterablePageRankDiGraph from scratch here!
