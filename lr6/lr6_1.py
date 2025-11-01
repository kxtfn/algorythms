import random
import time
import sys

sys.setrecursionlimit(20000)

def merge(arr, p, q, r, stats):
    n1 = q - p + 1
    n2 = r - q

    L = arr[p : p + n1]
    R = arr[q + 1 : q + 1 + n2]
    
    stats['assignments'] += (n1 + n2)

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        stats['comparisons'] += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        stats['assignments'] += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        stats['assignments'] += 1
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        stats['assignments'] += 1
        j += 1
        k += 1

def merge_sort(arr, p, r, stats=None):
    if stats is None:
        stats = {'comparisons': 0, 'assignments': 0}
    
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q, stats)
        merge_sort(arr, q + 1, r, stats)
        merge(arr, p, q, r, stats)
        
    return stats['comparisons'], stats['assignments']

def main():
    sizes = [10, 100, 1000, 5000, 10000]
    
    generators = {
        "Випадкова": lambda n: [random.randint(1, 1_000_000) for _ in range(n)],
        "Зростаюча": lambda n: list(range(1, n + 1)),
        "Спадна": lambda n: list(range(n, 0, -1))
    }
    
    print("--- Результати дослідження алгоритму сортування злиттям ---")
    print(f"{'Тип послідовності':<20} | {'Розмір (n)':<10} | {'Час (сек)':<15} | {'Порівняння':<15} | {'Присвоювання':<15}")
    print("-" * 80)
    
    for n in sizes:
        for name, gen_func in generators.items():
            data = gen_func(n)
            data_copy = list(data)
            
            start_time = time.perf_counter()
            comparisons, assignments = merge_sort(data_copy, 0, len(data_copy) - 1)
            end_time = time.perf_counter()
            
            elapsed_time = end_time - start_time
            
            print(f"{name:<20} | {n:<10} | {elapsed_time:<15.6f} | {comparisons:<15} | {assignments:<15}")
        
        print("-" * 80)

if __name__ == "__main__":
    main()