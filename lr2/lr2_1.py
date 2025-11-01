import random
from collections import deque

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True # число просте

def main():
    variant = 1
    S = variant * 5 + 50
    
    cherha = deque(maxlen=S) # не більше S елементів

    for _ in range(S):
        randoms = random.randint(1, 1000)
        cherha.append(randoms)
    
    prosti_chysla = []
    while cherha:
        element = cherha.popleft()
        if is_prime(element):
            prosti_chysla.append(str(element)) # збереження простих чисел як рядків

    if prosti_chysla:
        print("Знайдені прості числа:")
        print(", ".join(prosti_chysla))
    else:
        print("Простих чисел у черзі не знайдено.")

if __name__ == "__main__":
    main()