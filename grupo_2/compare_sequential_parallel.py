import time
from prime_count_parallel import count_primes_in_range, parallel_prime_count

if __name__ == "__main__":
    max_val = 100000
    
    start = time.time()
    seq_count = count_primes_in_range(1, max_val)
    seq_time = time.time() - start
    
    start = time.time()
    par_count = parallel_prime_count(max_val, processes=4)
    par_time = time.time() - start
    
    print(f"Sequencial: {seq_count} primos, Tempo: {seq_time:.4f} s")
    print(f"Paralelo:   {par_count} primos, Tempo: {par_time:.4f} s")
