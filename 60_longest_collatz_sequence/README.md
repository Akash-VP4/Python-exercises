The collatz sequence goes like this:

Start by any number greater than zero.
If your number is even, divide it by two.
If your number os odd, multiply by three and add one.
For example, starting by 10 we have:


10 → 5 → 16 → 8 → 4 → 2 → 1
Write a function, named collatz_length, given a number the function return the length of the sequence before reaching 1, for example:



>>> collatz_length(10)
6