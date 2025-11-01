import random

def main():
    variant = 1
    N = variant * 5 + 50
    
    hash_table = set()

    print(f"Початкова кількість елементів для додавання: {N}")

    for _ in range(N):
        hash_table.add(random.randint(1, 1000))
    
    print("\nПочаткова геш-таблиця:")
    print(sorted(list(hash_table)))
    print(f"Фактичний розмір таблиці: {len(hash_table)}")


    elements_to_delete = []
    for item in hash_table:
        if item % 2 == 0:
            elements_to_delete.append(item)

    for item in elements_to_delete:
        hash_table.remove(item)

    print("\nГеш-таблиця після видалення парних чисел:")
    if hash_table:
        print(sorted(list(hash_table)))
    else:
        print("Всі елементи були парними та їх було видалено.")

if __name__ == "__main__":
    main()