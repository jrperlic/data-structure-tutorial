![Linked List Banner Image](images/linked-list.jpg)

## Introduction

The second data structure we will be looking at in this tutorial is the linked list.

A **linked list** is a [noncontiguous](https://www.merriam-webster.com/thesaurus/noncontiguous) list. What does that mean? It means that the elements in a linked list are not located next to each other in memory.

For example, study the line of code below:

```python
fruits = ['apple', 'banana', 'orange']
```

The `fruits` list is a standard Python list. The `apple`, `banana`, and `orange` elements are located next to each other in memory. But if `fruits` was a linked list, its elements could be stored in disparate locations.

Before we move on, you should know that a linked list is organized differently from a regular list:

* Each element or **node** in a linked list contains a **value** and a link to the address of the next element.
* The first node is called the **head** and, as you might have guessed, the last node is called the **tail**.
* Some linked lists are extra fancy, maintaining a link to the next node as well as the previous node. When a linked list uses **bi-directional** linking, it is called a **doubly-linked list**.

## Inserting

When inserting a node into a linked list, there are three scenarios to consider:

1. [Inserting at the head](#inserting-at-the-head).
2. [Inserting at the tail](#inserting-at-the-tail).
3. [Inserting into the middle](#inserting-into-the-middle).

All three scenarios are similar, yet different enough that they deserve separate explanations. (For the code examples, make sure to import `deque`.)

### Inserting At the Head

```python
llist = deque("bcd")
llist.appendleft("a")
# deque(['a', 'b', 'c', 'd'])
```

### Inserting At the Tail

```python
llist = deque("bcd")
llist.append("e")
# deque(['b', 'c', 'd', 'e'])
```

### Inserting Into the Middle

```python
llist = deque("abde")
llist.insert(2, "c")
# deque(['a', 'b', 'c', 'd', 'e'])
```

## Removing

```python
llist = deque("abcd")
llist.popleft()
# deque(['b', 'c', 'd'])
```

```python
llist = deque("bcde")
llist.pop()
# deque(['b', 'c', 'd'])
```

```python
llist = deque("abcde")
llist.remove("c")
# deque(['a', 'b', 'd', 'e'])
```

## Accessing

```python
llist = deque("abcdef")
print(llist.index("e", 0, 5))
# 4
```

## Performance

| Linked List Operation | Python Code | Performance
| --- | --- | ---
| **insert_head** | `llist.appendleft(value)` | O(1)
| **insert_tail** | `llist.append(value)` | O(1)
| **insert** | `llist.insert(index, value)` | O(n)*
| **remove_head** | `llist.popleft()` | O(1)
| **remove_tail** | `llist.pop()` | O(1)
| **remove** | `llist.remove(value)` | O(n)*
| **size** | `len(llist)` | O(1)
| **empty** | `if len(llist) == 0:` | O(1)

_*Note: Inserting at and removing from the middle is slower because the index can't be found without using a loop._

## Example

Take a look at the `mystery1` and `mystery2` functions:

```python
def mystery1(ll):
    for i in reversed(ll):
        print(i, end=" ")
    print("")

def mystery2(ll):
    for i in range(0, len(ll), 2):
        print(ll[i], end=" ")
    for i in range(1, len(ll), 2):
        print(ll[i], end=" ")


ll = deque([1, 2, 3, 4, 5])

mystery1(ll)
mystery2(ll)
```

Can you predict what will be printed?

## Problem to Solve

You have a linked list that contains **n** integers.

Here is your task:

1. Find all **adjacent even integers** within the list. For example, if the list is `[2,4,5,6,8,10]`, the adjacent even integers are `[2,4]` and `[6,8,10]`.
1. Reverse the elements: `[2,4]` becomes `[4,2]`, and `[6,8,10]` becomes `[10,8,6]`.
1. Display the new linked list.

### I/O

| Example Input | Example Output
| ------------ | -------------
| `6`<br>`2 4 5 6 8 10` | `4 2 5 10 8 6`

### Hint

Use the [Stack](1-stack.md), Luke!