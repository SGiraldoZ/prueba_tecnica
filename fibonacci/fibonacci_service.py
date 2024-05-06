from datetime import datetime

def fibonacci_gen(seed1,seed2):
    """
    Fibonacci type sequence generator for 2 given seeds. X and Y
    """
    if seed1> seed2:
        seed1, seed2 = seed2, seed1
    while True:
        yield seed1
        seed1, seed2 = seed2, seed1+seed2


def fibonacci_from_time():
    """
    Generate a Fibonacci type sequence from the current time. Using the digits of the minutes as seeds.
    And the number for the required number of elements
    """
    gen_time = datetime.now().time()
    minute = str(gen_time.minute)
    second = gen_time.second
    seed1, seed2 = int(minute[-2]) if len(minute) > 1 else 0, int(minute[-1])
    fib_gen = fibonacci_gen(seed1, seed2)
    # Second + 2 to exclude the 2 seeds
    return ([next(fib_gen) for _ in range(second+2)], gen_time.strftime("%H:%M:%S"))
        

    
if __name__ == "__main__":
    print(fibonacci_from_time())
