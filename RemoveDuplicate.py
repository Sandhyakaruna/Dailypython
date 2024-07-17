def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def remove_duplicates(arr):
    # Use bubble sort to sort the array
    bubble_sort(arr)

    # Create a new array to hold unique elements
    unique_arr = []

    # Add the first element to the unique array
    if len(arr) > 0:
        unique_arr.append(arr[0])

    # Traverse the array and add elements to the unique array if they are not duplicates
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_arr.append(arr[i])

    return unique_arr
    def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = remove_duplicates(arr)
    
    # Print the unique elements separated by a space
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

