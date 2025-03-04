import concurrent.futures
import time

def partial_sum(numbers):
    return sum(numbers)

def parallel_sum(numbers, num_workers=4):
    size = len(numbers)
    chunk = size // num_workers
    futures = []
    total = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        for i in range(num_workers):
            start = i * chunk
            end = size if i == num_workers - 1 else (i + 1) * chunk
            futures.append(executor.submit(partial_sum, numbers[start:end]))
        for f in concurrent.futures.as_completed(futures):
            total += f.result()
    return total

if __name__ == "__main__":
    data = range(1_000_0000)  # 10 milhões, se desejar
    start_time = time.time()
    total_parallel = parallel_sum(data)
    elapsed_parallel = time.time() - start_time

    start_time = time.time()
    total_sequential = sum(data)
    elapsed_sequential = time.time() - start_time

    print(f"Soma Paralela: {total_parallel}, Tempo: {elapsed_parallel:.4f} s")
    print(f"Soma Sequencial: {total_sequential}, Tempo: {elapsed_sequential:.4f} s")
