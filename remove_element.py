def remove_element(nums: list, val: int) -> int:
    # Enquanto houver o valor target na lista de números.
    while val in nums:
        # Remove o valor da lista.
        nums.remove(val)

    return len(nums)


if __name__ == '__main__':
    lst = [3,2,2,3]
    val = 3
    remove_elem_v2 = remove_element(lst, val)
    print(remove_elem_v2)
