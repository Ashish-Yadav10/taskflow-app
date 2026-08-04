from backend.algorithms import (
    insertion_sort, binary_search, linear_search,
    insertion_sort_count, binary_search_count, linear_search_count
)

def run_checks():
    # Case 1: insertion_sort on empty list
    empty_list = []
    insertion_sort(empty_list, "key")
    if empty_list == []:
        print("PASS: insertion_sort on empty list")
    else:
        print(f"FAIL: insertion_sort on empty list — expected [], got {empty_list}")

    # Case 2: insertion_sort on single element
    single_list = [{"a": 1}]
    insertion_sort(single_list, "a")
    if single_list == [{"a": 1}]:
        print("PASS: insertion_sort on single element")
    else:
        print(f"FAIL: insertion_sort on single element — expected [{{'a': 1}}], got {single_list}")

    # Case 3: binary_search at first, last, middle
    arr = [{"k": 10}, {"k": 20}, {"k": 30}, {"k": 40}, {"k": 50}]
    idx_first = binary_search(arr, 10, "k")
    idx_mid = binary_search(arr, 30, "k")
    idx_last = binary_search(arr, 50, "k")

    if idx_first == 0 and idx_mid == 2 and idx_last == 4:
        print("PASS: binary_search first, middle, and last indices")
    else:
        print(f"FAIL: binary_search positions — expected (0,2,4), got ({idx_first},{idx_mid},{idx_last})")

    # Case 4: binary_search not found
    idx_absent = binary_search(arr, 99, "k")
    if idx_absent == -1:
        print("PASS: binary_search target absent")
    else:
        print(f"FAIL: binary_search absent — expected -1, got {idx_absent}")

    # Case 5: insertion_sort_count on hand-checkable list
    data = [{"val": 3}, {"val": 1}, {"val": 2}]
    count = insertion_sort_count(data, "val")
    if data == [{"val": 1}, {"val": 2}, {"val": 3}] and type(count) == int and count > 0:
        print("PASS: insertion_sort_count sort accuracy and count integer type")
    else:
        print(f"FAIL: insertion_sort_count test — got sorted {data}, count {count}")

    # Case 6: binary_search_count present
    sorted_data = [{"val": 10}, {"val": 20}, {"val": 30}]
    res_bs = binary_search_count(sorted_data, 20, "val")
    if res_bs.get("index") == 1 and isinstance(res_bs.get("comparison_count"), int) and res_bs["comparison_count"] > 0:
        print("PASS: binary_search_count index and integer count")
    else:
        print(f"FAIL: binary_search_count — expected index 1, got {res_bs}")

    # Case 7: linear_search_count absent
    unsorted_data = [{"val": 5}, {"val": 15}, {"val": 25}]
    res_ls = linear_search_count(unsorted_data, 99, "val")
    if res_ls.get("index") == -1 and res_ls.get("comparison_count") == len(unsorted_data):
        print("PASS: linear_search_count absent index and length count")
    else:
        print(f"FAIL: linear_search_count absent — expected (-1, 3), got {res_ls}")

if __name__ == "__main__":
    run_checks()
