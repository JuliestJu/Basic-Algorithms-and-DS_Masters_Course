
import timeit
from dynamic import *
from greedy import *

def measure_execution_time(amount):
    # Measure time for greedy algorithm
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number = 1000)
    print(f"Greedy algorithm execution time: {greedy_time} seconds for 1000 executions")
    
    # Measure time for dynamic programming algorithm
    dp_time = timeit.timeit(lambda: find_min_coins(amount), number = 1000)
    print(f"Dynamic programming algorithm execution time: {dp_time} seconds for 1000 executions")

if __name__ == "__main__":
    amounts_to_test = [100, 500, 1000, 10000, 100000, 123, 997, 2501, 12345, 999731] 
    for amount in amounts_to_test:
        print(f"Measuring execution time for amount: {amount}")
        measure_execution_time(amount)
        print("\n")