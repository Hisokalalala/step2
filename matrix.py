import numpy
import sys
import time
from matplotlib import pyplot as plt


if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])
a = numpy.zeros((n, n))  # Matrix A
b = numpy.zeros((n, n))  # Matrix B
c = numpy.zeros((n, n))  # Matrix C

# Initialize the matrices to some values.
for i in range(n):
    for j in range(n):
        a[i, j] = i * n + j
        b[i, j] = j * n + i
        c[i, j] = 0


def product(m1, m2):
    size = len(m1)
    result = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


begin = time.time()

######################################################
# Write code to calculate C = A * B                  #
# (without using numpy librarlies e.g., numpy.dot()) #
######################################################
c = product(a, b)

end = time.time()
# print("time: %.6f sec" % (end - begin))

# to draw the graph
# (N, time)
x = [3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 67, 100, 200, 400, 500, 700, 1000]
y = [0.000033, 0.000061, 0.000099, 0.000215, 0.000325, 0.000374, 0.000539, 0.001361, 0.005425, 0.017417,
     0.040709, 0.082543, 0.197933, 0.631375, 5.699142, 45.014128, 88.360380, 258.377851, 773.905043]

plt.title('N-time Graph')
plt.xlabel('N-Axis')
plt.ylabel('time-Axis')

plt.plot(x, y)
plt.show()


"""
# Print C for debugging. Comment out the print before measuring the execution time.
total = 0
for i in range(n):
    for j in range(n):
        # print c[i, j]
        total += c[i][j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
print("sum: %.6f" % total)
"""
