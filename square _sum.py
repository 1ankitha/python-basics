# Sum of squares of first n natural numbers
def squaresum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i * i)
    return sum
n =int(input())
print(squaresum(n))
  
 or

def squaresum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6
n = int(input())
print(squaresum(n))
