import time
from multiprocessing import Pool, cpu_count


def get_factors(n):
    return [i for i in range(1, abs(n) + 1) if n % i == 0]


# Синхронна реалізація
def factorize_sync(*numbers):
    return [get_factors(num) for num in numbers]

# Багатопроцесорна реалізація
def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(get_factors, numbers)
    return results


# Замір часу виконання
if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    # Синхронний запуск
    start_time = time.time()
    sync_result = factorize_sync(*numbers)
    sync_time = time.time() - start_time
    print("Синхронний результат:", sync_result)
    print("Час виконання (синхронно):", sync_time, "секунд")

    # Багатопроцесорний запуск
    start_time = time.time()
    parallel_result = factorize_parallel(*numbers)
    parallel_time = time.time() - start_time
    print("Паралельний результат:", parallel_result)
    print("Час виконання (паралельно):", parallel_time, "секунд")

    # Перевірка правильності
    a, b, c, d = sync_result  # або parallel_result
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
                 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
