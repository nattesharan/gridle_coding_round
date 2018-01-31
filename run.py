'''Imagine a given set of numbers wherein some are cannibals. We define a cannibal as a larger number can eat a smaller number and increase its value by 1. There are no restrictions on how many numbers any given number can consume. A number which has been consumed is no longer available.

Output:

Your task is to determine the number of numbers which can have a value equal to or greater than a specified value.

Explanation:

You'll be given two integers, i and j, on the first line. i indicates how many values you'll be given, and j indicates the number of queries.

Example:

7 2
21 9 5 8 10 1 3
10 15

Based on the above description, 7 is number of values that you will be given. 2 is the number of queries.

That means -
* Query 1 - How many numbers can have the value of at least 10
* Query 2 - How many numbers can have the value of at least 15

Your program should calculate and show the number of numbers which are equal to or greater than the desired number

The result is:
4 2 '''
result = []
i,j = map(int, input('Enter i and j: ').strip().split())
series = []
while len(series) != i:
    print('Please enter %d numbers separated by space'%(i))
    series = list(map(int, input().strip().split()))
queries = []
while len(queries) != j:
    print('Please enter %d queries separated by space'%(j))
    queries = list(map(int,input().strip().split()))
series = sorted(series,reverse=True)
for query in queries:
    count = 0
    for value in series:
        if value >= query:
            count += 1
        else:
            val = sum(num < value for num in series)
            if (val+value) >= query:
                count += 1
    result.append(count)
print(" ".join(map(str, result)))
