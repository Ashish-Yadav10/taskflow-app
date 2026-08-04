import copy
import random
from backend.algorithms import (
    insertion_sort_count,
    binary_search_count,
    linear_search_count
)

def generate_mock_tasks(size):
    priorities = ["low", "medium", "high"]
    tasks = []
    for i in range(size):
        tasks.append({
            "id": i,
            "title": f"Task Title {i}",
            "priority": random.choice(priorities),
            "due_date": "next friday"
        })
    return tasks

def benchmark():
    sizes = [10, 500, 3000]
    print("=== TASKFLOW ALGORITHM BENCHMARK RESULTS ===")
    
    for sz in sizes:
        tasks = generate_mock_tasks(sz)
        
        # 1. Insertion sort count
        tasks_for_sort = copy.deepcopy(tasks)
        sort_comps = insertion_sort_count(tasks_for_sort, "title")
        
        # 2. Linear search count (target absent)
        ls_res = linear_search_count(tasks, "Non-existent Task Title", "title")
        
        # 3. Binary search count (target absent on sorted data)
        bs_res = binary_search_count(tasks_for_sort, "Non-existent Task Title", "title")

        print(f"\n--- Dataset Size: {sz} records ---")
        print(f"Insertion Sort Comparisons: {sort_comps}")
        print(f"Linear Search Comparisons (Absent Target): {ls_res['comparison_count']}")
        print(f"Binary Search Comparisons (Absent Target): {bs_res['comparison_count']}")

if __name__ == "__main__":
    benchmark()
