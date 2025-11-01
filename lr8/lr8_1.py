import random
import time
import sys

sys.setrecursionlimit(20000)

def partition(arr, p, r, stats):
    x = arr[r]
    stats['assignments'] += 1
    
    i = p - 1
    stats['assignments'] += 1

    for j in range(p, r):
        stats['comparisons'] += 1
        if arr[j] <= x:
            i += 1
            stats['assignments'] += 4 
            arr[i], arr[j] = arr[j], arr[i]
            
    stats['assignments'] += 3 
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quick_sort_recursive(arr, p, r, stats):
    if p < r:
        q = partition(arr, p, r, stats)
        quick_sort_recursive(arr, p, q - 1, stats)
        quick_sort_recursive(arr, q + 1, r, stats)

def run_quick_sort(arr):
    stats = {'comparisons': 0, 'assignments': 0}
    arr_copy = list(arr) 
    quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1, stats)
    return stats['comparisons'], stats['assignments']

def generate_random(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

def generate_ascending(n):
    return list(range(1, n + 1))

def generate_descending(n):
    return list(range(n, 0, -1))

def main():
    sizes = [10, 100, 1000, 5000, 10000]
    
    print("--- Результати дослідження алгоритму швидкого сортування ---")
    print(f"{'Тип послідовності':<20} | {'Розмір (n)':<10} | {'Час (сек)':<15} | {'Порівняння':<15} | {'Присвоювання':<15}")
    print("-" * 80)
    
    for n in sizes:
        generators = {
            "Випадкова": generate_random,
            "Зростаюча": generate_ascending,
            "Спадна": generate_descending
        }
        
        for name, gen_func in generators.items():
            data = gen_func(n)
            
            start_time = time.perf_counter()
            comparisons, assignments = run_quick_sort(data)
            end_time = time.perf_counter()
            
            elapsed_time = end_time - start_time
            
            print(f"{name:<20} | {n:<10} | {elapsed_time:<15.6f} | {comparisons:<15} | {assignments:<15}")
        
        print("-" * 80)

if __name__ == "__main__":
    main()