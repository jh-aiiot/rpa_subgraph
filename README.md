# rpa_subgraph

This repository contains source code of generating subgraph from a network.
The generating operation focuses on trimming edges between the nodes.

* Operation
1. Get resource data of all nodes.
2. Generate a whole network.
3. Convert the original network into a linegraph network.
4. "Given the condition," delete the nodes of the linegraph network.
5. Re-convert the modified linegraph network into the orignal network scheme.

The given condition can vary.
** Default condition : Leave only the links with all data above zero.

The source code visualizes the resulting network.
