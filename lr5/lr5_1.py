import random
import time

def insertion_sort(arr):
    comparisons = 0  # лічильник порівнянь
    assignments = 0  # лічильник присвоювань

    for j in range(1, len(arr)):
        
        key = arr[j]
        assignments += 1
        i = j - 1
        
        while i >= 0:
            comparisons += 1  # рахуємо порівняння (arr[i] > key)
            if arr[i] > key:
                arr[i + 1] = arr[i]
                assignments += 1
                i -= 1
            else:
                break
        
        arr[i + 1] = key
        assignments += 1
        
    return comparisons, assignments

def generate_random(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

def generate_ascending(n): # за зростанням
    return list(range(1, n + 1))

def generate_descending(n): # за спаданням
    return list(range(n, 0, -1))

def main():
    sizes = [10, 100, 1000, 5000, 10000]
    
    print("--- Результати дослідження алгоритму сортування вставками ---")
    print(f"{'Тип послідовності':<20} | {'Розмір (n)':<10} | {'Час (сек)':<15} | {'Порівняння':<15} | {'Присвоєння':<15}")
    print("-" * 80)
    
    for n in sizes:
        generators = {
            "Випадкова": lambda: generate_random(n),
            "Зростаюча": lambda: generate_ascending(n),
            "Спадна": lambda: generate_descending(n)
        }
        
        for name, gen_func in generators.items():

            data = gen_func()

            start_time = time.perf_counter()
            
            comparisons, assignments = insertion_sort(data)
            
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            
            print(f"{name:<20} | {n:<10} | {elapsed_time:<15.6f} | {comparisons:<15} | {assignments:<15}")
        
        print("-" * 80) 

if __name__ == "__main__":
    main() 