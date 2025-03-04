import multiprocessing

def multiply_rows(A, B, rows):
    result_part = []
    for r in rows:
        row_result = []
        for j in range(len(B[0])):
            cell_sum = 0
            for k in range(len(B)):
                cell_sum += A[r][k] * B[k][j]
            row_result.append(cell_sum)
        result_part.append((r, row_result))
    return result_part

def parallel_matrix_multiply(A, B):
    n = len(A)
    num_workers = 2  # ajuste conforme seu ambiente
    chunk_size = n // num_workers
    pool = multiprocessing.Pool(num_workers)
    tasks = []
    for i in range(num_workers):
        start = i * chunk_size
        end = n if i == num_workers - 1 else (i + 1) * chunk_size
        tasks.append(pool.apply_async(multiply_rows, (A, B, range(start, end))))
    pool.close()
    pool.join()
    result = [[0]*len(B[0]) for _ in range(n)]
    for t in tasks:
        partial = t.get()
        for row_index, row_values in partial:
            result[row_index] = row_values
    return result

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[9,8,7],[6,5,4],[3,2,1]]
    result = parallel_matrix_multiply(A, B)
    print("Matriz resultante:")
    for row in result:
        print(row)
