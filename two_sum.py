def two_sum(nums: list, target: int) -> list:
    values = {}

    for i, elem in enumerate(nums):
        comp = target - elem

        if comp in values:
            return [values[comp], i]

        values[elem] = i

    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)
