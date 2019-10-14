import time
import numpy as np
import plotly.express as px


def fib_recursion(n):
    """Fibonacci function with recursive aproach"""
    if n==1 or n==2:
        return 1
    return fib_recursion(n-1) + fib_recursion(n-2)


def fib_memoize(n, memo):
    """Fibonacci function with memoize approach"""

    if memo[n] != 0:
        return memo[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_memoize(n-1, memo) + fib_memoize(n-2, memo)
    
    memo[n] = result
    return result


def fib_bottom_up(n):
    """Fibonacci function with bottom up approach"""

    # Store i-2 and i-1 value
    memo = [1,1]

    for i in range(3,n):
        res = memo[0] + memo[1]
        memo[0] = memo[1]
        memo[1] = res

    return res


def main():
    """Compute time to execute two different aproaches"""

    # n_values = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    n_values = np.array([5, 10, 15, 20])
    nb_values = len(n_values)

    result = {
        'recursion' : np.zeros(nb_values),
        'memoize': np.zeros(nb_values),
        'bottom_up': np.zeros(nb_values)
    }


    for i in range(nb_values):

        n_value = n_values[i]
        print(n_value)

        start = time.process_time()
        fib_recursion(n_value)
        result['recursion'][i] = (time.process_time() - start)

        start = time.process_time()
        memo = [0 for i in range(n_value+1)]
        fib_memoize(n_value, memo)
        result['memoize'][i] = (time.process_time() - start)

        start = time.process_time()
        fib_bottom_up(n_value)
        result['bottom_up'][i] = (time.process_time() - start)

    print(result)


    
if __name__ == "__main__":
    main()