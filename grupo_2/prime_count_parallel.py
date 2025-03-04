import math
import multiprocessing

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

def parallel_prime_count(n, processes=4):
    chunk = n // processes
    pool = multiprocessing.Pool(processes)
    tasks = []
    current_start = 1
    for i in range(processes):
        current_end = n if i == processes - 1 else current_start + chunk - 1
        tasks.append(pool.apply_async(count_primes_in_range, (current_start, current_end)))
        current_start = current_end + 1
    pool.close()
    pool.join()
    return sum(t.get() for t in tasks)

if __name__ == "__main__":
    max_val = 100000
    total_primes = parallel_prime_count(max_val, processes=4)
    print(f"Número de primos de 1 até {max_val}: {total_primes}")
