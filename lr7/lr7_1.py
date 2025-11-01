import random
import time

def heapify(arr, n, i, stats):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    stats['comparisons'] += 2 # два порівняння 
    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        stats['assignments'] += 3 # за одну операцію обміну
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, stats)

def heap_sort(arr):
    stats = {'comparisons': 0, 'assignments': 0}
    n = len(arr)

    # побудова максимальної купи 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, stats)

    # вилучення елементів з купи один за одним
    for i in range(n - 1, 0, -1):
        stats['assignments'] += 3 # за одну операцію обміну
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, stats)
        
    return stats['comparisons'], stats['assignments']

def generate_random(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

def generate_ascending(n):
    return list(range(1, n + 1))

def generate_descending(n):
    return list(range(n, 0, -1))

def main():
    sizes = [10, 100, 1000, 5000, 10000]
    
    print("--- Результати дослідження алгоритму сортування купою ---")
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
            comparisons, assignments = heap_sort(data)
            end_time = time.perf_counter()
            
            elapsed_time = end_time - start_time
            
            print(f"{name:<20} | {n:<10} | {elapsed_time:<15.6f} | {comparisons:<15} | {assignments:<15}")
        
        print("-" * 80)

if __name__ == "__main__":
    main()