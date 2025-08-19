# Problema 6 – Fibonacci recursiv (10p)

def fib(n: int) -> int:
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    print(fib(6))  # 8
#fib(10) returneaza 55

