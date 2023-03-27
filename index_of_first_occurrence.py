def str_str(haystack: str, needle: str) -> int:
    m = len(needle)
    n = len(haystack)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1


if __name__ == '__main__':
    haystack = 'sadbutsad'
    needle = 'sad'
    result = str_str(haystack, needle)
    print(result)
