![Tree Banner Image](images/tree.jpg)

## Introduction

The third and final data structure we will be looking at in this tutorial is the tree.

A **tree** is a collection of nodes, similar to a [linked list](2-linked-list.md), that is organized in a **hierarchical** structure. What does that mean? In the case of a tree, it means that the nodes are organized into two groups: **parents**, and **children**.

A parent node is a node that links to other nodes. Likewise, a child node is connected to the parent. (It is possible for a node to be _both_ a parent and child.)

Two more things before we continue:

1. The topmost node is called the **root**.
1. A node that connects to no other node is called a **leaf**.

## Binary Trees

A **binary search tree (BST)** is a tree in which the nodes link to no more than _two_ other nodes. A BST has left and right subtrees, which are formed by the nodes to the left and right of any parent.

![Binary Tree](images/binary-tree.png)

Furthermore, there is a special rule that must be followed when data is added to the BST: If the data value is less than the parent node, it is put in the left subtree. If the value is greater than the parent node, it is put in the right subtree. _The data in a BST is always sorted_ from left to right and from least to greatest.

## Recursion

## Inserting

(For the code examples, make sure to install [treelib](https://treelib.readthedocs.io/en/latest/).)

## Traversing

## Performance

| Tree Operation | Python Code | Performance
| --- | --- | ---
| **insert** |  | O(log n)
| **remove** |  | O(log n)
| **contains** |  | O(log n)
| **traverse_forward** |  | O(log n)
| **traverse_backward** |  | O(log n)
| **height** | `tree.depth()` | O(log n)
| **size** |  | O(1)
| **empty** |  | O(1)

## Example

## Problem to Solve