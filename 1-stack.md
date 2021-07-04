![Stack Banner Image](images/stack.jpg)

## Introduction

The first data structure we will be looking at in this tutorial is the stack.

A **stack** is a collection of elements stored in a list. There are many actions we can perform on a stack depending on what we need. However, for the purposes of this tutorial, there are two main operations we perform on a stack: **pushing** and **popping**.

When we push, we add an element to the back of the stack. And when we pop, we remove an element from the back of the stack.

## Last In, First Out

Imagine a stack of books resting on a table, like so:

![Stack of Books](images/stack-of-books.png)

Now, imagine yourself taking a book (popping) from the stack. Where did you take the book from? The top, the bottom, the middle?

When it comes to programming, we always take the element (the book) from the back of the stack (which, in our example, is at the top). Likewise, we always append the element to the back of the stack.

This rule of pushing and popping from the back of the stack is known as **Last In First Out (LIFO)** because the _last_ element _in_ is also the _first_ to be taken _out_.

### Performance

| Stack Operation | Python Code | Performance
| --- | --- | ---
| **push** | `stack.append(value)` | O(1)*
| **pop** | `stack.pop()` | O(1)*
| **size** | `len(stack)` | O(1)*
| **empty** | `if len(stack) == 0:` | O(1)*

_*Note: The performance of these operations are based on the performance of the dynamic array._

As you can see, the overall performance of the stack is very good.

## The Function Stack

We use stacks all the time in software. This is because **functions** use the stack.

In Python, when a function is called, it is pushed to the stack.

## Example

```python
stack = []
stack.append("Moby Dick")
stack.append("The Great Gatsby")
stack.append("Hamlet")
stack.pop()
stack.append("The Iliad")
stack.append("Pride and Prejudice")
stack.pop()
stack.append("To Kill a Mockingbird")
stack.append("Gulliver's Travels")
stack.append("Don Quixote")
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack) # What will print?
```

## Problem to Solve