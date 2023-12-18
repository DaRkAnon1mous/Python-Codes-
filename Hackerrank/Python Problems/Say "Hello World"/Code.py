#!/bin/python3

def fibonacci_sum_even_terms(limit):
    a, b = 1, 2
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum

def main():
   
    T = int(input())

    for _ in range(T):
      
        N = int(input())
        
        
        result = fibonacci_sum_even_terms(N)
        print(result)

if __name__ == "__main__":
    main()
