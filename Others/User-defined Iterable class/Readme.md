# Listwork Iterator

## Overview

Listwork is a Python class that provides an iterator for computing the sum of consecutive elements in a list. This iterator takes a list as input and, on each iteration, returns the sum of the current and next elements in the list.

## Usage

To use Listwork, create an instance of the class by providing a list of numbers. Then, iterate over the instance using a `for` loop to get the sums of consecutive elements.

```python
Liist = Listwork([12, 24, 36, 48, 50])

for i in Liist:
    print(i)
```
This will output the sums of consecutive elements in the provided list.

Example
For the input list [12, 24, 36, 48, 50], the output will be:

python
36
60
84
98

## How it works

The Listwork class initializes with a list and keeps track of two indices, l1 and l2, representing consecutive elements in the list. On each iteration, it calculates the sum of the current and next elements, updating the indices accordingly.

## Why use Listwork?

Listwork provides a simple and efficient way to calculate the sums of consecutive elements in a list using an iterator. It can be useful in scenarios where you need to perform operations on pairs of elements in a sequential manner.

## Contribution
Feel free to contribute to the project by forking the repository, making improvements, and creating pull requests. Bug reports and suggestions are also welcome.

## Demo
![image](https://github.com/DaRkAnon1mous/Python-Codes-/assets/86824571/ca903c61-ae15-4df5-b7ae-482d71f46f89)
