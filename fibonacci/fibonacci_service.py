from datetime import datetime

def fibonacci_gen(seed1,seed2):
    """
    Fibonacci type sequence generator for 2 given seeds. X and Y
    """
    while True:
        yield seed1
        seed1, seed2 = seed2, seed1+seed2


def fibonacci_from_time():
    gen_time = datetime.now().time()
    minute = str(gen_time.minute)
    second = gen_time.second
    seed1, seed2 = int(minute[-2]) if len(minute) > 1 else 0, int(minute[-1])
    fib_gen = fibonacci_gen(seed1, seed2)
    return ([next(fib_gen) for _ in range(second)], gen_time.strftime("%H:%M:%S"))
        

    
if __name__ == "__main__":
    print(fibonacci_from_time())
