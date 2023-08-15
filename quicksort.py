
def quicksort(array: list[int]) -> list[int]:
    if len(array) < 1:
        return array
    else:
        pivot: int = array[0]
        less: list = [i for i in array[1:] if i <= pivot]
        greater: list = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    data: list[int] = [ 9, 3, 5, 1, 7, 12, 2 ]

    sorted_data: list[int] = quicksort(data)
    print(f"sorted data ::: {sorted_data}")
