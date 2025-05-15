# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import math as m
import statistics as stpy
from scipy import stats

# Define function
def mean_confidence_interval(length, mean, stdev):
    return 1.96 * (stdev / m.sqrt(length))

# Input
total = int(input())
numbers = list(map(int, input().split()))

# Set statistics values
mean = np.mean(numbers)
median = np.median(numbers)
mode = int(stats.mode(numbers)[0])
stdev = stpy.pstdev(numbers)
confidence_interval = mean_confidence_interval(total, mean, stdev)
min_confidence = round(mean - confidence_interval, 1)
max_confidence = round(mean + confidence_interval, 1)

# Show the final result
print(round(mean,1))
print(round(median,1))
print(mode)
print(round(stdev,1))
print("{} {}".format(min_confidence, max_confidence))