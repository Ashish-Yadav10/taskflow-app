import re

def insertion_sort(records, key):
    """Sorts a list of dictionaries in place by record[key]."""
    for i in range(1, len(records)):
        current_item = records[i]
        j = i - 1
        while j >= 0 and records[j][key] > current_item[key]:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = current_item


def binary_search(sorted_records, target_value, key):
    """Returns the index of a record matching target_value, or -1 if not found."""
    low = 0
    high = len(sorted_records) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_records[mid][key] == target_value:
            return mid
        elif sorted_records[mid][key] < target_value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def linear_search(records, target_value, key):
    """Scans records in order and returns index of target_value, or -1."""
    for i, rec in enumerate(records):
        if rec[key] == target_value:
            return i
    return -1


# Counting wrappers for Section 2 Benchmarks
def insertion_sort_count(records, key):
    comparisons = 0
    for i in range(1, len(records)):
        current_item = records[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if records[j][key] > current_item[key]:
                records[j + 1] = records[j]
                j -= 1
            else:
                break
        records[j + 1] = current_item
    return comparisons


def binary_search_count(sorted_records, target_value, key):
    comparisons = 0
    low = 0
    high = len(sorted_records) - 1
    index = -1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if sorted_records[mid][key] == target_value:
            index = mid
            break
        elif sorted_records[mid][key] < target_value:
            low = mid + 1
        else:
            high = mid - 1

    return {"index": index, "comparison_count": comparisons}


def linear_search_count(records, target_value, key):
    comparisons = 0
    index = -1
    for i, rec in enumerate(records):
        comparisons += 1
        if rec[key] == target_value:
            index = i
            break
    return {"index": index, "comparison_count": comparisons}
