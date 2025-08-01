This is a rapid introduction about Exception.

In this exercice you'll just have to print the first argument passed to the script:


print(sys.argv[1])


But without actually checking if len(sys.argv) is long enough to have it.

So, sometimes, it will fail with an IndexError.

You'll have to catch this IndexError and print:

Not enough parameters.

