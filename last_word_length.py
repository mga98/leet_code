def length_of_last_word(s: str) -> int:
    s = s.split()

    return len(s[-1])


if __name__ == '__main__':
    string = 'Hello World'
    last_word_length = length_of_last_word(string)
    print(last_word_length)
