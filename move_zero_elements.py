def move_zeros(array: list[int]) -> list[int]:
    #your code here
    for i in array:
        if i == 0:
            array.append(array.pop(array.index(i)))
    return array

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(move_zeros(nums))