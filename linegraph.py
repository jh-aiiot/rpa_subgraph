# Recommendation Subgraph Generation
# Version 1.4
# Programmed by Joohyun Kim
# AIIoT Lab, Ajou University, Republic of Korea

# Notation
# VD : Value-described
# ED : Existence-described

# Required Libraries
import random
import pandas
import numpy
import networkx
import matplotlib.pyplot

from pyvis.network import Network

# Settings
entity_num = 50                         # 'entity_num' is the total number of entities.
entity_list = []                        # 'entity_list' is the list of all entities.
random.seed(1)                          # Seed is given for reproducibility


class Entity:
    def __init__(self,
                 num_of_vd_resource,
                 num_of_ed_resource,
                 selection_limit,
                 selection_probability):
        self.num_of_vd_resource = num_of_vd_resource
        self.num_of_ed_resource = num_of_ed_resource
        self.selection_limit = selection_limit
        self.selection_probability = selection_probability

    def resource_vd(self):
        amount_resource_vd = []
        for _ in range(self.num_of_vd_resource):
            chosen = random.choices(self.selection_limit[_],
                                    cum_weights=self.selection_probability[_],
                                    k=1)
            amount_resource_vd.append(chosen)
        return amount_resource_vd

    def resource_ed(self):
        amount_resource_ed = []
        for _ in range(self.num_of_ed_resource):
            chosen = random.choices([0, 1],
                                    cum_weights=self.selection_probability[self.num_of_vd_resource+_],
                                    k=1)
            amount_resource_ed.append(chosen)
        return amount_resource_ed

    def set_resource(self):
        resource_vd_list = self.resource_vd()
        resource_ed_list = self.resource_ed()
        return resource_vd_list+resource_ed_list

    def print_resource(self):
        resource_vd_list = self.resource_vd()
        resource_ed_list = self.resource_ed()
        print(resource_vd_list+resource_ed_list)


class Linegraph:
    def __init__(self,
                 original_list):
        self.original = original_list
        self.num_entity = len(original_list)
        self.num_resource = len(original_list[0])
        self.line_resource_list = []
        self.line_entity_list = []

        # Initializing function
        self.line_graphing()
        self.line_graph_trimming_mild()
        self.line_graph_trimming_hard()

    def line_graphing(self):
        for s in range(self.num_entity):
            for t in range(self.num_entity):
                if s == t:
                    continue
                else:
                    self.line_entity_list.append([s, t])
                    resource_list = []
                    for r in range(self.num_resource):
                        new_r = self.original[s][r][0] - self.original[t][r][0]
                        resource_list.append([new_r])
                    self.line_resource_list.append(resource_list)
        return 0

    def line_graph_trimming_hard(self):
        num_line_graph = len(self.line_resource_list)
        num_line_graphs = len(self.line_entity_list)
        new_line_resource_list = []
        new_line_entity_list = []

        # Error!
        if num_line_graph != num_line_graphs:
            print("There is a problem in making line graphs.")

        for ln in range(num_line_graph):
            done = 0
            for r in range(self.num_resource):
                if self.line_resource_list[ln][r][0] < 0:
                    done += 1
            if done:
                continue
            else:
                new_line_resource_list.append(self.line_resource_list[ln])
                new_line_entity_list.append(self.line_entity_list[ln])

        self.line_resource_list = new_line_resource_list
        self.line_entity_list = new_line_entity_list

        return 0
    
    def line_graph_trimming_mild(self):
        num_line_graph = len(self.line_resource_list)
        num_line_graphs = len(self.line_entity_list)
        new_line_resource_list = []
        new_line_entity_list = []

        # Error!
        if num_line_graph != num_line_graphs:
            print("There is a problem in making line graphs.")
            
        activated_diff = numpy.logical_and(relu(diff).tolist(), numpy.ones(num_rscTypes)).astype(numpy.int8)

        for ln in range(num_line_graph):
            for r in range(self.num_resource):
                
                self.line_resource_list[ln]=numpy.logical_and(relu(self.line_resource_list[ln][r]).tolist(), numpy.ones(num_resource)).astype(numpy.int8)

                new_line_resource_list.append(self.line_resource_list[ln])
                new_line_entity_list.append(self.line_entity_list[ln])

        self.line_resource_list = new_line_resource_list
        self.line_entity_list = new_line_entity_list

        return 0

    def get_line_graph_list(self):
        return self.line_resource_list, self.line_entity_list

    def get_left_node_list(self):
        source_node = [0]
        done = 1

        if done:
            for s in source_node:
                new_source_node = []
                for n in range(len(self.line_entity_list)):
                    if s == self.line_entity_list[n][0]:
                        new_source_node.append(self.line_entity_list[n][1])
            temp_source_node = list(set(source_node + new_source_node))

            if source_node == temp_source_node:
                done = 0
            else:
                source_node = temp_source_node

        return source_node

    def get_left_edge_list(self):
        source_node = self.get_left_node_list()
        left_edge_list = []

        for n in range(len(self.line_entity_list)):
            left = 0
            if self.line_entity_list[n][0] in source_node:
                left += 1
                if self.line_entity_list[n][1] in source_node:
                    left += 1
                else:
                    continue
            else:
                continue

            if left == 2:
                left_edge_list.append(self.line_entity_list[n])

        return left_edge_list


# Property of default "entity_list"
print("Checking : entity list is empty.")
print("Empty :", len(entity_list))
# print(entity_list)

for e in range(entity_num):
    # "A" is a type of entity.
    # Use capital case alphabet to show different types of entity.
    # We only make one type of entity in this program.
    A = Entity(3,                           # Number of VD Resources
               2,                           # Number of ED Resources
               # 2023.03.02 Resource number increment
               # Selection limit for VD Resources
               [[0, 128, 256, 512], [0, 4, 8, 16, 32], [0, 4, 8, 16, 32]],
               # Selection Probability for the VD Resources and the ED Resources
               [[0.3, 0.3, 0.2, 0.2], [0.2, 0.1, 0.2, 0.3, 0.2], [0.2, 0.1, 0.2, 0.3, 0.2], [0.3, 0.7], [0.4, 0.6]])
    temp = A.set_resource()
    entity_list.append(temp)

# Property of processed "entity_list"
print("\nChecking : entity list is full.")
print("Total number of entities :", len(entity_list), "\nThe number of resources :", len(entity_list[0]))

# Visualizing Linegraph
linegraph_dataframe = pandas.DataFrame(numpy.array(Linegraph(entity_list).get_left_edge_list()),
                                       columns=['Source', 'Target'])

G = networkx.Graph()
G = networkx.from_pandas_edgelist(linegraph_dataframe,
                                  source='Source',
                                  target='Target')

print("\nGraph information")
print("The produce linegraph is a", G)

matplotlib.pyplot.figure(figsize=(10, 8))
networkx.draw_shell(G, with_labels=True)

matplotlib.pyplot.show()
