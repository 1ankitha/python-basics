# Sum of squares of first n natural numbers
def cubesum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i * i * i)
    return sum
n = int(input())
print(cubesum(n))
