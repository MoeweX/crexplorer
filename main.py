#!/usr/bin/env python3

from timeit import Timer
import math

memory_s = input("How much megabyte of memory should we allocate? Enter a number: ")
max_memory = int(memory_s)
start_printing = max(max_memory - 100, int(max_memory / 2))

def fibonacci(n):
    a = 0
    b = 1
    r = -1
    if n < 0:
        print("Incorrect input")
        return
    elif n == 0:
        r = a
    elif n == 1:
        r = b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        r = b
    # print("Fibonacci number {0!s} is {1!s}".format(n, r))

print("Starting CPU benchmark")
t = Timer(lambda: fibonacci(10000))
results = t.repeat(number=1000, repeat=3)
mean = sum(results) / len(results)
var  = sum(pow(x-mean,2) for x in results) / len(results)
std  = math.sqrt(var)  # standard deviation
print("Time needed for CPU benchmark: {0!s}s (SD={1!s}s)".format(mean, std))

print("Trying to allocate up to {1!s} mb of memory, print allocated amount starting at {0!s}:".format(start_printing, max_memory))
longstring = []
for x in range(1, max_memory + 1):
    longstring.append('1' * 10**6)
    if (x >= start_printing):
        print("{0!s}mb".format(len(longstring)), end = " ")

print("\nWas able to allocate all needed memory")
