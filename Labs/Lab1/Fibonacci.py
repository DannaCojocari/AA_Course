import math
import time
import matplotlib.pyplot as plt


def fibonacciBinet(n):
    if n < 0:
        return ValueError("The number can not be negative")
    elif n <= 1:
        return n

    Phi = (math.sqrt(5) + 1) / 2
    phi = Phi - 1

    return round((math.pow(Phi, n) - (- math.pow(phi, n))) / (Phi - (- phi)))


def fibonacciRecursive(n):
    if n < 0:
        return ValueError("The number can not be negative")
    elif n <= 1:
        return n
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


def fibonacciLinear(n):
    if n < 0:
        return ValueError("The number can not be negative")
    elif n <= 1:
        return n

    fibonacci = [0, 1]
    for i in range(2, n + 1):
        res = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(res)

    return fibonacci[-1]


def fibonacciMemoization(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    if n < 0:
        return ValueError("The number can not be negative")
    elif n <= 1:
        return n

    cache[n] = fibonacciMemoization(n - 1, cache) + fibonacciMemoization(n - 2, cache)
    return cache[n]


def fibonacciBottomUp(n):
    if n < 0:
        return ValueError("The number can not be negative")
    elif n <= 1:
        return n

    a = 0
    b = 1

    for _ in range(2, n + 1):
        temp = a + b
        a = b
        b = temp

    return b


def multiply(F1, F2):
    x = F1[0][0] * F2[0][0] + F1[0][1] * F2[1][0]
    y = F1[0][0] * F2[0][1] + F1[0][1] * F2[1][1]
    z = F1[1][0] * F2[0][0] + F1[1][1] * F2[1][0]
    w = F1[1][0] * F2[0][1] + F1[1][1] * F2[1][1]

    F1[0][0] = x
    F1[0][1] = y
    F1[1][0] = z
    F1[1][1] = w


def matrixPower(F1, n):
    if n == 0 or n == 1:
        return

    F2 = [[1, 1], [1, 0]]
    matrixPower(F1, n // 2)

    multiply(F1, F1)

    if n % 2 != 0:
        multiply(F1, F2)


def fibonacciMatrix(n):
    if n < 0:
        return ValueError("The number can not be negative")
    elif n <= 1:
        return n

    F1 = [[1, 1], [1, 0]]
    matrixPower(F1, n - 1)

    return F1[0][0]


def fibonacciFastDoubling(n):
    if n < 0:
        return ValueError("The number can not be negative")

    def fib(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = fib(n // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    return fib(n)[0]


array1 = [1, 3, 4, 6, 7, 9, 10, 13]
array2 = [27, 28, 29, 31, 38, 39, 41, 42, 45]
array3 = [115, 168, 240, 243, 421, 494, 548, 558, 644, 722, 750, 755, 758, 804, 862, 999]
array4 = [5620, 7464, 8157, 8504, 9136, 9935, 10725, 14202, 14368, 15694, 16818, 18274, 19559, 19701, 19945]

recursive = array1 + array2
binet = array1 + array2 + array3
memoization = array1 + array2 + array3
allNumbers = array1 + array2 + array3 + array4

execution_times = {
    "Recursive": [],
    "Binet": [],
    "Memoization": [],
    "Linear": [],
    "BottomUp": [],
    "FastDoubling": [],
    "Matrix": []
}

# Recursive testing
# for n in recursive:
#     start = time.perf_counter()
#     fibonacciRecursive(n)
#     execution_times["Recursive"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# plt.plot(recursive, execution_times["Recursive"], marker='o', label="Recursive")
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Recursive Algorithm")
# plt.legend()
# plt.grid()
# plt.show()



# Binet testing
# for n in binet:
#     start = time.perf_counter()
#     fibonacciBinet(n)
#     execution_times["Binet"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# plt.plot(binet, execution_times["Binet"], marker='o', label="Binet")
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Binet Algorithm")
# plt.legend()
# plt.grid()
# plt.show()


# Memoization testing
# for n in memoization:
#     start = time.perf_counter()
#     fibonacciMemoization(n)
#     execution_times["Memoization"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# plt.plot(memoization, execution_times["Memoization"], marker='o', label="Memoization")
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Memoization Algorithm")
# plt.legend()
# plt.grid()
# plt.show()


# Linear
# for n in allNumbers:
#     start = time.perf_counter()
#     fibonacciLinear(n)
#     execution_times["Linear"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# plt.plot(allNumbers, execution_times["Linear"], marker='o', label="Linear")
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Linear Algorithm")
# plt.legend()
# plt.grid()
# plt.show()


# BottomUp
# for n in allNumbers:
#     start = time.perf_counter()
#     fibonacciBottomUp(n)
#     execution_times["BottomUp"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# plt.plot(allNumbers, execution_times["BottomUp"], marker='o', label="BottomUp")
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("BottomUp Algorithm")
# plt.legend()
# plt.grid()
# plt.show()


# FastDoubling
# for n in allNumbers:
#     start = time.perf_counter()
#     fibonacciFastDoubling(n)
#     execution_times["FastDoubling"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# plt.plot(allNumbers, execution_times["FastDoubling"], marker='o', label="FastDoubling")
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("FastDoubling Algorithm")
# plt.legend()
# plt.grid()
# plt.show()


# Matrix
# for n in allNumbers:
#     start = time.perf_counter()
#     fibonacciMatrix(n)
#     execution_times["Matrix"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# plt.plot(allNumbers, execution_times["Matrix"], marker='o', label="Matrix")
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Matrix Algorithm")13
# plt.legend()
# plt.grid()
# plt.show()


# First test on all the algorithms
# for n in array1:
#     # Recursive
#     start = time.perf_counter()
#     fibonacciRecursive(n)
#     execution_times["Recursive"].append(time.perf_counter() - start)
#
#     # Binet
#     start = time.perf_counter()
#     fibonacciBinet(n)
#     execution_times["Binet"].append(time.perf_counter() - start)
#
#     # Memoization
#     start = time.perf_counter()
#     fibonacciMemoization(n)
#     execution_times["Memoization"].append(time.perf_counter() - start)
#
#     # Linear
#     start = time.perf_counter()
#     fibonacciLinear(n)
#     execution_times["Linear"].append(time.perf_counter() - start)
#
#     # BottomUp
#     start = time.perf_counter()
#     fibonacciBottomUp(n)
#     execution_times["BottomUp"].append(time.perf_counter() - start)
#
#     # FastDoubling
#     start = time.perf_counter()
#     fibonacciFastDoubling(n)
#     execution_times["FastDoubling"].append(time.perf_counter() - start)
#
#     # Matrix
#     start = time.perf_counter()
#     fibonacciMatrix(n)
#     execution_times["Matrix"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# for method, times in execution_times.items():
#     plt.plot(array1, times, marker='o', label=method)
#
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Fibonacci Algorithms")
# plt.legend()
# plt.grid()
# plt.show()


# Second test on all the algorithms
# for n in array2:
#     # Recursive
#     start = time.perf_counter()
#     fibonacciRecursive(n)
#     execution_times["Recursive"].append(time.perf_counter() - start)
#
#     # Binet
#     start = time.perf_counter()
#     fibonacciBinet(n)
#     execution_times["Binet"].append(time.perf_counter() - start)
#
#     # Memoization
#     start = time.perf_counter()
#     fibonacciMemoization(n)
#     execution_times["Memoization"].append(time.perf_counter() - start)
#
#     # Linear
#     start = time.perf_counter()
#     fibonacciLinear(n)
#     execution_times["Linear"].append(time.perf_counter() - start)
#
#     # BottomUp
#     start = time.perf_counter()
#     fibonacciBottomUp(n)
#     execution_times["BottomUp"].append(time.perf_counter() - start)
#
#     # FastDoubling
#     start = time.perf_counter()
#     fibonacciFastDoubling(n)
#     execution_times["FastDoubling"].append(time.perf_counter() - start)
#
#     # Matrix
#     start = time.perf_counter()
#     fibonacciMatrix(n)
#     execution_times["Matrix"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# for method, times in execution_times.items():
#     plt.plot(array2, times, marker='o', label=method)
#
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Fibonacci Algorithms")
# plt.legend()
# plt.grid()
# plt.show()


#Third test on all the algorithms except recursive
# for n in array3:
#     # Binet
#     start = time.perf_counter()
#     fibonacciBinet(n)
#     execution_times["Binet"].append(time.perf_counter() - start)
#
#     # Memoization
#     start = time.perf_counter()
#     fibonacciMemoization(n)
#     execution_times["Memoization"].append(time.perf_counter() - start)
#
#     # Linear
#     start = time.perf_counter()
#     fibonacciLinear(n)
#     execution_times["Linear"].append(time.perf_counter() - start)
#
#     # BottomUp
#     start = time.perf_counter()
#     fibonacciBottomUp(n)
#     execution_times["BottomUp"].append(time.perf_counter() - start)
#
#     # FastDoubling
#     start = time.perf_counter()
#     fibonacciFastDoubling(n)
#     execution_times["FastDoubling"].append(time.perf_counter() - start)
#
#     # Matrix
#     start = time.perf_counter()
#     fibonacciMatrix(n)
#     execution_times["Matrix"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# for method, times in execution_times.items():
#     if method != "Recursive":
#         plt.plot(array3, times, marker='o', label=method)
#
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Fibonacci Algorithms")
# plt.legend()
# plt.grid()
# plt.show()


# Fourth test on the most efficient algorithms
# for n in array4:
#     # Linear
#     start = time.perf_counter()
#     fibonacciLinear(n)
#     execution_times["Linear"].append(time.perf_counter() - start)
#
#     # BottomUp
#     start = time.perf_counter()
#     fibonacciBottomUp(n)
#     execution_times["BottomUp"].append(time.perf_counter() - start)
#
#     # FastDoubling
#     start = time.perf_counter()
#     fibonacciFastDoubling(n)
#     execution_times["FastDoubling"].append(time.perf_counter() - start)
#
#     # Matrix
#     start = time.perf_counter()
#     fibonacciMatrix(n)
#     execution_times["Matrix"].append(time.perf_counter() - start)
#
# plt.figure(figsize=(10, 6))
# for method, times in execution_times.items():
#     if method not in ["Recursive", "Binet", "Memoization"]:
#         plt.plot(array4, times, marker='o', label=method)
#
# plt.xlabel("Fibonacci Number (n)")
# plt.ylabel("Execution Time (seconds)")
# plt.title("Fibonacci Algorithms")
# plt.legend()
# plt.grid()
# plt.show()