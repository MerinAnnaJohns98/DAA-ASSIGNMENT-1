"""
Insertion Sort
Sorts a list of integers in ascending order using insertion sort.
"""

def insertion_sort(values):
    """Sort values in place and return the sorted list."""
    # Start from the second element; the first element is already sorted.
    for i in range(1, len(values)):
        key = values[i]  # Value to insert into the sorted portion
        j = i - 1

        # Shift elements larger than key one position to the right.
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1

        # Place key in its correct position.
        values[j + 1] = key

    return values


def main():
    try:
        numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    insertion_sort(numbers)
    print("Sorted array:", *numbers)


if __name__ == "__main__":
    main()
