# 📁 Shortest Path: Dijkstra's Algorithm

> A Python implementation of Dijkstra's algorithm that finds the shortest path between nodes in a weighted graph using an adjacency matrix.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Learning](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

---

## 📌 About

This project implements Dijkstra's algorithm, one of the most important graph algorithms in computer science, used in real-world applications like GPS navigation, network routing, and map services. Given a weighted adjacency matrix representing a graph, the function finds the shortest distance and exact path from a starting node to either one specific target or all other nodes. Built to understand graph representation, greedy algorithms, and path tracking.

---

## 🧠 What I Learned

- **Adjacency matrix representation** — Storing a graph as a 2D list where each value represents the edge weight between two nodes, using `float('inf')` to indicate no direct connection between them
- **Dijkstra's greedy approach** — At each step, picking the unvisited node with the smallest known distance and using it to update its neighbors — a greedy strategy that guarantees the shortest path in graphs with non-negative weights
- **Parallel path tracking** — Maintaining a `paths` list alongside `distances` so that whenever a shorter route is found, both the distance and the full path are updated together
- **`visited` array** — Marking nodes as visited once their shortest distance is finalized, preventing them from being reconsidered and causing incorrect updates
- **Generator expressions for formatting** — Using `(str(n) for n in paths[node_no])` to lazily convert node numbers to strings before joining them into a readable path like `0 -> 2 -> 3 -> 5`
- **Optional target node** — Using `target_node=None` as a default parameter so the function can either find the path to one specific node or compute all shortest paths from the start in a single call
- **`float('inf')` as a sentinel value** — Using `INF` to represent unreachable nodes and as the starting comparison value when searching for the minimum distance node each iteration

---

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core language |

---

## 💡 How It Works

The graph is represented as a 6-node adjacency matrix. `shortest_path(matrix, start, target)` runs Dijkstra's algorithm from the start node and prints the shortest distance and path to the target, or to all nodes if no target is specified.

```
Graph (6 nodes):

    0 --5-- 1
    |       |  \
    3       1    2
    |       |      \
    2 --1-- 2 --1-- 3
    |       |       |
   11       5       3
    |       |       |
    4       4       5
```

**Example output:**
```
0-5 distance: 6
Path: 0 -> 2 -> 1 -> 5

0-4 distance: 8
Path: 0 -> 2 -> 4

0-3 distance: 4
Path: 0 -> 2 -> 3
```

---

## 🚀 Future Improvements

- [ ] Visualize the graph and highlighted shortest path using `matplotlib`
- [ ] Support adjacency list representation as an alternative to the matrix
- [ ] Add negative weight detection and raise an error, Dijkstra's does not work with negative edges
- [ ] Implement A* search as a comparison, a heuristic-guided improvement on Dijkstra's for spatial graphs

---

## 📂 Project Structure

```
shortest-path/
│
├── README.md
└── ShortestPathAlgorithm.py    # Dijkstra's algorithm and adjacency matrix example
```

---

*Part of my Python learning journey 🐍 — diving into graph algorithms with real-world applications*
