![Tutorial Banner Image](images/tutorial.jpg)

## Introduction

Welcome to the Python Data Structures Tutorial! If you're familiar with functional programming in Python and want to improve your coding skills, then you've come to the right place.

## Overview

The following data structures are covered in this tutorial:

- [Stack](1-stack.md)
- [Linked List](2-linked-list.md)
- [Tree](3-tree.md)

There are descriptions and examples in each module. You will find a problem to solve on your own at the end of each module. You should only look at the solution after you have attempted to solve the problem first.

## Frequently Asked Questions

**Contents**

* [What are data structures?](#what-are-data-structures)
* [What is performance?](#what-is-performance)
* [What do I do when I'm stuck on a problem?](#what-do-i-do-when-im-stuck-on-a-problem)
* [Where can I learn more about data structures?](#where-can-i-learn-more-about-data-structures)

### What are data structures?

Put simply, data structures are the way we are able to store and retrieve data. They are _the_ fundamental building block of computer science.

You should already be familiar with Python lists and dictionaries. Both are prime examples of data structures.

### What is performance?

In computer science, performance is a measure of how long it takes code to run. [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation) is the language we use for talking about code performance for large sets of data.

Consider this Python code:

```python
def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
```

The size of the data in `sum` is based on the size of `numbers`. For the purposes of this example, we will say that the size of `numbers` is `n`. Because of the `for` loop in the code, the function will run `n` times. Therefore, we say that the big O of `sum` is O(n).

| Time Complexity | Big O
| --------------- | -----
| **Constant** | O(1)
| **Logarithmic** | O(log n)
| **Linear** | O(n)
| **Quadratic** | O(n^2)
| **Exponential** | O(2^n)

### What do I do when I'm stuck on a problem?

When you're stuck on a problem, consider following this [four-step process](https://asq.org/quality-resources/problem-solving):

1. Understand the Problem
1. Plan and Design the Solution
1. Implement the Solution
1. Evaluate the Solution

### Where can I learn more about data structures?

If you want to learn more about data structures, there are many online resources available. Remember, [Google is your best friend](https://giybf.com/).

## Contact

For additional questions and comments, please send them to:

Jared Perlic, BYU-Idaho, CSE 212, Section 2

jperlic@byui.edu