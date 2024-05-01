
import timeit
import random
from insertion_sort import insertionSort
from merge_sort import mergeSort
from data_sets_creator import generate_datasets, print_datasets

def main():
    # Generate datasets
    datasets = generate_datasets()
    
    # Define setup string
    setup = """
from insertion_sort import insertionSort
from merge_sort import mergeSort
import random
"""
    
    # Perform timing tests
    for dataset_type, dataset_list in datasets.items():
        print(f"Dataset Type: {dataset_type}")
        for data in dataset_list:
            print(f"Dataset Size: {len(data)}")
            
            # Timing insertionSort
            insertion_sort_time = timeit.timeit(stmt="insertionSort(data[:])", setup=setup, globals={'data': data}, number=1000)
            print("Insertion Sort Time:", insertion_sort_time)
            
            # Timing mergeSort
            merge_sort_time = timeit.timeit(stmt="mergeSort(data[:])", setup=setup, globals={'data': data}, number=1000)
            print("Merge Sort Time:", merge_sort_time)
            
            # Timing Timsort (Python's built-in sort)
            timsort_time = timeit.timeit(stmt="sorted(data[:])", setup=setup, globals={'data': data}, number=1000)
            print("Timsort Time:", timsort_time)
            
            print()  # Add a blank line for readability

if __name__ == "__main__":
    main()