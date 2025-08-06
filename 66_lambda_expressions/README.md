A function can be expressed in a concise way called lambda expression. More generically, it's called an "anonymous function" because it doesn't have a name.

The function syntax is:

def the_name(parameter):
    return parameter * 2
The lambda syntax is:


lambda x: x * 2
As you see it has no name, and it's very concise.

It's particularly useful in order to give a minimalist function directly as a parameter of another function, typically, the builtin sorted.


>>> li = [('antoine', 18), ('julien', 42), ('kevin', 9)]
>>> sorted(li, key=lambda x: x[1])
[('kevin', 9), ('antoine', 18), ('julien', 42)]
In this exercise, you'll write a function named filtered, taking two parameters: an iterable, typically a list, and a filter, a lambda expression. Your function filtered should return an iterable (a list for example).


>>> items = [1, 2, 3, 4, 5, 6]
>>> even = filtered(items, lambda x: x % 2 == 0)
>>> odds = filtered(items, lambda x: x % 2 == 1)
>>> even
[2, 4, 6]
>>> odds
[1, 3, 5]
Obviously your filtered function should also work if passed a function name instead of a lambda expression.


items = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 == 1

even = filtered(items, is_even) # 2 4 6
odds = filtered(items, is_odd) # 1 3 5
(Now you see why we use lambda.)

After your filtered function, you'll write three lines using your filtered function and lambdas:

print all numbers from 0 to 100 included that are multiple of 3
print all numbers from 0 to 100 included that are multiple of 5
print all numbers from 0 to 100 included that are multiple of 15
Numbers should be separated by comas, one list per line, such as:


0, 3, 6, 9, ...
0, 5, 10, 15, ...
0, 15, 30, 45, ...
